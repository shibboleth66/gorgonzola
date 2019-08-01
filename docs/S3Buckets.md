# S3 Buckets

## **class** S3Buckets

Query S3 for simepl Bucket operations.

Caller must have permission to assume the specified Role.

## Request Syntax

```python
s3_buckets = gorgonzola.S3Buckets(
    RoleArn='string'
)
```

## Parameters

* **RoleArn** (string) -- [REQUIRED]

    ARN of IAM Role to be assumed during session creation.

### Return Type

**list**

### Methods

* [get_buckets()](#-get_buckets())

> ## get_buckets()

## Request Syntax

```python
buckets = s3_buckets.get_buckets(
    DetailLevel='low'|'high'
)
```

### Parameters

* **DetailLevel** (string) -- defines level of information returned

    *low* returns simple list of buckets

    *high* returns list of dicts, each containing bucket information

### Return Type

**list**