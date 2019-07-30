from .aws_boto_session import BotoSession
from boto3.dynamodb.conditions import Key, Attr
import json


class DynamodbTable(BotoSession):
    """Perform simple tasks on DynamoDB Table.

    Generate list of roles found in account.

    Account ID is specified in ARN of role passed as argument.

    Parameters
    ----------
    RoleArn : str
        ARN of IAM role to assume (you must have permission).
    TableName: str
        Name of DynamoDB Table
    RegionName : str, optional
        Lowercase ID of AWS region
        Defaults to 'eu-west-2'

    Methods
    ----------
    query(key=None, value=None)
        Returns single items matching primary key values.

    scan(attribute=None, value=None)
        Returns one or more items filtered by attribute and value.
        If no attribute specified, returns all items.

    put_item(item=None)
        Write dictionary of attribute/value pairs to table.
        Dictionary must include Primary Key(s).

    Examples
    ----------

    # Create class object.
    db_table = gorgonzola.DynamoDBTable(
        'RoleArn': 'arn:aws:iam::123456789012:role/MyRole',
        TableName='myTable'
    )

    Query for matcin items (based on key).
    results = db_table.query(
        key='Id',
        value='100'
    )

    Scan for matching items (based on attribute).
    results = db_table.scan(
        attribute='ProductType',
        value='Bicycle'
    )
    """

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
        self._bind_to_dynamodb_table()

    # ==========================================================
    # Bind to Dynamodb Table
    def _bind_to_dynamodb_table(self):

        try:
            self.table = self.boto.Table(self.table_name)
        except Exception as e:
            print("* Error Binding to Table: {}".format(self.table_name))
            print("* Boto Error: {}".format(e))

    # ==========================================================
    # Query Dynamodb Table
    def query(self, key=None, value=None):
        """Query DynamoDB Table

        Parameters
        ----------
        key : str
            Name of primary key
        value: str
            Value of primary key
        """

        query_params = {}

        if key is not None:
            query_params['KeyConditionExpression'] = Key(key).eq(value)

        resp = self.table.query(**query_params)

        return resp.get('Items', [])

    # ==========================================================
    # Scan Dynamodb Table
    def scan(self, attribute=None, value=None):
        """Scan DynamoDB Table

        Parameters
        ----------
        attribute : str
            Name of attribute
        value: str
            Value of attribute
        """

        scan_params = {}

        if attribute is not None:
            scan_params['FilterExpression'] = Attr(attribute).eq(value)

        resp = self.table.scan(**scan_params)

        return resp.get('Items', [])

    # ==========================================================
    # Put Item in Dynamodb Table
    def put_item(self, item=None):
        """Write entry to DynamoDB Table

        Parameters
        ----------
        item_data : str
            Dict of attribute name/value pairs.
            Ensure values are of correct type specified by DB schema.
        """

        if item is not None:

            put_params = {
                "Item": item
            }

            resp = self.table.put_item(**put_params)

            return resp
