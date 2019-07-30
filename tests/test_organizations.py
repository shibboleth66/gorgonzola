import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '913100224341'
role = 'custom-admin'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )

orgs = gorgonzola.Organizations(
    RoleArn=arn
)

for detail_level in ['low', 'high']:

    print(orgs.get_accounts(
        DetailLevel=detail_level
    ))
