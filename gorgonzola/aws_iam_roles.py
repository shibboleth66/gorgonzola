from .aws_boto_session import BotoSession


class Roles(BotoSession):

    # ==========================================================
    # Initialize Roles object.
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'iam'
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
    # Generate list of roles
    def __query_all_roles(self):
        self.info = []

        resp = self.boto.list_roles()

        self.info.extend(resp['Roles'])

        # Continue to query until no NextToken present.
        while 'NextToken' in resp:
            resp = self.boto.list_roles(
                NextToken=resp['NextToken']
            )

            self.info.extend(resp['Roles'])

    # ==========================================================
    # Return account info (list of dicts)
    def get_roles(self):
        self.__query_all_roles()

        return self.info

    # ==========================================================
    # Return account list
    def get_roles_list(self):
        self.list = []

        for i in self.get_roles():
            self.list.append(
                i.get('RoleName', None)
            )

        return self.list
