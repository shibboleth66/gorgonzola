# Lambda Functions

## **class** LambdaFunction

Automatically invokes specified Lambda Function.

Caller must have permission to assume the specified Role.

### Request Syntax

```python
lambda_function = LambdaFunction(
    RoleArn='string',
    FunctionName='string',
    RegionName='string',
    InvocationType='Event'|'RequestResponse',
    Event='dict'
)
```

### Parameters

* **RoleArn** (string) -- [REQUIRED]

    ARN of IAM Role to be assumed during session creation.

* **FunctionName** (string) -- [REQUIRED]

    Name or ARN of Lambda Function.

* **RegionName** (string)

    Lowercase id of AWS region.

    Defaults to *eu-west-2* (London)

* **InvocationType** (string)

    Type of Lambda Trigger.

    Defaults to *RequestResponse*.

* **Event** (dict)

    JSON event parameters (payload).

    Defaults to *{}*.

### Return Type

**object**

### Methods

* [get_response()](#-get_response())

> ## get_response()

### Request Syntax

```python
response = lambda_function.get_response()
```

**Note:** If *InvocationType* is *Event*, response object contains RequestId and StatusCode

### Return Type

**dict**
