import boto3
from .aws_boto_session import BotoSession


class Regions(BotoSession):
    """Query SSM Global infrastructure

    Query global ssm parameter paths for simple ilsting of services


    """

    # ==========================================================
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'ssm'
        self.path = '/aws/service/global-infrastructure/regions'
        self.info = []
        self.list = []

        # Connect to SSM
        self.boto = boto3.client('ssm')

        # Auto-generate data.
        self._query_ssm_for_region_data()

    # ==========================================================
    def _query_ssm_for_region_data(self):

        # Query SSM for region info.
        resp = self.boto.get_parameters_by_path(
            Path=self.path
        )

        # Add response 'Parameters' to info list.
        self.info.extend(resp['Parameters'])

        # Continue to query until no NextToken present.
        while 'NextToken' in resp:
            resp = self.boto.get_parameters_by_path(
                Path=self.path,
                NextToken=resp['NextToken']
            )

            # Add response 'Parameters' to info list.
            self.info.extend(resp['Parameters'])

    # ==========================================================
    # Return low detail level
    def get_detail_low(self):
        for i in self.info:
            self.list.append(
                i.get('Value', None)
            )

        return self.list

    # ==========================================================
    # Get info.
    def get_info(self, DetailLevel='low'):

        # Auto-generate data.
        self._query_ssm_for_region_data()

        # Return level of data based on arguments.
        if DetailLevel.lower() == 'high':
            return self.info
        else:
            return self.get_detail_low()
