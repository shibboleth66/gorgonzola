import boto3
from .aws_sts import Credentials


class Session():
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

    #  ==========================================================
    def __init__(self, **kwargs):

        # Required Parameters
        self.role_arn = kwargs.get('RoleArn', None)
        self.service_name = kwargs.get('ServiceName', None)

        # Optional Parameters (with defaults)
        self.region_name = kwargs.get('RegionName', 'eu-west-2')
        self.type = kwargs.get('ServiceInterface', 'client')
        self.duration = kwargs.get('Duration', 900)

        # Begin params doctionary.
        self.params = {
            "region_name": self.region_name
        }

        # Make boto session.
        self._generate_credentials()
        self._create_session()

    #  ==========================================================
    def _create_session(self):

        # Create sessions object.
        self.session = boto3.session.Session(**self.params)

        # Create default 'resource' object.
        self.boto = self.session.resource(self.service_name)

        # Create 'client' object of requried.
        if self.type.lower() is 'client':
            self.boto = self.boto.meta.client

    #  ==========================================================
    def _generate_credentials(self):

        # Set parameters for credential generation.
        params = {
            "RoleArn": self.role_arn,
            "Duration": self.duration
        }

        # Generate STS credentials.
        creds = Credentials(**params).get()

        # Update object parameters with credentials.
        self.params.update(**creds)

    #  ==========================================================
    def __str__(self):
        return "Boto Session for: {}/{}/{}/{}".format(
            self.type, self.service_name, self.region_name, self.role_arn
        )
