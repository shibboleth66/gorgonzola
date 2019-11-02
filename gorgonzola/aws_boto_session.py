import boto3
from .aws_sts_credentials import STSCredentials


class BotoSession():
    """Create AWS Boto Session.

    Create Boto (Resource or Client) session to specified IAM Role.

    Enables access to multiple AWS accounts through STS service.

    Parameters
    ----------
    RoleArn : str
        ARN of AWS IAM Role
    ServiceName : str
        Lowercase name of AWS service (as required by boto)
    ServiceInterface : str
        Interface type, 'client' or 'resource'
        Defaults to 'client'
    RegionName : str, optional
        Lowercase ID of AWS region
        Defaults to 'eu-west-2'
    Duration : int, optional
        Session Duration in seconds
        Defaults to 900

    Examples
    ----------

    # Create session object.
    session = gorgonzola.BotoSession(
        RoleArn=arn:aws:iam::123456789012:role/MyRole',
        ServiceName='ec2',
        ServiceInterface='resource'
    )

    # Reference boto resource within session object.
    ec2 = session.boto

    # use boto commands as normal.
    response = ec2.describe_instances()
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
        self._get_creds()
        self._get_session()

    # ==========================================================
    def _get_creds(self):

        # Set parameters for credential generation.
        params = {
            "RoleArn": self.role_arn,
            "Duration": self.duration
        }

        # Generate STS credentials.
        creds = STSCredentials(**params).get_credentials()

        # Update object parameters with credentials.
        self.params.update(**creds)

    # ==========================================================
    def _get_session(self):

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
