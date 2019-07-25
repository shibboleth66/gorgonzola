import json
import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '124387271761'
role = 'OrganizationAccountAccessRole'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )


roles = gorgonzola.Roles(
    RoleArn=arn
)

print(json.dumps(roles.get_roles(), indent=2, default=str))
print(roles.get_roles_list())
