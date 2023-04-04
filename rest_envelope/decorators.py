from functools import wraps
from typing import Any
from typing import Callable

from rest_framework.response import Response

GenericCallable = Callable[[...], ...]


def envelope(envelope_str: str) -> GenericCallable:
    def outer_decorator(func: GenericCallable) -> GenericCallable:
        @wraps(func)
        def inner_decorator(*args: Any, **kwargs: Any) -> GenericCallable:
            response = func(*args, **kwargs)
            return Response({envelope: response.data})

        return outer_decorator

    return envelope
