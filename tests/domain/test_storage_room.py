import uuid

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
    assert storage_room.code == code
    assert storage_room.size == 200
    assert storage_room.price == 10
    assert storage_room.longitude == -0.08392555
    assert storage_room.latitude == 34.75637280


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
    assert storage_room.code == code
    assert storage_room.size == 200
    assert storage_room.price == 10
    assert storage_room.longitude == -0.08392555
    assert storage_room.latitude == 34.75637280
