import boto3
from .aws_boto_session import BotoSession


class SsmGlobals(BotoSession):
    """Query SSM Global infrastructure

    Query global ssm parameter paths for simple ilsting of services


    """

    # ==========================================================
    def __init__(self, **kwargs):

        # Global Parameters.
        self.service_name = 'ssm'
        self.path = '/aws/service/global-infrastructure/regions'
        self.region_info = []
        self.region_list = []

        # Connect to SSM
        self.boto = boto3.client('ssm')

    # ==========================================================
    def __get_regions(self):

        # Query SSM for region info.
        resp = self.boto.get_parameters_by_path(
            Path=self.path
        )

        # Add response 'Parameters' to info list.
        self.region_info.extend(resp['Parameters'])

        # Continue to preform SSM query until no NextToken present.
        while 'NextToken' in resp:
            resp = self.boto.get_parameters_by_path(
                Path=self.path,
                NextToken=resp['NextToken']
            )

            # Add response 'Parameters' to info list.
            self.region_info.extend(resp['Parameters'])

    # ==========================================================
    def get_region_info(self):

        # Generate list of region info.
        self.__get_regions()

        # Return region info (list of dicts)
        return self.region_info

    # ==========================================================
    def get_region_list(self):

        # Extract region value from generated info.
        for region in self.get_region_info():
            self.region_list.append(region.get('Value', 'unknown'))

        # Return  region list.
        return self.region_list
