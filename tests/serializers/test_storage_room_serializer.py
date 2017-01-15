import json

from hamcrest import assert_that, equal_to

from rentomatic.domain.storage_room import StorageRoom
from rentomatic.serializers.storage_room_serializer import StorageRoomEncoder


def test_serialize_domain_storageroom():
    room = StorageRoom('f853578c-fc0f-4e65-81b8-566c5dffa35a',
                       size=100,
                       price=19,
                       longitude=-0.0123123,
                       latitude=40.23422)
    expected_json = """
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "size": 100,
            "price": 19,
            "longitude": -0.0123123,
            "latitude": 40.23422
        }
    """

    assert_that(json.loads(json.dumps(room, cls=StorageRoomEncoder)), equal_to(json.loads(expected_json)))
