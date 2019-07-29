from .aws_boto_session import BotoSession


class Roles(BotoSession):

    # ==========================================================
    # Initialize Roles object.
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'iam'
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
    # Generate list of roles
    def _query_iam_for_role_data(self):

        resp = self.boto.list_roles()

        self.info.extend(resp['Roles'])

        # Continue to query until no NextToken present.
        while 'NextToken' in resp:
            resp = self.boto.list_roles(
                NextToken=resp['NextToken']
            )

            self.info.extend(resp['Roles'])

    # ==========================================================
    # Return low detail level
    def get_detail_low(self):

        for i in self.info:
            self.list.append(
                i.get('RoleName', None)
            )

        return self.list

    # ==========================================================
    # Get info
    def get_info(self, DetailLevel='low'):

        # Auto-generate data.
        self._query_iam_for_role_data()

        # Return level of data based on arguments.
        if DetailLevel.lower() == 'high':
            return self.info
        else:
            return self.get_detail_low()
