import os, sys
sys.path.append(os.path.dirname(os.getcwd()))
import gorgonzola

account = '124387271761'
role = 'OrganizationAccountAccessRole'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )

iam = gorgonzola.BotoSession(
    RoleArn=arn,
    ServiceName='iam'
).get()

# iam = session.boto

resp = iam.list_roles()

for role in resp['Roles']:
    print(role)
