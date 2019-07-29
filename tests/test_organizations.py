import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '913100224341'
role = 'custom-admin'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )

# org = gorgonzola.Organizations(
#     RoleArn=arn
# )

# print(org.get_accounts_list())

orgs = gorgonzola.Organizations(
    RoleArn=arn
)

for detail_level in ['low', 'high']:

    print(orgs.get_info(
        DetailLevel=detail_level
    ))
