## S3 Buckets

```python
import gorgonzola

s3_buckets = gorgonzola.S3Buckets(
    RoleArn='arn:aws:iam::123456789012:role/MyRole'
)

buckets = s3_buckets.get_buckets(
    DetailLevel='high'
)
```