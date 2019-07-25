import boto3
from .aws_sts_credentials import Credentials


class BotoSession():
    """Create AWS Boto Session.

    Instantiate Resource or Client session to specified IAM Role.
    Enables access to multiple AWS accounts through STS service.

    **kwargs:
        RoleArn (string, required): ARN of AWS IAM Role
            Formatted ARN of IAM Role
        ServiceName (string, required): Name of AWS Service
            Lowercase name of AWS service (as required by boto)
        ServiceInterface (string, optional): Boto interface type
            Either 'client' or 'resource' depending on requirement
            Defaults to 'client'
        RegionName (stgin, optional): AWS Region
            Lowercase ID of AWS region
            Defaults to 'eu-west-2'
        Duration (integer, optional): Session Duration
            STS session duration in seconds
            Defaults to 900

    Examples:
        gorgonzola.Session(
            'RoleArn': 'arn:aws:iam::123456789012:role/OrganizationAccountAccessRole',
            'ServiceName': 'ec2',
            'ServiceInterface': 'resource'
        )
    """

    # ==========================================================
    def __init__(self, **kwargs):

        # Required Parameters
        self.role_arn = kwargs.get('RoleArn', None)
        self.service_name = kwargs.get('ServiceName', None)

        # Optional Parameters (with defaults)
        self.region_name = kwargs.get('RegionName', 'eu-west-2')
        self.service_interface = kwargs.get('ServiceInterface', 'client')
        self.duration = kwargs.get('Duration', 900)

        # Begin params doctionary.
        self.params = {
            "region_name": self.region_name
        }

        # Make boto session.
        self.__get_creds()
        self.__get_session()

    # ==========================================================
    def __get_creds(self):

        # Set parameters for credential generation.
        params = {
            "RoleArn": self.role_arn,
            "Duration": self.duration
        }

        # Generate STS credentials.
        creds = Credentials(**params).get()

        # Update object parameters with credentials.
        self.params.update(**creds)

    # ==========================================================
    def __get_session(self):

        # Create session object.
        self.session = boto3.session.Session(**self.params)

        # Create required boto object.
        if self.service_interface.lower() == 'client':
            self.boto = self.session.client(self.service_name)

        elif self.service_interface.lower() == 'resource':
            self.boto = self.session.resource(self.service_name)

        else:
            raise Exception("Unknown Service Interface: {}".format(
                self.service_interface
            ))
