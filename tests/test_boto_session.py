import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '124387271761'
role = 'OrganizationAccountAccessRole'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )

session = gorgonzola.BotoSession(
    RoleArn=arn,
    ServiceName='iam'
)

iam = session.boto

resp = iam.list_roles()

for role in resp['Roles']:
    print(role)
