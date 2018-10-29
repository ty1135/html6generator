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