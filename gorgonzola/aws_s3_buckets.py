from .aws_boto_session import BotoSession


class Buckets(BotoSession):

    # ==========================================================
    # Initialize Roles object.
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 's3'
        self.role_arn = kwargs.get('RoleArn', None)

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
    def __query_all_buckets(self):
        self.info = []

        resp = self.boto.list_buckets()

        self.info.extend(resp['Buckets'])

        # Continue to query until no NextToken present.
        while 'NextToken' in resp:
            resp = self.boto.list_buckets(
                NextToken=resp['NextToken']
            )

            self.info.extend(resp['Buckets'])

    # ==========================================================
    # Return  info (list of dicts)
    def get_buckets(self):
        self.__query_all_buckets()

        return self.info

    # ==========================================================
    # Return  list
    def get_buckets_list(self):
        self.list = []

        for i in self.get_buckets():
            self.list.append(
                i.get('Name', None)
            )

        return self.list
