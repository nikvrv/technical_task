import time
from logging import getLogger
from typing import Tuple, List

import pytest
import requests

from config import API_URL

logger = getLogger(__name__)


@pytest.fixture()
def preparation_and_results() -> Tuple[float, int, List]:
    """
    Preparation to performance test and display results
    Create start time, passed time and list to time responses
    After test, count max response time, min response time and average time and display it
    :return: tuple of start time, passed time, list of response times
    """
    start_time = time.time()
    passed_time = 0
    response_time = []
    yield start_time, passed_time, response_time

    logger.info(f"Max time is: {max(response_time)}")
    logger.info(f"Min time is: {min(response_time)}")
    logger.info(f"Average time: {sum(response_time) / len(response_time)}")


class TestPerformance:
    """
    Send queries to define endpoint during 30 seconds and add elapse time to list
    Elapse time - time delta between the Request was sent and the Response was received
    Calculate max, mix and average time
    """

    def test_peoples(self, run_server_for_functions, preparation_and_results) -> None:
        """
        Test for get people endpoint
        :param run_server_for_functions: fixture to run server
        :param preparation_and_results: fixture to prepare and calculate results
        :return: None
        """
        start_time, passed_time, response_time = preparation_and_results

        while passed_time < 30:
            response = requests.get(f"{API_URL}/people/1")
            passed_time = time.time() - start_time
            response_time.append(response.elapsed.total_seconds())

    def test_planets(self, run_server_for_functions, preparation_and_results) -> None:
        """
        Test for get planets endpoint
        :param run_server_for_functions: fixture to run server
        :param preparation_and_results: fixture to prepare and calculate results
        :return: None
        """
        start_time, passed_time, response_time = preparation_and_results

        while passed_time < 30:
            response = requests.get(f"{API_URL}/planets/2")
            passed_time = time.time() - start_time
            response_time.append(response.elapsed.total_seconds())

    def test_starships(self, run_server_for_functions, preparation_and_results) -> None:
        """
        Test for get starships endpoint
        :param run_server_for_functions: fixture to run server
        :param preparation_and_results: fixture to prepare and calculate results
        :return: None
        """
        start_time, passed_time, response_time = preparation_and_results

        while passed_time < 30:
            response = requests.get(f"{API_URL}/starships/3")
            passed_time = time.time() - start_time
            response_time.append(response.elapsed.total_seconds())
