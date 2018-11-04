from fundamentals.widgets import BaseWidget
from control import ControlAbility

import uuid


# Format
class LayoutSkeleton(object):
    def get_skeleton(self):
        return {
            'attributes': None,
            'attributes__foldable_vector': None,
            'attributes__folding_states': None,
            'name': self.__class__.__name__.lower,
        }


class GeneralLayout(BaseWidget, LayoutSkeleton):
    pass


# All Widgets
class FlowLayout(GeneralLayout):
    __fields__ = [
        'attributes__flex_direction',
        'attributes__justify_content',
        'attributes__align_items'
    ]


class BorderLayout(GeneralLayout):
    __fields__ = [
        'attributes__flex_direction',
        'attributes__justify_content',
    ]


class BoxLayout(GeneralLayout):
    __fields__ = [
        'attributes__flex_direction',
        'attributes__justify_content',
    ]


class CardLayout(GeneralLayout):
    __fields__ = [
        'attributes__index',
    ]


class PopupLayout(GeneralLayout):
    __fields__ = [
        'position',
    ]


if __name__ == '__main__':
    pass