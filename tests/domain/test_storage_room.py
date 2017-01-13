import uuid

from hamcrest import assert_that, equal_to

from rentomatic.domain.storage_room import StorageRoom


def test_storageroom_model_init():
    code = uuid.uuid4()
    storage_room = StorageRoom(
        code,
        size=200,
        price=10,
        longitude=-0.08392555,
        latitude=34.75637280
    )
    assert_that(storage_room.code, equal_to(code))
    assert_that(storage_room.size, equal_to(200))
    assert_that(storage_room.price, equal_to(10))
    assert_that(storage_room.longitude, equal_to(-0.08392555))
    assert_that(storage_room.latitude, equal_to(34.75637280))


def test_storage_room_model_from_dict():
    code = uuid.uuid4()
    storage_room = StorageRoom.from_dict(
        storage_room_params={
            'code': code,
            'size': 200,
            'price': 10,
            'longitude': -0.08392555,
            'latitude': 34.75637280
        }
    )
    assert_that(storage_room.code, equal_to(code))
    assert_that(storage_room.size, equal_to(200))
    assert_that(storage_room.price, equal_to(10))
    assert_that(storage_room.longitude, equal_to(-0.08392555))
    assert_that(storage_room.latitude, equal_to(34.75637280))
