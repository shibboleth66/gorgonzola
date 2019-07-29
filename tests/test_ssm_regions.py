import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '124387271761'
role = 'OrganizationAccountAccessRole'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )

regions = gorgonzola.Regions()

for detail_level in ['low', 'high']:

    print(regions.get_info(
        DetailLevel=detail_level
    ))
