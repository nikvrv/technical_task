from fastapi import APIRouter, HTTPException
from utils import read_file
from typing import Dict, Optional
from config import DELAY
from random import random
from asyncio import sleep
from logging import getLogger

logger = getLogger(__name__)
router = APIRouter()


async def delay() -> None:
    """
    if delay in config is true. Execute random delay
    :return: None
    """
    if DELAY:
        delay_time = random()
        logger.info(f"Delay is: {delay_time}")
        await sleep(delay_time)


async def validate_id(item_id: int) -> None:
    """
    Raise HTTP Exception if item id doesn't include in range (0-99)
    :param item_id: integer
    :return: None
    """
    if not 0 <= item_id <= 99:
        raise HTTPException(status_code=404, detail="Wrong id number. Please use id from 0 to 99")


@router.get("/people/{people_id}")
async def get_people(people_id: int) -> Optional[Dict]:
    """
    Send mock data based on people id
    Validate people id. Next, read json file with mock answer and add it to response
    :param people_id: integer
    :return: Dict with mock answer, if error is not raised
    """
    await validate_id(people_id)
    response = {'id': people_id}
    people_data = await read_file("people.json")

    if people_data:
        response.update(people_data)
    await delay()
    return response


@router.get("/planets/{planet_id}")
async def get_planet(planet_id: int) -> Optional[Dict]:
    """
    Send mock data based on planet id
    Validate planet id. Next, read json file with mock answer and add it to response
    :param planet_id: integer
    :return: Dict with mock answer, if error is not raised
    """
    await validate_id(planet_id)
    response = {'id': planet_id}
    planet_data = await read_file("planet.json")

    if planet_data:
        response.update(planet_data)
    await delay()
    return response


@router.get("/starships/{starship_id}")
async def get_starship(starship_id: int) -> Optional[Dict]:
    """
    Send mock data based on starship id
    Validate starship id. Next, read json file with mock answer and add it to response
    :param starship_id: integer
    :return: Dict with mock answer, if error is not raised
    """
    await validate_id(starship_id)
    response = {'id': starship_id}
    starship_data = await read_file("starship.json")

    if starship_data:
        response.update(starship_data)
    await delay()
    return response
