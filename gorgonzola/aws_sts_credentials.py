import boto3
import sys


class STSCredentials():
    """Generate STS Credentials

    Generate AWS credentials by assuming passed IAM Role.
    IAM Role must exist and be correctly formatted.

    Parameters
    ----------
        RoleArn : str
            ARN of AWS IAM Role
        Duration : int, optional
            Session Duration in seconds
            Defaults to 900

    Methods
    ----------
    get_credentials()
        Returns dictionary of STS credentials.

    Examples
    ----------

    # Create credentials object.
    sts = gorgonzola.Credentials(
        'RoleArn': 'arn:aws:iam::123456789012:role/MyRole',
        'Duration': 1200
    )

    # Return credentials dictionary
    creds = sts.get_credentials()
    """

    #  ==========================================================
    def __init__(self, **kwargs):

        # Required Parameters.
        self.role = kwargs.get('RoleArn', None)

        # Optional Parameters (with defaults)
        self.duration = kwargs.get('Duration', 900)

    #  ==========================================================
    def _connect_to_sts(self):
        self.boto = boto3.client('sts')

    #  ==========================================================
    def _assume_role(self):

        # Set parameters for role assumption.
        params = {
            "RoleArn": self.role,
            "RoleSessionName": 'temp-x-acc-session',
            "DurationSeconds": self.duration
        }

        # Create credentials object.
        try:
            self.creds = self.boto.assume_role(**params).get('Credentials', {})
        except Exception as e:
            print("* Error Assuming Role: {}".format(self.role))
            print("* Boto Error: {}".format(e))
            sys.exit()

    #  ==========================================================
    # Generate credentials.
    def get_credentials(self):
        """Generate and return Credentials"""

        self._connect_to_sts()
        self._assume_role()

        return {
            'aws_access_key_id': self.creds['AccessKeyId'],
            'aws_secret_access_key': self.creds['SecretAccessKey'],
            'aws_session_token': self.creds['SessionToken']
        }
