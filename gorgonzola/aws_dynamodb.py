from .aws_boto_session import BotoSession
from boto3.dynamodb.conditions import Key, Attr


class DynamodbTable(BotoSession):

    # ==========================================================
    # Initialize Organizations object
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'dynamodb'
        self.service_interface = 'resource'

        # Required Parameters.
        self.role_arn = kwargs.get('RoleArn', None)
        self.table_name = kwargs.get('TableName', None)

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

        # Bind to Dynamodb Table
        self.__bind()

    # ==========================================================
    # Bind to Dynamodb Table
    def __bind(self):

        try:
            self.table = self.boto.Table(self.table_name)
        except Exception as e:
            print("* Error Binding to Table: {}".format(self.table_name))
            print("* Boto Error: {}".format(e))

    # ==========================================================
    # Query Dynamodb Table
    def query(self, attribute=None, value=None):

        query_params = {}

        if attribute is not None:
            query_params['KeyConditionExpression'] = Key(attribute).eq(value)

        resp = self.table.query(**query_params)

        return resp.get('Items', [])

    # ==========================================================
    # Scan Dynamodb Table
    def scan(self, key=None, value=None):

        scan_params = {}

        if key is not None:
            scan_params['FilterExpression'] = Attr(key).eq(value)

        resp = self.table.scan(**scan_params)

        return resp.get('Items', [])
