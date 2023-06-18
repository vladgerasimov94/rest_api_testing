from json import dumps
from uuid import uuid4

from clients.base_client import BaseClient
from config import COVID_TRACKER_HOST
from utils.api_request import APIRequest


class CovidTrackerClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = COVID_TRACKER_HOST
        self.request = APIRequest()

    def get_latest_summary_info(self):
        response = self.request.get(f'{COVID_TRACKER_HOST}/api/v1/summary/latest')
        return response.text


covid_tracker_client = CovidTrackerClient()
