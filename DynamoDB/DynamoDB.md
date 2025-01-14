# DynamoDb

[2024 DAT404: Advanced data modeling with Amazon DynamoDB - Alex DeBrie](https://www.youtube.com/watch?v=hjqrDqVaiw0)
[2023 talk on Dynamodb](https://www.youtube.com/watch?v=PVUofrFiS_A)
[2023 Deep Dive on Dynamodb](https://www.youtube.com/watch?v=ld-xoehkJuU)

[dynamodb-shell](https://github.com/awslabs/dynamodb-shell)
## Key Characteristics

- Thanks to it being hosted you don't have to worry about load blancers, storage nodes,
  etc as it is a fully managed experience.
- Consistent performance at any scale.
- Serverless-friendly (good with Lambda, how I go into Dynamodb as well)

PutItem: takes the Primary key and determines which Partition it will go to off of that.
DDB scales up the partitions as needed which is why primary key is important. You should
be referencing your partition key whenever you are accessing data in that ddb.

Partition Key - Grouped by partition key.

- Grouped by this Sort key - Orded by sort key.
- ordered by this

Items are spread across paritions by partition key.

Single -tiem actions

- basic crud, putitem, getitem, updateitem, deleteitem
- requires full primary key
- all write operations.

Query-operation (composiste primary key only)

- Fetech many
- Requires partition key; sort key is optional

Scan

- Fetch all (use sparingly)

## Secondary Index

- Copy of the data with a new primary key to make it easy to get records out efficiently.
- It is fully managed copies of your data.
- Enable additional read-based access patterns
- Two kinds:
  - Global secondary indexes (prefer)
  - Local Secondary indexes (less flexible but you get faster read-accuracy)

## What don't you need to know about DynamoDB?

- Paxos vs. Raft
- Two-phase vs. three phase commit
- Memory buffer configuration settings.

## What do you need to know?

- Partitions and importance of primary key
- API Structure
  - single-item actions vs. query vs. scan.
- Secondary Indexes
- Billing

## Data Modeling Basics

Before you design your data model, take some time to understand your domain.

- What are your constraints?
- What is your data distribution? (1:many relationship? what is the relationship and
  distributionn of your parition key?)
- How big are your items?
- Know your access patterns. Explicityly list them out with a sheet that says these are my
  read patterns, these are my write patterns.

Single Item Actions - don't query for a single item. Transactions: use them when they make
sense.

**Flexibility vs. efficiency** What is important and why are you using it?

## Tips for all modeling styles

Design for your access patterns.

- Use meaningful field for primary key
- Don't needlessly overload your item collection, if you have a lot of item types inside
  one record. If you don't have an access pattern where you are grouping things together
  that you aren't going to receive together. Only put them together if you are actually
  going to fetch them together.
- Think about your writes early.
  - Use conditional writes. You shouldn't need a back and forth when persisting an item.
- Flatten heirarchies
  - Denormalize where prudent.

## Denormalization

- Embedding
  - One-to-one
- Do not do unbounded 1 to many relations. (storing all the orders on a customer in one
  row)
- Key tradeoff: Item size vs multiple reads.
- Duplication: faster reads vs harder/ more expensive writes

## Napkin Math on Dynamodb

Napkin Math - Simon Eskildsen, SRECON, Dublin 2019

### Performance base rates

Client-side operation latency:

- GEtItem/Query: 5 ms
- put item: 20 ms
- transation: 100ms Limits:
- Query response: 1MB per request (paginated response for each query using the token) a
  5MB result will take 5 calls of 1 MB each

### Billing

- read Capaciy Unit
  - read up to 4KB of data read, cut in half if you dont need strongly consistent read
- write capcicy Unit
  - 1 KB of data written
- Prices: (on demand numbers)
  - 12.5 cents per 1 million RCUs
  - 67.5 per 1 milllion WCUs
  - \$.25 per GB-month

Performance and billing are two seperate things with Dynamodb. Pricing should affect how
you build applications.

Multiplyers for napkin math:

- Item Size \<- Larger items require more resources
- Secondary Indexes \<- More writes
- Transactions \<- coordiations
- Global Tables \<- replication costs

Mind:

- Review items sizes carefully
  - remove fields you don't need
  - don't store blobs in ddb (store them in s3)
- Limit Secondary indexes
  - Do you need a secondary index? Writes are ~20x more than reads
  - use projections to limit size of items in the index.
- Limit transactions
  - Use them for low volume high value operations
- Ensure you need global tables
- Don't use consistent reads

## DynamoDB Streams

If you have a table you can enable a stream on it. Any time a record is inserted updated,
deleted you can operate on those things with a batch of records.

### Use Cases

- Solving the dual-write problem (event driven applications). You want to do multiple
  things with it.
  - If something goes wrong while you do one but not the other what are you doing with it?
  - If event bridge is down or if something goes wrong you have a way of getting it
    retried via the stream.

### Tips

- Clean up your events before pushing elsewhere.
- Don't just grant access to the DDB stream as it only allows 2 consumers and will have
  extra data you don't need.
- Understand stream processing mechanics + failure modes.
