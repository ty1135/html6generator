class NestedDict(dict):
    def __setitem__(self, key, value):
        keys = key.split('__')

        if len(keys) > 1:
            cur_dict = self
            for k in keys[:-1]:
                if k not in cur_dict or cur_dict[k] is None:
                    cur_dict[k] = {}
                cur_dict = cur_dict[k]
            cur_dict[keys[-1]] = value
        else:
            super().__setitem__(key, value)


class BaseWidget(NestedDict):
    def __init__(self, **kwargs):
        super(BaseWidget, self).__init__()
        self.init_from_skeleton()
        self.init_from_default()
        self.init_from_widget()
        self.init_from_kwargs(kwargs)

    def init_from_skeleton(self):
        for field in super().__fields__:
            self[field] = None

    def init_from_default(self):
        for field, value in self.__default__.items():
            self[field] = value() if callable(value) else value

    def init_from_widget(self):
        for field in self.__fields__:
            self[field] = None

    def init_from_kwargs(self, kwargs):
        for field in kwargs:
            self[field] = kwargs[field]





if __name__ == '__main__':
    n = NestedDict()
    n['a__b__c'] = 1
    print(n)
    n['x'] = 2
    n['x'] = 2
    print(n)