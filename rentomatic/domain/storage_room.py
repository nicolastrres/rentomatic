from rentomatic.shared.domain_model import DomainModel


class StorageRoom:
    def __init__(self, code, size, price, longitude, latitude):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude


DomainModel.register(StorageRoom)
