import boto3
import sys


class Credentials():
    """Generate STS Credentials

    Assume Role using STS service to return temporary credentials.
    IAM Role must exist and be correctly formatted.

    **kwargs:
        RoleArn (string, required): ARN of AWS IAM Role
            Formatted ARN of IAM Role
        Duration (integer, optional): Session Duration
            STS session duration in seconds
            Defaults to 900

    Examples:
        creds = gorgonzola.Credentials(
            'RoleArn': 'arn:aws:iam::123456789012:role/OrganizationAccountAccessRole',
            'Duration': 1200
        )

        Return credentials dictionary
        creds.get()
    """

    #  ==========================================================
    def __init__(self, **kwargs):

        # Required Parameters.
        self.role = kwargs.get('RoleArn', None)

        # Optional Parameters (with defaults)
        self.duration = kwargs.get('Duration', 900)

    #  ==========================================================
    def __connect_to_sts(self):
        self.boto = boto3.client('sts')

    #  ==========================================================
    def __assume_role(self):

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
    def get(self):

        self.__connect_to_sts()
        self.__assume_role()

        return {
            'aws_access_key_id': self.creds['AccessKeyId'],
            'aws_secret_access_key': self.creds['SecretAccessKey'],
            'aws_session_token': self.creds['SessionToken']
        }
