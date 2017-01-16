from rentomatic.shared.domain_model import DomainModel


class StorageRoom:
    def __init__(self, code, size, price, longitude, latitude):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = float(longitude)
        self.latitude = float(latitude)

    @classmethod
    def from_dict(cls, storage_room_params):
        return cls(
            code=storage_room_params.get('code'),
            size=storage_room_params.get('size'),
            price=storage_room_params.get('price'),
            longitude=float(storage_room_params.get('longitude')),
            latitude=float(storage_room_params.get('latitude'))
        )


DomainModel.register(StorageRoom)
