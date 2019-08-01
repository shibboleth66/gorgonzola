# Boto Session

## **class** BotoSession

Object representing an authenticated Boto3 session.

Session can be created in any account/subscription indicated by RoleArn.

Caller must have permission to assume the specified Role.


### Request Syntax

```python
boto_session = gorgonzola.BotoSession(
    RoleArn='string'
    ServiceName='string',
    ServiceInterface='client'|'resource',
    RegionName='string',
    Duration='integer'
)
```

### Parameters

* **RoleArn** (string) -- [REQUIRED]

    ARN of IAM Role to be assumed during session creation.

* **ServiceName** (string) -- [REQUIRED]

    Lowercase name of AWS service to use.

* **ServiceInterface** (string)

    Boto3 interface type. Can be *client* or *resource*
    
    Defaults to *client*

* **RegionName** (string)

    Lowercase id of AWS region.

    Defaults to *eu-west-2* (London)

* **Duration** (integer)

    Length (in seconds) of session duration.

    Defaults to *900*

### Return Type

**object**