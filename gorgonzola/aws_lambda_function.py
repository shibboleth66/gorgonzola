import json
from .aws_boto_session import BotoSession


class LambdaFunction(BotoSession):
    """Invoke Lambda Function

    Invoke Lambda function in any account.
    Class uses existing Gonzola classes to assume passed role.

    **kwargs:
        RoleArn (string, required): ARN of IAM Role to assume.
        FunctionName (string, required): ARN or Name of Lambda function
        RegionName (string, optional): AWS Region
            Defaults to 'eu-west-2'
        Payload (dict, optional): Event payload passed to function
            Defaults to empty dict
        InvocationType (string, optional): Synchronous or Asynchronous invocation.
            Can be Event/RequestResponse/DryRun
            Defaults to 'RequestResponse'

    Examples:
        my_function = LambdaFunction(
            RoleArn='arn:aws:iam::123456789012:role/OrganizationAccountAccessRole',
            FunctionName='WorldsBestFunction'
        )

        my_function.invoke()

        results = my_function.get_response()
    """

    # ==========================================================
    # Initialize LambdaFunction object.
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'lambda'
        self.service_interface = 'client'

        # Required Parameters.
        self.role_arn = kwargs.get('RoleArn', None)
        self.function_name = kwargs.get('FunctionName', None)

        # Optional Parameters (with defaults)
        self.region_name = kwargs.get('RegionName', 'eu-west-2')
        self.payload = kwargs.get('Payload', {})
        self.invocation_type = kwargs.get('InvocationType', 'RequestResponse')

        # Set parameters for super init.
        super_params = {
            'ServiceInterface': self.service_interface,
            'ServiceName': self.service_name,
            'RoleArn': self.role_arn,
            'RegionName': self.region_name
        }

        # Initialise parent object.
        super().__init__(**super_params)

        # Automatically invoke function.
        self.invoke()

    # ==========================================================
    # Invoke function with passed parameters.
    # Response captured is based on InvocationType.
    def invoke(self):

        params = {
            'FunctionName': self.function_name,
            'InvocationType': self.invocation_type,
            'Payload': json.dumps(
                self.payload
            )
        }

        response = self.boto.invoke(**params)

        if self.invocation_type == "RequestResponse":
            self.results = json.loads(
                response['Payload'].read()
            )
        else:
            self.results = {
                'RequestId': response['ResponseMetadata']['RequestId'],
                'StatusCode': response['StatusCode']
            }

    # ==========================================================
    # Return results object.
    def get_response(self):
        return self.results
