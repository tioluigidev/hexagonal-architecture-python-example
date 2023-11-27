from domain.decision_domain_service import DecisionDomainService
from domain.location_domain_service import LocationDomainService
from shared.model_location import ModelLocation


def test_decision_ds_dont_go_outside():
    assert DecisionDomainService.get_decision(-1) == 'Don''t go outside today'


def test_decision_ds_sweater():
    assert DecisionDomainService.get_decision(10) == 'Take a sweater with you'


def test_decision_ds_nice_to_go():
    assert DecisionDomainService.get_decision(30) == 'Nice weather to go outside today'


def test_location_ds_get_location():
    location = LocationDomainService.get_location()
    assert isinstance(location, ModelLocation)
    assert location.city is not None
    assert location.latitude is not None
    assert location.longitude is not None
