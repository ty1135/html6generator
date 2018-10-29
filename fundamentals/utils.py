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


def nested_set(a_dict, key, value):
    for k in a_dict:
        if k == key:
            a_dict[key] = value
            return
        elif isinstance(a_dict[k], dict):
            nested_set(a_dict[k], key, value)
        else:
            continue


if __name__ == "__main__":
    d = {
        "a": {
            "b": {
                "k": 1
            },
            "k": 2
        }
    }

    nested_set(d, 'k', 'done')
    print(d)
