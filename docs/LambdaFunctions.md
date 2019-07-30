## Lambda Functions

```python
import gorgonzola

lambda_function = LambdaFunction(
    RoleArn='arn:aws:iam::123456789012:role/MyRole',
    FunctionName='WorldsBestFunction',
    RegionName='us-west-1'
)

response = lambda_function.get_response()
```