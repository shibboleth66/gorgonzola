import json
from .aws_boto_session import BotoSession


class LambdaFunction(BotoSession):
    """Simple Invocation of AWS Lambda

    Automatically invoke function in specified account.

    Account ID is specified in ARN of role passed as argument.

    Parameters
    ----------
    RoleArn :str
        ARN of AWS IAM Role.
    FunctionName : str
        ARN or Name of Lambda function
    RegionName : str, optional
        Lowercase ID of AWS region
        Defaults to 'eu-west-2'
    Event : dict, optional
        Event payload passed to function
        Defaults to empty dict
    InvocationType : str, optional
        Function Invocation, either 'Event' or 'RequestResponse'
        Defaults to 'RequestResponse'

    Methods
    ----------
    get_response()
        Return any results as JSON.
        For 'RequestResponse', returns response from function.
        For 'Event', returns StatusCode and RequestId

    Examples
    ----------

    # Invoke specified function
    my_function = LambdaFunction(
        RoleArn='arn:aws:iam::123456789012:role/MyRole',
        FunctionName='WorldsBestFunction'
    )

    # Capture results.
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
        self.event = kwargs.get('Event', {})
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
                self.event
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
        """Return function response"""
        return self.results
