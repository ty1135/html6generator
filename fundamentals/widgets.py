from .utils import NestedDict, nested_del
from .fields import validate_field

import json


class BaseWidget(NestedDict):
    def __init__(self, **kwargs):
        super(BaseWidget, self).__init__()
        self.init_from_skeleton()
        self.init_from_widget()
        self.init_from_kwargs(kwargs)

        validate_field(self)
        nested_del(self)

    def init_from_skeleton(self):
        for field, value in super().get_skeleton().items():
            real_value = value() if callable(value) else value
            self.long_set(field, real_value)

    def init_from_widget(self):
        if hasattr(self, '__fields__'):
            for field in self.__fields__:
                self.long_set(field, None)

    def init_from_kwargs(self, kwargs):
        for field in kwargs:
            if '__' in field:
                self.long_set(field, kwargs[field])
            else:
                self.short_set(field, kwargs[field])

    def onto(self, *args):
        ret = {}
        for arg in args:
            ret[arg] = self.short_get(arg)
        return ret

    def dump(self):
        import subprocess

        # get string
        ret = json.dumps(self)

        # print
        print(ret)

        # write_to_clipboard
        process = subprocess.Popen(
            'pbcopy',
            env={'LANG': 'en_US.UTF-8'},
            stdin=subprocess.PIPE
        )
        process.communicate(ret.encode('utf-8'))
