from .utils import NestedDict

import json


class BaseWidget(NestedDict):
    def __init__(self, **kwargs):
        super(BaseWidget, self).__init__()
        self.init_from_skeleton()
        self.init_from_default()
        self.init_from_widget()
        self.init_from_kwargs(kwargs)

    def init_from_skeleton(self):
        for field in super().__skeleton__:
            self[field] = None

    def init_from_default(self):
        for field, value in super().get_defaults():
            self[field] = value() if callable(value) else value

    def init_from_widget(self):
        if hasattr(self, '__fields__'):
            for field in self.__fields__:
                self[field] = None

    def init_from_kwargs(self, kwargs):
        for field in kwargs:
            self[field] = kwargs[field]

    def dump(self):
        return json.dumps(self)