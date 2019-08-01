# STS Credentials

## **class** STSCredentials

Uses Boto3 `sts` service to assume specified role and return temporay credentials.

### Request Syntax

```python
sts_credentials = gorgonzola.STSCredentials(
    RoleArn='string'
    Duration='integer'
)
```

### Parameters

* **RoleArn** (string) -- [REQUIRED]

    ARN of IAM Role to be assumed during session creation.

* **Duration** (integer)

    Length (in seconds) of session duration.

    Defaults to *900*

### Return Type

**object**

### Methods

* [get_credentials()](#-get_credentials())

> ## get_credentials()

### Request Syntax

```python
credentials = sts_credentials.get_credentials()
```

### Return Type

**dict**

### Response Syntax

```json
{
    'aws_access_key_id': 'string',
    'aws_secret_access_key': 'string',
    'aws_session_token': 'string'
}
```