# DynamoDBTable

## **class** DynamoDBTable

Perform basic functions on AWS DynamoDB Table.

Caller must have permission to assume the specified Role.

### Request Syntax

```python
dynamodb_table = gorgonzola.DynamoDBTable(
    RoleArn='string',
    TableName='string',
    RegionName='string'
)
```

### Parameters

* **RoleArn** (string) -- [REQUIRED]

    ARN of IAM Role to be assumed during session creation.

* **TableName** (string) -- [REQUIRED]

    Name of DynamoDB Table.

* **RegionName** (string)

    Lowercase id of AWS region.

    Defaults to *eu-west-2* (London)

### Return Type

**object**

### Methods

* [query()](#-query())
* [scan()](#-scan())
* [put_item()](#-put_item())

> ## query()

Query and return table items whose specified `key` name matches passed `value`. 

### Request Syntax

```python
results = dynamodb_table.query(
    key='string',
    value='string'|'integer'
)
```

### Parameters

* **key** (string) -- [REQUIRED] Name of primary key attribute

* **value** (string) -- [REQUIRED] Value of primary key attribute

### Return Type

**list**

> ## scan()

Query and return table items whose `attribute` names match passed `value`. 

### Request Syntax

```python
results = dynamodb_table.scan(
    attribute='string',
    value='string'|'integer'
)
```

### Parameters

* **attribute** (string) -- [REQUIRED] Name of table attribute

* **value** (string) -- [REQUIRED] Value of table attribute

### Return Type

**list**

> ## put_item()

Write simple JSON object to Table.

### Request Syntax

```python
data_to_write = {
    'Id': 500,
    'ProductType': 'Road Bike',
    'ProductName': 'The Sausage 9000',
    'ProductPrice': '£11.50'
}

results = dynamodb_table.put_item(
    item=data_to_write
)
```
**Note:** Data type of attribute values **must** match data schema of Table.

### Parameters

* **item** (dict) -- [REQUIRED] Dictionary of attribute/values to write

### Return Type

**dict** 
