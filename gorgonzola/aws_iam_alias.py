from .aws_boto_session import BotoSession


class IAMAccountAlias(BotoSession):

    # ==========================================================
    # Initialize IAM object
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'iam'
        self.service_interface = 'client'
        self.info = []
        self.list = []

        # Required Parameters.
        self.role_arn = kwargs.get('RoleArn', None)

        # Optional Parameters.
        self.action = kwargs.get('Action', 'UNKNOWN').lower()
        self.alias = kwargs.get('Alias', 'dummy-alias')

        # Set parameters for super init.
        super_params = {
            'ServiceInterface': self.service_interface,
            'ServiceName': self.service_name,
            'RoleArn': self.role_arn
        }

        # Initialise parent object.
        super().__init__(**super_params)

    # ==========================================================
    def get(self):
        for alias in self.boto.list_account_aliases().get(
                'AccountAliases', {}):
            return alias

    # ==========================================================
    def execute(self):

        if self.action == 'create':
            self.create()

        elif self.action == 'update':
            self.update()

        elif self.action == 'delete':
            self.delete()

        else:
            print("Action is invalid: {}".format(self.action))

    # ==========================================================
    def create(self):
        return self.boto.create_account_alias(
            AccountAlias=self.alias
        )

    # ==========================================================
    def delete(self):
        return self.boto.delete_account_alias(
            AccountAlias=self.alias
        )

    # ==========================================================
    def update(self):
        self.delete()
        self.create()
