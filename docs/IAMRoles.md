## IAM Roles

```python
import gorgonzola

iam_roles = IAMRoles(
    RoleArn='arn:aws:iam::123456789012:role/MyRole'
)

roles = iam_roles.get_roles(
    DetailLevel='high'
)
```