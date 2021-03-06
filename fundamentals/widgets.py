from .utils import NestedDict, nested_set, nested_del

import json


class BaseWidget(NestedDict):
    def __init__(self, **kwargs):
        super(BaseWidget, self).__init__()
        self.init_from_skeleton()
        self.init_from_widget()
        self.init_from_kwargs(kwargs)
        nested_del(self)

    def init_from_skeleton(self):
        for field, value in super().get_skeleton().items():
            self[field] = value() if callable(value) else value

    def init_from_widget(self):
        if hasattr(self, '__fields__'):
            for field in self.__fields__:
                self[field] = None

    def init_from_kwargs(self, kwargs):
        for field in kwargs:
            if '__' in field:
                self[field] = kwargs[field]
            else:
                nested_set(self, field, kwargs[field])

    def onto(self, *args):
        ret = {}
        for arg in args:
            ret[arg] = self.nested_get(arg)
        return ret

    def dump(self):
        ret = json.dumps(self)
        print(ret)
        return ret