import boto3


class StsCredentials():
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
        ).get()
    """

    #  ==========================================================
    def __init__(self, **kwargs):

        # Required Parameters.
        self.role = kwargs.get('RoleArn', None)

        # Optional Parameters (with defaults)
        self.duration = kwargs.get('Duration', 900)

        # self._validate_id()
        # self._validate_role()

        # Generate credentials.
        # self._connect_to_sts()
        # self._assume_role()

    #  ==========================================================
    def __connect_to_sts(self):
        self.boto = boto3.client('sts')

    # #  ==========================================================
    # def _validate_id(self):
    #     if self.acc_id is None:
    #         raise Exception("Account Id missing")

    # #  ==========================================================
    # def _validate_role(self):
    #     if self.role is not None:
    #         if 'arn' not in self.role:
    #             self.role = "{}:{}:{}/{}".format(
    #                 'arn:aws:iam:', self.acc_id, 'role', self.role
    #             )
    #     else:
    #         raise Exception("IAM Role missing")

    #  ==========================================================
    def __assume_role(self):

        # Set parameters for role assumption.
        params = {
            "RoleArn": self.role,
            "RoleSessionName": 'temp-x-acc-session',
            "DurationSeconds": self.duration
        }

        # Create credentials object.
        self.creds = self.boto.assume_role(**params).get('Credentials', {})

    #  ==========================================================
    def generate(self):

        self.__connect_to_sts()
        self.__assume_role()

        return {
            'aws_access_key_id': self.creds['AccessKeyId'],
            'aws_secret_access_key': self.creds['SecretAccessKey'],
            'aws_session_token': self.creds['SessionToken']
        }
