import sys
sys.path.insert(0, '../gorgonzola')
import gorgonzola

account = '124387271761'
role = 'OrganizationAccountAccessRole'
arn = "{}:{}:{}/{}".format(
        'arn:aws:iam:', account, 'role', role
    )

payload = {
    "Surname": 'Bond',
    "Givenname": 'James'
}

func = gorgonzola.LambdaFunction(
    RoleArn=arn,
    FunctionName='testicles',
    Event=payload
)

print(func.get_response())
