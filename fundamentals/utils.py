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

    # def nested_get(self, item):
    #     items = item.split('__')
    #
    #     if len(items) > 1:
    #         cur_dict = self
    #         for it in items:
    #             cur_dict = dict.__getitem__(cur_dict, it)
    #         return cur_dict
    #     else:
    #         return nested_get(self, item)


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


def nested_get(a_dict, item):
    for key in a_dict:
        print(key, a_dict)
        print('-')
        ret = dict.__getitem__(a_dict, key)
        if key == item:
            return ret
        elif isinstance(ret, dict):
            try:
                return nested_get(ret, item)
            except KeyError:
                pass
        else:
            continue
        raise KeyError('{} not found'.format(item))


if __name__ == "__main__":
    d = {
        "a": {
            "b": {
                "k": None
            },
            "k": None
        }
    }

    ret = nested_get(d, 'b')
    print(ret)