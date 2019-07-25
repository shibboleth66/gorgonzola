import json
import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '913100224341'
role = 'custom-admin'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )

db = gorgonzola.DynamodbTable(
    RoleArn=arn,
    TableName='ProductCatalog',
    RegionName='eu-west-1'
)

# print(json.dumps(db.scan(), indent=2, default=str))

# print(json.dumps(
#     db.scan(attribute='BicycleType', value='Road'),
#     indent=2, default=str
# ))

print(json.dumps(
    db.query(key='Id', value=201),
    indent=2, default=str
))
