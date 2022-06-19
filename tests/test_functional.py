import pytest
from src.models import PeopleModel, PlanetModal, StarshipModel
from utils import validate_json
import requests
from config import API_URL


class TestPeople:

    @pytest.mark.parametrize('people_id', [0, 1, 12, 98, 99])
    def test_get_people(self, run_server_for_session, people_id: int) -> None:
        """
        Execute query to /people/id. ID are taken from params
        Check status code and validate response data
        :param run_server_for_session: fixture with prepare server
        :param people_id: int, take from parameters
        :return: None
        """
        response = requests.get(f"{API_URL}/people/{people_id}")
        assert response.status_code == 200
        assert validate_json(response.json(), PeopleModel)

    @pytest.mark.parametrize('people_id', [-1, 100, 101])
    def test_people_invalid_ids(self, run_server_for_session, people_id: int) -> None:
        """
        Execute query to /people/id. ID are taken from params
        Tests for properly type, but with invalid range
        Check status code and error message
        :param run_server_for_session: fixture with prepare server
        :param people_id: int, take from parameters
        :return: None
        """
        response = requests.get(f"{API_URL}/people/{people_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Wrong id number. Please use id from 0 to 99"}

    @pytest.mark.parametrize('people_id', [0.5, '2h'])
    def test_people_invalid_type_ids(self, run_server_for_session, people_id) -> None:
        """
        Execute query to /people/id. IDs are taken from params
        Tests for invalid type. Check error message
        :param run_server_for_session: fixture with prepare server
        :param people_id: int, take from parameters
        :return: None
        """
        response = requests.get(f"{API_URL}/people/{people_id}")
        assert response.json()['detail'][0]['msg'] == "value is not a valid integer"


class TestPlanets:

    @pytest.mark.parametrize('planet_id', [0, 1, 23, 99])
    def test_get_planet(self, run_server_for_session, planet_id: int) -> None:
        """
        Execute query to /planets/id. ID are taken from params
        Check status code and validate response data
        :param run_server_for_session: fixture with prepare server
        :param planet_id: int, take from parameters
        :return: None
        """
        response = requests.get(f"{API_URL}/planets/{planet_id}")
        assert response.status_code == 200
        assert validate_json(response.json(), PlanetModal)

    @pytest.mark.parametrize('planet_id', [-1, 100, 101])
    def test_planet_invalid_ids(self, run_server_for_session, planet_id: int) -> None:
        """
        Execute query to /planets/id. ID are taken from params
        Tests for properly type, but with invalid range
        Check status code and error message
        :param run_server_for_session: fixture with prepare server
        :param planet_id: int, take from parameters
        :return: None
        """
        response = requests.get(f"{API_URL}/planets/{planet_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Wrong id number. Please use id from 0 to 99"}

    @pytest.mark.parametrize('planet_id', [0.5, 'h4'])
    def test_planet_invalid_type_ids(self, run_server_for_session, planet_id) -> None:
        """
        Execute query to /planets/id. IDs are taken from params
        Tests for invalid type. Check error message
        :param run_server_for_session: fixture with prepare server
        :param planet_id: int, take from parameters
        :return: None
        """
        response = requests.get(f"{API_URL}/planets/{planet_id}")
        assert response.json()['detail'][0]['msg'] == "value is not a valid integer"


class TestStarships:

    @pytest.mark.parametrize('starship_id', [0, 1, 23, 99])
    def test_get_starship(self, run_server_for_session, starship_id: int) -> None:
        """
        Execute query to /starships/id. ID are taken from params
        Check status code and validate response data
        :param run_server_for_session: fixture with prepare server
        :param starship_id: int, take from parameters
        :return: None
        """
        response = requests.get(f"{API_URL}/starships/{starship_id}")
        assert response.status_code == 200
        assert validate_json(response.json(), StarshipModel)

    @pytest.mark.parametrize('starship_id', [-1, 100, 101])
    def test_starship_invalid_ids(self, run_server_for_session, starship_id: int) -> None:
        """
        Execute query to /starships/id. ID are taken from params
        Tests for properly type, but with invalid range
        Check status code and error message
        :param run_server_for_session: fixture with prepare server
        :param starship_id: int, take from parameters
        :return: None
        """
        response = requests.get(f"{API_URL}/starships/{starship_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Wrong id number. Please use id from 0 to 99"}

    @pytest.mark.parametrize('starship_id', [0.5, 'l3'])
    def test_starships_invalid_type_ids(self, run_server_for_session, starship_id) -> None:
        """
        Execute query to /planets/id. IDs are taken from params
        Tests for invalid type. Check error message
        :param run_server_for_session: fixture with prepare server
        :param starship_id: int, take from parameters
        :return: None
        """
        response = requests.get(f"{API_URL}/starships/{starship_id}")
        assert response.json()['detail'][0]['msg'] == "value is not a valid integer"
