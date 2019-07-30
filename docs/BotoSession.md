## Boto Session

```python
import gorgonzola

boto_session = gorgonzola.Session(
    RoleArn='arn:aws:iam::123456789012:role/MyRole'
    ServiceName='ec2',
    ServiceInterface='resource'
)
```