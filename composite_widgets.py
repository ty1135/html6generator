from fundamentals.widgets import BaseWidget
import uuid


class BaseCompositeWidget(BaseWidget):
    def add_widgets(self, *widgets):
        if 'component' not in self or self['component'] is None:
            self['component'] = []
        for w in widgets:
            self['component'].append(w)


# Format
class CompositeWidgetSkeleton(object):
    __skeleton__ = [
        'version',
        'id',
        'type',
        'description',
        'component'
    ]


# Default value
class CompositeWidgetDefault(object):
    def get_defaults(self):
        return [
            ('version', 1),
            ('id', lambda: str(uuid.uuid4())),
            ('type', self.__class__.__name__.lower)
        ]


class CompositeWidget(BaseCompositeWidget, CompositeWidgetSkeleton, CompositeWidgetDefault):
    pass


if __name__ == '__main__':
    import pprint
    import atomic_widgets

    b = atomic_widgets.Button(disable=True, icon='icon/url', label='token_label')
    c = CompositeWidget(type='single-test')

    c.add_widgets(b)
    pprint.pprint(c)

    c.dump()