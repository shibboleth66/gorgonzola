## STS Credentials

### 
```python
import gorgonzola

sts_credentials = gorgonzola.STSCredentials(
    RoleArn='arn:aws:iam::123456789012:role/MyRole'
    Duration=1200
)

credentials = sts_credentials.get_credentials()
```