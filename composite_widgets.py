from fundamentals.widgets import BaseWidget
from control import ControlAbility
from fundamentals.fields import RequiredField
import uuid


class BaseCompositeWidget(BaseWidget):
    def add_widgets(self, *widgets):
        if 'component' not in self or self['component'] is None:
            self['component'] = []
        for w in widgets:
            self['component'].append(w)


# DefaultWidget

# Format
class DefaultWidgetSkeleton(object):
    def get_skeleton(self):
        return {
            'version': 1,
            'id': lambda: str(uuid.uuid4()),
            'type': RequiredField,
            'description': None,
            'component': [],
        }


class DefaultWidget(BaseCompositeWidget, DefaultWidgetSkeleton, ControlAbility):
    pass

# CustomWidget


class CustomWidgetSkeleton(object):
    def get_skeleton(self):
        return {
            'id': lambda: str(uuid.uuid4()),
            'type': None,
            'description': None,
            'title': None,
            'layout': RequiredField,
            'component': []
        }


class CustomWidget(BaseCompositeWidget, CustomWidgetSkeleton, ControlAbility):
    pass


if __name__ == '__main__':
    import atomic_widgets

    b = atomic_widgets.Button(disable=True, icon='icon/url', label='token_label')
    c = DefaultWidget()

    c.add_widgets(b)

    c.add_method(
        name='del',
        http_method='del',
        payload=[(b['id'], b.onto('disable', 'icon', 'label'))],
        body={}
    )

    c.dump()
