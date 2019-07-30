import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '124387271761'
role = 'OrganizationAccountAccessRole'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )

params = gorgonzola.SSMGlobalParameters()

for detail_level in ['low', 'high']:

    print(params.get_regions(
        DetailLevel=detail_level
    ))
