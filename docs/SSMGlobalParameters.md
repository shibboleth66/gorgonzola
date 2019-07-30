## SSM Global Parameters

*Get list of Global Regions*
```python
import gorgonzola

ssm_parameters = gorgonzola.SSMGlobalParameters(
    RoleArn='arn:aws:iam::123456789012:role/MyRole'
)

regions = ssm_parameters.get_regions(
    DetailLevel='high'
)
```