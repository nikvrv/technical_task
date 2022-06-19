import pytest
from src.app import app
from multiprocessing import Process
import uvicorn
from config import HOST, PORT


def run_server() -> None:
    """
    Run uvicorn server with application on define HOST and PORT
    :return:
    """
    uvicorn.run(app, host=HOST, port=PORT)


# TODO Below there are duplicates fixtures, but with different scope.
# TODO Because performance tests are failed with max sockets (65k), if run them in one session

@pytest.fixture(scope='session')
def run_server_for_session() -> None:
    """
    Fixture with pre- and post- conditions for tests
    Run server in another process and terminate it based on scope
    :return: None
    """
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start()
    yield
    proc.terminate()


@pytest.fixture(scope='function')
def run_server_for_functions() -> None:
    """
    Fixture with pre- and post- conditions for tests
    Run server in another process and terminate it based on scope
    :return: None
    """
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start()
    yield
    proc.terminate()
