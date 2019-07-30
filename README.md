# GORGONZOLA

AWS Boto3 helper functions.

Gorgonzola is a set of helper functions for multi-account management with an AWS Organization.

The helper functions provide a wrapper around AWS Boto3, providing simplified execution of common, multi-account API operations.

## Contents

[ Boto Session ](#-boto-session)

[ STS Credentials ](#-sts-credentials)

[ SSM Global Parameters ](#-ssm-global-parameters)

[ Lambda Functions ](#-lambda-functions)

[ Organizations ](#-organizations)

[ DynamoDB ](#-dynamodb)

[ IAM Roles ](#-iam-roles)

[ S3 Buckets ](#-s3-buckets)

## Boto Session

```python
import gorgonzola

session = gorgonzola.Session(
    'RoleArn': 'arn:aws:iam::123456789012:role/MyRole',
    'ServiceName': 'ec2',
    'ServiceInterface': 'resource'
)
```

## STS Credentials

### 
```python
import gorgonzola

sts_credentials = gorgonzola.STSCredentials(
    'RoleArn': 'arn:aws:iam::123456789012:role/MyRole',
    'Duration': 1200
)

credentials = sts_credentials.get_credentials()
```

## SSM Global Parameters

*Get list of Global Regions*
```python
import gorgonzola

ssm = gorgonzola.SSMGlobalParameters(
    'RoleArn': 'arn:aws:iam::123456789012:role/MyRole'
)

regions = ssm.get_regions(
    DetailLevel='high'
)
```

## Lambda Functions

```python
import gorgonzola

lambda_function = LambdaFunction(
    RoleArn='arn:aws:iam::123456789012:role/MyRole',
    FunctionName='WorldsBestFunction'
)

response = lambda_function.get_response()
```

## Organizations

```python
import gorgonzola

organizations = gorgonzola.Organizations(
    'RoleArn': 'arn:aws:iam::123456789012:role/MyRole'
)

accounts = organizations.get_accounts(
    DetailLevel='high'
)
```

## DynamoDB

```python
import gorgonzola

db_table = gorgonzola.DynamoDBTable(
    'RoleArn': 'arn:aws:iam::123456789012:role/MyRole',
    TableName='myTable'
)

results = db_table.query(
    key='Id',
    value='100'
)

results = db_table.scan(
    attribute='ProductType',
    value='Bicycle'
)
```

## IAM Roles

```python
import gorgonzola

iam_roles = IAMRoles(
    RoleArn='arn:aws:iam::123456789012:role/MyRole'
)

role_list = iam_roles.get_roles(
    DetailLevel='high'
)
```

## S3 Buckets

```python
import gorgonzola

s3_buckets = gorgonzola.S3Buckets(
    'RoleArn': 'arn:aws:iam::123456789012:role/MyRole'
)

buckets = s3_buckets.get_buckets(
    DetailLevel='high'
)
```