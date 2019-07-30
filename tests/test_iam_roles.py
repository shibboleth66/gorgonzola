import json
import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '124387271761'
role = 'OrganizationAccountAccessRole'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )


roles = gorgonzola.IAMRoles(
    RoleArn=arn
)

for detail_level in ['low', 'high']:

    print(roles.get_roles(
        DetailLevel=detail_level
    ))
