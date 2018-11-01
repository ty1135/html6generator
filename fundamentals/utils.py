import copy

# Nested Dictionary


class NestedDict(dict):
    def long_set(self, key, value):
        keys = key.split('__')

        cur_dict = self
        for k in keys[:-1]:
            if k not in cur_dict or cur_dict[k] is None:
                cur_dict[k] = {}
            cur_dict = cur_dict[k]
        cur_dict[keys[-1]] = value

    def long_get(self, item):
        items = item.split('__')

        cur_dict = self
        for it in items:
            cur_dict = cur_dict[it]
        return cur_dict

    def short_get(self, item):
        ret_dict = self._short_get(item)
        return ret_dict[item]

    def short_set(self, item, value):
        ret_dict = self.short_get(item)
        print(ret_dict, item, value)
        print("-"*10)
        ret_dict[item] = value

    def _short_get(self, item, found=None):
        found_is_none = found is None
        found = [] if found_is_none else found

        for key in self:
            if key == item:
                found.append(self)
            elif isinstance(self[key], dict):
                NestedDict._short_get(self[key], item, found=found)
            else:
                continue

        if found_is_none:
            if not found:
                raise KeyError('{} not found'.foramt(item))
            elif len(found) > 1:
                raise KeyError('more than two nested keys with same name "{}"'.format(item))
            else:
                return found[0]




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
                "k": 1
            },
            "k": {
                "g": 2
            }
        }
    }

    a = NestedDict({'r': 's'})

    t = NestedDict(d)
    # t.nested_set('a__b__k', '$')
    # t.nested_set('k', '$')
    # ret = t.short_get('b')
    # ret = t.long_set('k', '20')
    ret = a.short_get('r')
    print(ret)
