# Django REST Envelop

Turn the ViewSet list endpoints to return an object rather than a list directly.

## Installation

From PYPi using `pip`:

```
pip install django-rest-envelope
```

## Usage

In your viewset views, you can use the `ListEnvelopeMixin` along with another mixin that defines the `list()` method:

```python
class MyViewSet(ListEnvelopeMixin, ReadOnlyModelViewSet):
    envelope: "my_envelope"
```

In your ViewSet class that uses the mixin you have to define the `envelope` attribute.

Additionally, you can overwrite the `get_envelope()` method to tweak the behaviour of
which envelope use in different situations.

## Licence

This package is distributed under [MIT Licence](./LICENCE).
