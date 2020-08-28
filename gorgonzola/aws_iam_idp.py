from .aws_boto_session import BotoSession


class IAMIdentityProvider(BotoSession):

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
        self.action = kwargs.get('Action', 'UNKNOWN').lower()
        self.saml_metadata_document = kwargs.get('SAMLMetadataDocument', None)
        self.saml_provider_name = kwargs.get('SAMLProviderName', None)

        # Set parameters for super init.
        super_params = {
            'ServiceInterface': self.service_interface,
            'ServiceName': self.service_name,
            'RoleArn': self.role_arn
        }

        # Initialise parent object.
        super().__init__(**super_params)

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

        try:
            self.boto.create_saml_provider(
                SAMLMetadataDocument=self.saml_metadata_document,
                Name=self.saml_provider_name
            )
        except Exception as e:
            print("* Cannot create IDP: {}".format(
                self.saml_provider_name
            ))
            print("* {}".format(e))

    # ==========================================================
    def update(self):

        self.get_arn()

        if self.saml_provider_arn is None:

            print("* Provider does not exist, creating...")
            self.create()

        else:
            try:
                # Update SAML Provider.
                self.boto.update_saml_provider(
                    SAMLMetadataDocument=self.saml_metadata_document,
                    SAMLProviderArn=self.saml_provider_arn
                )
            except Exception as e:
                print("* Error Updating SAML provider {}:".format(
                    self.saml_provider_name
                ))
                print("* {}".format(e))

    # ==========================================================
    def delete(self):

        self.get_arn()

        try:
            # Delete SAML provider
            self.boto.delete_saml_provider(
                SAMLProviderArn=self.saml_provider_arn
            )
        except Exception as e:
            print("* Error Deleting SAML provider {}:".format(
                self.saml_provider_name
            ))
            print("* {}".format(e))

    # ==========================================================
    def get_arn(self):

        try:
            # Retrieve list of SAML providers.
            response = self.boto.list_saml_providers()
        except Exception as e:
            print("* Cannot create list of IDPs.")
            print("* {}".format(e))
            return None

        # Process each in turn.
        for provider in response['SAMLProviderList']:

            # Extract ARN
            arn = provider['Arn']

            # Check if ARN contains required Provider Name.
            if self.saml_provider_name in arn:
                self.saml_provider_arn = arn
