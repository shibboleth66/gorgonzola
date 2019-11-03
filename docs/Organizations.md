# Organizations

## **class** Organizations

Query AWS ORganizations API to return details of organizational accounts/subscriptions.

Caller must have permission to assume the specified Role.

### Request Syntax

```python
import gorgonzola

organizations = gorgonzola.Organizations(
    RoleArn='string'
)
```

### Parameters

* **RoleArn** (string) -- [REQUIRED]

    ARN of IAM Role to be assumed during session creation.

### Return Type

**object**

### Methods

* [get_accounts()](#-get_accounts())

> ## get_accounts()

### Request Syntax

```python
accounts = organizations.get_accounts(
    DetailLevel="low"|"high"
)
```

### Parameters

* DetailLevel (string) -- defines level of information returned

    *low* returns simple list of account ids

    *high* returns list of dicts, each containing account information

### Return Type

**list**

### Response Syntax (*low*)

```json
[
    "0123456789012"
]
```

### Response Syntax (*high*)
```json
[
    {
        "Id": "string",
        "Arn": "string",
        "Email": "string",
        "Name": "string",
        "Status": "string", 
        "JoinedMethod": "string",
        "JoinedTimestamp": "datetime"
    }
]
```