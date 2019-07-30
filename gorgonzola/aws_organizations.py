from .aws_boto_session import BotoSession


class Organizations(BotoSession):
    """Simple Operations for AWS Organizations

    Return account/subscription information from Organizations.

    Account ID is specified in ARN of role passed as argument.

   Parameters
    ----------
    RoleArn :str
        ARN of AWS IAM Role.

    Methods
    ----------
    get_accounts(DetailLevel='low')

    Examples
    ----------

        # Create class object.
        orgs = gorgonzola.Organizations(
            'RoleArn': 'arn:aws:iam::123456789012:role/MyRole'
        )

        Return simple list of account Ids.
        accounts = orgs.get_accounts()

        Return detailed list of account Ids.
        accounts = orgs.get_accounts(
            DetailLevel='high'
        )
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
    def _get_detail_low(self):
        for i in self.info:
            self.list.append(
                i.get('Id', None)
            )

        return self.list

    # ==========================================================
    # Get accounts.
    def get_accounts(self, DetailLevel='low'):
        """Generate list of Organizational Accounts

        Parameters
        ----------
        DetailLevel : str, optional
            Level of detail in returned list, can be 'high' or 'low'
            Defaults to 'low'
        """

        # Auto-generate data.
        self._query_organizations_for_account_data()

        # Return level of data based on arguments.
        if DetailLevel.lower() == 'high':
            return self.info
        else:
            return self._get_detail_low()

    # ==========================================================
    # Get account.
    # def get_account(self, id=None):

    #     self.get_ou(_structure)
    #     self.get_tags()

    # ==========================================================
    # def get_ou(self, account):

    #     resp = self.boto.list_parents(
    #         ChildId=account
    #     )

    #     if len(resp.get('Parents', [])) != 0:
    #         return resp['Parents'][0]
