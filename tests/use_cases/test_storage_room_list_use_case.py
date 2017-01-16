from unittest.mock import Mock

import pytest
from hamcrest import assert_that
from hamcrest import equal_to

from rentomatic.domain.storage_room import StorageRoom
from rentomatic.use_cases.storage_room_use_case import StorageRoomListUseCase


@pytest.fixture
def domain_storage_rooms():
    storage_room_1 = StorageRoom(
        code='f853578c-fc0f-4e65-81b8-566c5dffa35a',
        size=210,
        price=39,
        longitude=-0.09998975,
        latitude=51.75436293
    )

    storage_room_2 = StorageRoom(
        code='fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
        size=405,
        price=66,
        longitude=0.18228006,
        latitude=51.74640997,
    )

    storage_room_3 = StorageRoom(
        code='913694c6-435a-4366-ba0d-da5334a611b2',
        size=56,
        price=60,
        longitude=0.27891577,
        latitude=51.45994069,
    )

    storage_room_4 = StorageRoom(
        code='eed76e77-55c1-41ce-985d-ca49bf6c0585',
        size=93,
        price=48,
        longitude=0.33894476,
        latitude=51.39916678,
    )

    return [storage_room_1, storage_room_2, storage_room_3, storage_room_4]


def test_storageroom_list_without_parameters(domain_storage_rooms):
    repo = Mock()
    repo.list.return_value = domain_storage_rooms

    storage_room_list_use_case = StorageRoomListUseCase(repo)
    result = storage_room_list_use_case.execute()

    repo.list.assert_called_with()
    assert_that(result, equal_to(domain_storage_rooms))
