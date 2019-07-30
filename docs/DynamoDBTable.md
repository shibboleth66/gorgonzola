## DynamoDB

```python
import gorgonzola

dynamodb_table = gorgonzola.DynamoDBTable(
    RoleArn='arn:aws:iam::123456789012:role/MyRole',
    TableName='myTable',
    RegionName='us-east-1'
)

results = dynamodb_table.query(
    key='Id',
    value='100'
)

results = dynamodb_table.scan(
    attribute='ProductType',
    value='Bicycle'
)
```