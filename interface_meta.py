"""
Define our interface metaclass here
"""
from __future__ import annotations

import inspect
import warnings
from abc import ABCMeta


def is_valid_interface_subclass(cls, subclass, attr):
    cls_attr = getattr(cls, attr, None)
    if not hasattr(subclass, attr):
        return f"Attribute {attr!r} of {cls.__name__!r} not implemented in {subclass.__name__!r}"
    subclass_attr = getattr(subclass, attr, None)
    if callable(cls_attr) == callable(subclass_attr) == False:
        return
    cls_argspec = inspect.getfullargspec(cls_attr)
    subclass_argspec = inspect.getfullargspec(subclass_attr)
    if cls_argspec != subclass_argspec:
        return (f"Signature mismatch '{cls.__name__}.{attr}' <-> '{subclass.__name__}.{attr}'."
                f"In the interface : {cls_argspec}."
                f"In concrete class: {subclass_argspec}")


def subclasshook(cls, subclass):
    cls._register_interface_subclass(subclass)
    errors = [is_valid_interface_subclass(cls, subclass, am) for am in cls.__abstractmethods__]
    if any(errors):
        raise TypeError("\n".join(str(e) for e in errors if e))
    return True


class InterfaceMeta(ABCMeta):
    def __new__(mcs, *args, **kwargs):
        i = super().__new__(mcs, *args, **kwargs)
        i._all_classes = {}
        i.__subclasshook__ = classmethod(subclasshook)
        return i

    def _register_interface_subclass(cls, subclass):
        subclass_name = subclass.__name__
        if subclass_name in cls._all_classes:
            warnings.warn(f"Already registered {subclass_name}")
        cls._all_classes[subclass_name] = subclass

    def all_classes(cls):
        return cls._all_classes

    def for_id(cls, an_id):
        return cls._all_classes.get(an_id)
