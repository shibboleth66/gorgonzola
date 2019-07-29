from .aws_boto_session import BotoSession


class Buckets(BotoSession):

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
    def get_detail_low(self):
        for i in self.info:
            self.list.append(
                i.get('Name', None)
            )

        return self.list

    # ==========================================================
    # Get info
    def get_info(self, DetailLevel='low'):

        # Auto-generate data.
        self._query_s3_for_bucket_data()

        # Return level of data based on arguments.
        if DetailLevel.lower() == 'high':
            return self.info
        else:
            return self.get_detail_low()
