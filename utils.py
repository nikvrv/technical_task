from json import loads
from logging import getLogger
from pathlib import Path
from typing import Dict

from pydantic import ValidationError

log = getLogger(__name__)


async def get_project_root() -> Path:
    """
    Return path to root directory of project
    :return: Path
    """
    return Path(__file__).parent


def validate_json(source: Dict, model) -> bool:
    """
    Parse response json to model
    :param source: json object
    :param model: Model inherit to BaseModel of pydantic
    :return: True of validation success, otherwise False
    """
    try:
        model.parse_obj(source)
    except ValidationError as exc:
        log.error(f"Validation error: {exc}")
        return False
    else:
        return True


async def read_file(file_name: str) -> Dict:
    """
    Read file from data directory and parse it to dict
    :param file_name: should be with extension
    :return: Dict
    """
    project_path = await get_project_root()
    file_path = project_path.joinpath(f'data/{file_name}')
    with open(file_path, 'r') as file:
        return loads(file.read())
