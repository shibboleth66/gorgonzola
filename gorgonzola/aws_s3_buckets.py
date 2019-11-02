from .aws_boto_session import BotoSession


class S3Buckets(BotoSession):
    """List any/all S3 buckets in account.

    Generate list of buckets found in account.

    Account ID is specified in ARN of role passed as argument.

    Parameters
    ----------
    RoleArn : str
        ARN of AWS IAM Role.

    Methods
    ----------
    get_buckets(DetailLevel='low')
        Returns list of S3 Buckets

    Examples
    ----------

    # Create class object.
    s3_buckets = gorgonzola.S3Buckets(
        RoleArn=arn:aws:iam::123456789012:role/MyRole'
    )

    Return simple list of buckets.
    buckets = s3_buckets.get_buckets()

    Return detailed list of buckets.
    buckets = s3_buckets.get_buckets(
        DetailLevel='high'
    )
    """

    # ==========================================================
    # Initialize Roles object.
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 's3'
        self.role_arn = kwargs.get('RoleArn', None)
        self.info = []
        self.list = []

        # Set parameters for super init.
        super_params = {
            'ServiceName': self.service_name,
            'RoleArn': self.role_arn,
            'ServiceInterface': 'client'
        }

        # Initialise parent object.
        super().__init__(**super_params)

    # ==========================================================
    # Generate list of buckets
    def _query_s3_for_bucket_data(self):
        resp = self.boto.list_buckets()

        self.info.extend(resp['Buckets'])

        # Continue to query until no NextToken present.
        while 'NextToken' in resp:
            resp = self.boto.list_buckets(
                NextToken=resp['NextToken']
            )

            self.info.extend(resp['Buckets'])

    # ==========================================================
    # Return low detail level
    def _get_detail_low(self):
        for i in self.info:
            self.list.append(
                i.get('Name', None)
            )

        return self.list

    # ==========================================================
    # Get info
    def get_buckets(self, DetailLevel='low'):
        """Generates list of buckets

        Parameters
        ----------
        DetailLevel : str, optional
            Required detail of results (Default is 'low')
            If DetailLevel is 'high' returns list of dictionaries
        """

        # Auto-generate data.
        self._query_s3_for_bucket_data()

        # Return level of data based on arguments.
        if DetailLevel.lower() == 'high':
            return self.info
        else:
            return self._get_detail_low()
