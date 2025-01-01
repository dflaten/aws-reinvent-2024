output "api_endpoint" {
  value = "${aws_apigatewayv2_api.lambda.api_endpoint}/test"
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "subnet_ids" {
  value = aws_subnet.public[*].id
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.k6.name
}

output "ecs_task_definition_arn" {
  value = aws_ecs_task_definition.k6.arn
}
