from shared.model_location import ModelLocation


class LocationDomainService:
    @staticmethod
    def get_location():
        return ModelLocation('Rio de Janeiro', -22.9035, -43.2069)