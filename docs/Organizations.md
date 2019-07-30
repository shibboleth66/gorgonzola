## Organizations

```python
import gorgonzola

organizations = gorgonzola.Organizations(
    RoleArn='arn:aws:iam::123456789012:role/MyRole'
)

accounts = organizations.get_accounts(
    DetailLevel='high'
)
```