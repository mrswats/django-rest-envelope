import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from testing.models import TestModel


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def model():
    return TestModel.objects.create(name="test-name")


@pytest.fixture
def get(model, client):
    url = reverse("test-ok-list")
    return client.get(url)


@pytest.fixture
def get_err(model, client):
    url = reverse("test-error-list")

    def _():
        return client.get(url)

    return _


@pytest.fixture
def get_with_decorator(client):
    url = reverse("test-decorator-list")
    return client.get(url)


@pytest.mark.django_db
def test_view_returns_ok_status_code(get):
    assert get.status_code == 200


@pytest.mark.django_db
def test_view_returns_object_data(get):
    assert get.json() == {"tests": [{"name": "test-name"}]}


@pytest.mark.django_db
def test_view_raises_assertion_error_if_envelope_is_not_defined(get_err):
    with pytest.raises(AssertionError) as exc:
        get_err()

    assert str(exc.value) == (
        "'TestViewSetNoEnvelope' should either include a `envelope` attribute,"
        "or override the `get_envelope()` method."
    )
