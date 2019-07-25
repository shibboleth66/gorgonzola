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

        # Autogenerate list of regions
        self.__get()

    # ==========================================================
    def __get(self):

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
    # Return region info
    def get_info(self):
        return self.info

    # ==========================================================
    # Return region list.
    def get_list(self):
        for i in self.get_info():
            self.list.append(
                i.get('Value', None)
            )

        return self.list
