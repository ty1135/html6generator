import copy

# Nested Dictionary

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


def normalize(func):
    def wrapper(a_dict, key, value):
        dict_copy = copy.deepcopy(a_dict)
        func(a_dict, key, value)
        if a_dict == dict_copy:
            a_dict[key] = value
    return wrapper


def _nested_set(a_dict, key, value):
    for k in a_dict:
        if k == key:
            a_dict[key] = value
            return
        elif isinstance(a_dict[k], dict):
            _nested_set(a_dict[k], key, value)
        else:
            continue


nested_set = normalize(_nested_set)


def nested_del(a_dict):
    to_be_del = []
    for k in a_dict:
        if a_dict[k] is None or a_dict[k] == {}:
            to_be_del.append([a_dict, k])
        elif isinstance(a_dict[k], dict):
            nested_del(a_dict[k])
        else:
            continue

    for some_dict, some_key in to_be_del:
        del some_dict[some_key]


if __name__ == "__main__":
    d = {
        "a": {
            "b": {
                "k": None
            },
            "k": None
        }
    }

    nested_del(d)
    print(d)
