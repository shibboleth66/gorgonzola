import json
from .aws_boto import Session


class Invoke(Session):
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
            Defaults to 'RequesrResponse'
    """

    #  ==========================================================
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'lambda'

        # Required Parameters.
        self.role_arn = kwargs.get('RoleArn', None)
        self.function_name = kwargs.get('FunctionName', None)

        # Optional Parameters (with defaults)
        self.region_name = kwargs.get('RegionName', 'eu-west-2')
        self.payload = kwargs.get('Payload', {})
        self.invocation_type = kwargs.get('InvocationType', 'RequestResponse')

        # Set parameters for super init.
        super_params = {
            'ServiceName': self.service_name,
            'RoleArn': self.role_arn,
            'RegionName': self.region_name
        }

        # Initialise parent object.
        super().__init__(**super_params)

        # Invoke function.
        self._create_session()
        self._invoke_function()

    #  ==========================================================
    def _create_session(self):

        # Set session parameters.
        params = {
            'ServiceName': self.service_name,
            'RoleArn': self.role_arn,
            'RegionName': self.region_name
        }

        # Create boto session
        self.boto = Session(**params)

    #  ==========================================================
    def _invoke_function(self):

        # Set invocation parameters.
        params = {
            'FunctionName': self.function_name,
            'InvocationType': self.invocation_type,
            'Payload': json.dumps(self.payload)
        }

        # Invoke lambda function.
        response = self.boto.invoke(**params)

        # Return response based on invocation type.
        if self.invocation_type == "RequestResponse":
            return json.loads(response['Payload'].read())
