from .aws_boto_session import BotoSession


class IAMRoles(BotoSession):
    """Query IAM for Role information.

    Generate list of roles found in account.

    Account ID is specified in ARN of role passed as argument.

    Parameters
    ----------
    RoleArn : str
        ARN of AWS IAM Role

    Methods
    ----------
    get_roles(DetailLevel='low')
        Returns list of IAM Roles

    Examples
    ----------

    # Invoke specified function
    iam_roles = IAMRoles(
        RoleArn='arn:aws:iam::123456789012:role/MyRole'
    )

    # Capture results.
    role_list = iam_roles.get_roles(
        DetailLevel='high'
    )
    """

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
    def _get_detail_low(self):

        for i in self.info:
            self.list.append(
                i.get('RoleName', None)
            )

        return self.list

    # ==========================================================
    # Get roles
    def get_roles(self, DetailLevel='low'):
        """Generates list of IAM Roles

        Parameters
        ----------
        DetailLevel : str, optional
            Level of detail in returned list, can be 'high' or 'low'
            Defaults to 'low'
        """

        # Auto-generate data.
        self._query_iam_for_role_data()

        # Return level of data based on arguments.
        if DetailLevel.lower() == 'high':
            return self.info
        else:
            return self._get_detail_low()
