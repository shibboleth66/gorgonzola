from .aws_boto_session import BotoSession


class Organizations(BotoSession):
    """List AWS Organizations Accounts

    Generate full list of Accunts present within an AWS Organization.

    **kwargs:
        RoleArn (string, required): ARN of AWS IAM Role
            Formatted ARN of IAM Role.

    Examples:
        orgs = gorgonzola.Organizations(
            'RoleArn': 'arn:aws:iam::123456789012:role/OrganizationAccountAccessRole'
        )

        Return list of dictionaries, each containing Account Information.
        orgs.get_accounts()

        Return list of Account IDs.
        orgs.get_accounts_list()
    """

    # ==========================================================
    # Initialize Organizations object
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'organizations'
        self.service_interface = 'client'
        self.info = []
        self.list = []

        # Required Parameters.
        self.role_arn = kwargs.get('RoleArn', None)

        # Set parameters for super init.
        super_params = {
            'ServiceInterface': self.service_interface,
            'ServiceName': self.service_name,
            'RoleArn': self.role_arn
        }

        # Initialise parent object.
        super().__init__(**super_params)

    # ==========================================================
    # Generate list of ALL accounts
    def _query_organizations_for_account_data(self):
        resp = self.boto.list_accounts()

        self.info.extend(resp['Accounts'])

        # Continue to query until no NextToken present.
        while 'NextToken' in resp:
            resp = self.boto.list_accounts(
                NextToken=resp['NextToken']
            )

            self.info.extend(resp['Accounts'])

    # ==========================================================
    # Return low detail level
    def get_detail_low(self):
        for i in self.info:
            self.list.append(
                i.get('Id', None)
            )

        return self.list

    # ==========================================================
    # Get info.
    def get_info(self, DetailLevel='low'):

        # Auto-generate data.
        self._query_organizations_for_account_data()

        # Return level of data based on arguments.
        if DetailLevel.lower() == 'high':
            return self.info
        else:
            return self.get_detail_low()

    # ==========================================================
    # def get_ou(self, account):

    #     resp = self.boto.list_parents(
    #         ChildId=account
    #     )

    #     if len(resp.get('Parents', [])) != 0:
    #         return resp['Parents'][0]
