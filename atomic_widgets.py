from fundamentals.widgets import BaseWidget
from control import ControlAbility

import uuid


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
    pass


if __name__ == '__main__':
    import pprint
    b = Button(disable=True, icon='icon/url', label='token_label')

    pprint.pprint(b)