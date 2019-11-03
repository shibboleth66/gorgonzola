# SSM Global Parameters

## **class** SSMGlobalParameters

Queries SSM Global listings to return specified information.

### Request Syntax

```python
ssm_parameters = gorgonzola.SSMGlobalParameters(
    RoleArn='string'
)
```

### Parameters

* **RoleArn** (string) -- [REQUIRED]

    ARN of IAM Role to be assumed during session creation.

### Return Type

**object**

### Methods

* [get_regions()](#-get_regions())

> ## get_regions()

### Request Syntax

```python
regions = ssm_parameters.get_regions(
    DetailLevel='low'|'high'
)
```

### Parameters

* **DetailLevel** (string) -- defines level of information returned

### Return Type

**list**

### Response Syntax (*low*)

```json
[
    "eu-west-1"
]
```

### Response Syntax (*high*)
```json
[
    {
        "Name": "string",
        "Type": "string",
        "Value": "string",
        "Version": "integer",
        "LastModifiedDate": "datetime",
        "ARN": "string"
    }
]
```