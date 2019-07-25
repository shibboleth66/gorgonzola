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
    def __query_all_accounts(self):
        self.info = []

        resp = self.boto.list_accounts()

        self.info.extend(resp['Accounts'])

        # Continue to query until no NextToken present.
        while 'NextToken' in resp:
            resp = self.boto.list_accounts(
                NextToken=resp['NextToken']
            )

            self.info.extend(resp['Accounts'])

    # ==========================================================
    # Return account info (list of dicts)
    def get_accounts(self):
        self.__query_all_accounts()

        return self.info

    # ==========================================================
    # Return account list
    def get_accounts_list(self):
        self.list = []
        
        for i in self.get_accounts():
            self.list.append(
                i.get('Id', None)
            )

        return self.list

    # ==========================================================
    # def get_ou(self, account):

    #     resp = self.boto.list_parents(
    #         ChildId=account
    #     )

    #     if len(resp.get('Parents', [])) != 0:
    #         return resp['Parents'][0]
