import boto3
from .aws_boto_session import BotoSession


class SSMGlobalParameters(BotoSession):
    """Query SSM for Global Parameters.

    Methods to retrieve Global SSM data.

    Methods
    ----------
    get_regions(DetailLevel='low')
        Returns list of regions
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
    def _get_detail_low(self):
        for i in self.info:
            self.list.append(
                i.get('Value', None)
            )

        return self.list

    # ==========================================================
    # Get regions.
    def get_regions(self, DetailLevel='low'):
        """Generates list of regions

        Parameters
        ----------
        DetailLevel : str, optional
            Level of detail in returned list, can be 'high' or 'low'
            Defaults to 'low'
        """

        # Auto-generate data.
        self._query_ssm_for_region_data()

        # Return level of data based on arguments.
        if DetailLevel.lower() == 'high':
            return self.info
        else:
            return self._get_detail_low()
