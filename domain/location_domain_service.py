from shared.location_model import LocationModel


class LocationDomainService:
    @staticmethod
    def get_location():
        return LocationModel('Rio de Janeiro', -22.9035, -43.2069)
