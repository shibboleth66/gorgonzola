import json
import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '124387271761'
role = 'OrganizationAccountAccessRole'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )


alias = gorgonzola.IAMAccountAlias(
    RoleArn=arn,
    Action='delete',
    Alias='banjo-development'
)

alias.execute()

print(alias.get())
