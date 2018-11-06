from fundamentals.widgets import BaseWidget
from control import ControlAbility

import uuid
import random

# Format
class WidgetSkeleton(object):
    def get_skeleton(self):
        return {
            'version': 1,
            'id': lambda: str(uuid.uuid4()),
            'view__type': self.__class__.__name__.lower,
            'view__description': None,
            'view__props': None,
            'model': None
        }


class GeneralWidget(BaseWidget, WidgetSkeleton, ControlAbility):
    pass


# All Widgets
class Button(GeneralWidget):
    __fields__ = [
        'model__disable',
        'view__props__icon',
        'view__props__label'
    ]


class CheckBox(GeneralWidget):
    __fields__ = [
        'view__props__options',
        'view__props__label',
        'model__checked'
    ]


class DotCluster(GeneralWidget):
    __fields__ = [
        'view__props__row_size',
        'model__dot'
    ]


class Label(GeneralWidget):
    __fields__ = [
        'view__props__icon',
        'view__props__text'
    ]


class Pagination(GeneralWidget):
    __fields__ = [
        'model__page',
        'model__pages',
        'model__page_size',
    ]


class ProgressBar(GeneralWidget):
    __fields__ = [
        'model__percent'
    ]


class Radio(GeneralWidget):
    __fields__ = [
        'view__props__options',
        'model__checked'
    ]


class ScrollBar(GeneralWidget):
    __fields__ = [
        'view__props__label',
        'view__props__min',
        'view__props__max',
        'view__props__extent',
        'model__value'
    ]


class Select(GeneralWidget):
    __fields__ = [
        'view__props__label',
        'view__props__option',
        'model__choice'
    ]


class TextArea(GeneralWidget):
    __fields__ = [
        'view__props__label',
        'view__props__palceholder',
        'model__editable',
        'model__text'
    ]


class TextField(GeneralWidget):
    __fields__ = [
        'view__props__label',
        'view__props__palceholder',
        'model__editable',
        'model__text'
    ]


class TimeLine(GeneralWidget):
    __fields__ = [
        'model__content'
    ]


class Tree(GeneralWidget):
    __fields__ = [
        'view__props__multiple',
        'model__title',
        'node',
    ]

    def __init__(self, *args, **kwargs):
        if 'node' not in kwargs:
            kwargs['node'] = []
            super().__init__(*args, **kwargs)

    def add_node(self, *node_dicts):
        node_list = self.short_get('node')
        for node in node_dicts:
            node_list.append(node)


class Node(dict):
    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid.uuid4())
        if 'action' not in kwargs:
            kwargs['action'] = ["create", "update", "delete"]
        if 'children' not in kwargs:
            kwargs['children'] = []
        if 'name' not in kwargs:
            raise Exception('Every node needs a name')
        super().__init__(**kwargs)

    def add_children(self, *sub_nodes):
        for sub in sub_nodes:
            self['children'].append(sub)


class TreeSelect(GeneralWidget):
    __fields__ = [
        'view__props__label',
        'view__props__editable',
        'tree_direction',
        'option_tree',
        'model__value'
    ]

    def __init__(self, *args, **kwargs):
        if 'option_tree' not in kwargs:
            kwargs['option_tree'] = []
        super().__init__(*args, **kwargs)

    def add_node(self, *node_dicts):
        node_list = self.short_get('option_tree')
        for node in node_dicts:
            node_list.append(node)


class TreeSelectNode(dict):
    def __init__(self, **kwargs):
        if 'text' not in kwargs:
            raise Exception('text needed when initializing TreeSelectNode')
        if 'subtree' not in kwargs:
            kwargs['subtree'] = []
        if 'value' not in kwargs:
            kwargs['value'] = random.randint(0, 100)
        super().__init__(**kwargs)

    def add_children(self, *sub_nodes):
        for sub in sub_nodes:
            self['subtree'].append(sub)


class EditableSelect(GeneralWidget):
    __fields__ = [
        'view__props__label',
        'view__props__option',
        'tree_direction',
        'model__value'
    ]


if __name__ == '__main__':
    t = TreeSelect()
    n1 = TreeSelectNode(name='哈哈')
    n2 = TreeSelectNode(name='哈哈2')
    t.add_node(n1)
    n1.add_children(n2)
    print(t)