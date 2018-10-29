from fundamentals.widgets import BaseWidget
import uuid


# Format
class WidgetSkeleton(object):
    __skeleton__ = [
        'version',
        'id',
        'view__type',
        'view__description',
        'props',
        'model',
    ]


# Default value
class WidgetDefault(object):
    def get_defaults(self):
        return [
            ('version', 1),
            ('id', lambda: str(uuid.uuid4())),
            ('view__type', self.__class__.__name__.lower)
        ]


class GeneralWidget(BaseWidget, WidgetSkeleton, WidgetDefault):
    pass


# All Widgets
class Button(GeneralWidget):
    __fields__ = [
        'model__disable',
        'props__icon',
        'props__label'
    ]


class CheckBox(GeneralWidget):
    __fields__ = [
        'props__options',
        'model__checked'
    ]


class DotCluster(GeneralWidget):
    __fields__ = [
        'props__row_size',
        'model__dot'
    ]


class Label(GeneralWidget):
    __fields__ = [
        'props__icon',
        'props__text'
    ]


class Pagination(GeneralWidget):
    __fields__ = [
        'view__props',
        'model__page',
        'model__pages'
    ]


class ProgressBar(GeneralWidget):
    __fields__ = [
        'model__percent'
    ]


class Radio(GeneralWidget):
    __fields__ = [
        'props__options',
        'model__checked'
    ]


class ScrollBar(GeneralWidget):
    __fields__ = [
        'props__label',
        'props__min',
        'props__max',
        'props__extent',
        'model__value'
    ]


class Select(GeneralWidget):
    __fields__ = [
        'props__label',
        'props__option',
        'model__choice'
    ]


class TextArea(GeneralWidget):
    __fields__ = [
        'props__label',
        'props__palceholder',
        'model__editable',
        'model__text'
    ]


class TextField(GeneralWidget):
    __fields__ = [
        'props__label',
        'props__palceholder',
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
    b = Button(model__disable=True, prop__icon='icon/url', prop__label='token_label')
    pprint.pprint(b)