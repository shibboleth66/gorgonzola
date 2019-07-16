from .aws_boto_session import BotoSession


class Organizations(BotoSession):
    """

    """

    # ==========================================================
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'organizations'
        self.service_interface = 'client'
        self.account_info = []
        self.account_list = []

        # Required Parameters.
        self.role_arn = kwargs.get('RoleArn', None)

        # Optional Parameters (with defaults)
        self.region_name = kwargs.get('RegionName', 'eu-west-2')

        # Set parameters for super init.
        super_params = {
            'ServiceInterface': self.service_interface,
            'ServiceName': self.service_name,
            'RoleArn': self.role_arn,
            'RegionName': self.region_name
        }

        # Initialise parent object.
        super().__init__(**super_params)

    # ==========================================================
    def __get_accounts(self):

        # Query SSM for region info.
        resp = self.boto.list_accounts()

        # Add response 'Accounts' to info list.
        self.account_info.extend(resp['Accounts'])

        # Continue to query until no NextToken present.
        while 'NextToken' in resp:
            resp = self.boto.list_accounts(
                NextToken=resp['NextToken']
            )

            # Add response 'Accounts' to info list.
            self.account_info.extend(resp['Accounts'])

    # ==========================================================
    def get_account_info(self):

        # Generate list of region info.
        self.__get_accounts()

        # Return region info (list of dicts)
        return self.account_info

        # ==========================================================
    def get_account_list(self):

        # Extract account id from generated info.
        for account in self.get_account_info():
            self.account_list.append(account.get('Id', None))

        # Return account list.
        return self.account_list
