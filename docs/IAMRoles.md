# IAM Roles

## **class** IAMRoles

Query IAM for simple Roles operations.

Caller must have permission to assume the specified Role.

## Request Syntax

```python
iam_roles = IAMRoles(
    RoleArn='string'
)
```

## Parameters

* **RoleArn** (string) -- [REQUIRED]

    ARN of IAM Role to be assumed during session creation.

### Return Type

**list**

### Methods

* [get_roles()](#-get_roles())

> ## get_roles()

## Request Syntax

```python
roles = iam_roles.get_roles(
    DetailLevel='low'|'high'
)
```

### Parameters

* **DetailLevel** (string) -- defines level of information returned

    *low* returns simple list of roles

    *high* returns list of dicts, each containing role information

### Return Type

**list**