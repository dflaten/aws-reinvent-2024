import time
import json
import boto3
import logging
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.metrics import MetricResolution
from aws_lambda_powertools.utilities.typing import LambdaContext

metrics = Metrics()
_ddb_client = None
#
def get_ddb_client():
    global _ddb_client
    if _ddb_client is None:
        _ddb_client = boto3.client('dynamodb')
    return _ddb_client
# Inefficient: Initializations inside, see comments below
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event, context):

    custom_metric_invocations_name = 'SuccessfulInvocations'
    custom_metric_duration_name = 'FunctionDuration'
    #execution "counter"
    value = 1

    metrics.add_dimension(name="function_name", value=context.function_name)
    #initial marker to track the duration of the function
    start_time = time.time()

    # Inefficient logging with high verbosity
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger()
    logger.debug(f"Received event: {json.dumps(event)}")
    try:
        order = json.loads(event['body'])
        order_id = order['orderId']
        customer_id = order['customerId']
        product_id = order['productId']
        quantity = int(order['quantity'])
        price = int(order['price'])
    except (KeyError, ValueError, TypeError) as e:
        logger.error(f"Error parsing event: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps('Bad Request')
        }
    # Inefficient: Initialize boto3 DynamoDB client inside the handler
    dynamodb = get_ddb_client()
    try:
        dynamodb.put_item(
            TableName='OrdersTable',
            Item={
                'orderId': {'S': order_id},
                'customerId': {'S': customer_id},
                'productId': {'S': product_id},
                'Quantity': {'N': str(quantity)},
                'Price': {'N': str(price)}
            },
            ConditionExpression="attribute_not_exists(orderId)"
        )
    except Exception as e:
        logger.error(f"Error saving order to DynamoDB: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error')
        }
    finally:
      # End time for the duration metric
      end_time = time.time()
      duration = (end_time - start_time) * 1000

    metrics.add_metric(name=custom_metric_invocations_name, unit=MetricUnit.Count, value=1, resolution=MetricResolution.High)
    metrics.add_metric(name=custom_metric_duration_name, unit=MetricUnit.Milliseconds, value=duration, resolution=MetricResolution.High)

    return {
        'statusCode': 200,
        'body': json.dumps('Order created successfully')
    }
