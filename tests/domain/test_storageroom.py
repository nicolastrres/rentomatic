import uuid
from rentomatic.domain.storageroom import StorageRoom


def test_storageroom_model_init():
    code = uuid.uuid4()
    storageroom = StorageRoom(
        code,
        size=200,
        price=10,
        longitude='-0.08392555',
        latitude='34.75637280'
    )
    assert storageroom.code == code
    assert storageroom.size == 200
    assert storageroom.price == 10
    assert storageroom.longitude == '-0.08392555'
    assert storageroom.latitude == '34.75637280'
