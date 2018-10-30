from composite_widgets import DefaultWidget, CustomWidget
from atomic_widgets import (Button, CheckBox, DotCluster, Label, Pagination,
                            ProgressBar, Radio, ScrollBar, Select, TextArea,
                            TextField, TimeLine, Tree)

# 整体 = 标题 + 工作台
whole = CustomWidget(layout='BoxLayout', description='整体')  # 整体

title = Label(text='汽车旅游(整体标题)')  # 标题
workbench = CustomWidget(layout='BoxLayout', description='整个工作台')  # 工作台

whole.add_widgets(title, workbench)
# ---------------------------------------------------

# 工作台 = 测试集 + 模型 + Runtime info

test_set = CustomWidget(layout='BoxLayout', description='工作台测试集部分')  # 测试集 TODO layout?
model = CustomWidget(layout='BoxLayout', description='工作台模型部分')  # 模型 TODO layout?
runtime_info = CustomWidget(layout='BoxLayout', description='工作台运行时部分')  # Runtime info TODO layout?

workbench.add_widgets(test_set, model, runtime_info)

# ------------------------------------------------------
# 测试集 = 测试集标题 + bucket页 + 分页组件

test_set_title = Label(text='ID: 1', description='测试集标签')
bucket_container = CustomWidget(layout='BoxLayout', description='bucket_container')  # TODO ! to be defined
test_set_pagination = Pagination(page=10, pages=10)

test_set.add_widgets(test_set_title, bucket_container, test_set_pagination)

# ------------------------------------------------------

# 模型 = TO BE DEFINED






# ------------------------------------------------------

# Runtime info = Tap + CardLayout

tap = CustomWidget(layout='BoxLayout', description='tap')
card_layout = CustomWidget(layout='CardLayout', description='card_layout')

runtime_info.add_widgets(tap, card_layout)


# Tap = log按钮 + 预览按钮
log_button = Button(disable=False, label='文章日志')
preview_button = Button(disable=False, label='预览')
tap.add_widgets(log_button, preview_button)

# ------------------------------------------------------

# cardlayout = log_container + preview_container

log_container = CustomWidget(layout='BoxLayout', description='log_container')
preview_container = CustomWidget(layout='BoxLayout', description='preview_container')

card_layout.add_widgets(log_container, preview_container)



if __name__ == "__main__":
    p = test_set_pagination
    log_button.add_method(
        name='test_method',
        http_method='put',
        payload=[(p['id'], p.onto('page', 'pages')), ('id1', {"some": "thing"})],
        body=[('id1', {"some": "thing"}), ('id1', {"some": "thing"})]
    )
    whole.dump()
    print('目前所有div 都是自定义 且没有type')