from composite_widgets import DefaultWidget, CustomWidget
from atomic_widgets import (Button, CheckBox, DotCluster, Label, Pagination,
                            ProgressBar, Radio, ScrollBar, Select, TextArea,
                            TextField, TimeLine, Tree, Node)

from layouts import BoxLayout, CardLayout, PopupLayout


def div(direction, description):
    return CustomWidget(
        layout=BoxLayout(flex_direction=direction, justify_content='center'),
        description=description
)

# '整个页面' =  工具栏 + 工作台


whole_thing = div('column', '整个页面')

tools_view = div('row', '工具栏')
workbench = div('row', '工作台')


whole_thing.add_widgets(tools_view, workbench)

# 工具栏 = 数据集button + 点触button #TODO method里面要写popup

data_button = Button(icon='/url')
dot_button = Button(icon='/url')

tools_view.add_widgets(data_button, dot_button)


# 工作台 = 模型部分 + 其他部分（测试集部分 + 运行信息部分 + 编辑）

model_section = div('column', '模型部分')
other_section = div('column', '其他部分')

workbench.add_widgets(model_section, other_section)

# 其他部分 = 上面部分（测试集部分 + 运行信息部分） + 编辑器
top_section = div('row', '上面部分')
edit_section = div('column', '编辑部分')
other_section.add_widgets(top_section, edit_section)

# 上面部分 = 测试集部分 + 运行信息部分
test_section = div('column', '测试集部分')
info_section = div('column', '运行信息部分')
top_section.add_widgets(test_section, info_section)

# 模型部分 = 按钮部分 + 卡片切换部分

button_part = div('row', '模型部分——按钮部分')
model_cards = CustomWidget(layout=CardLayout(index=0), description='卡片切换部分')
model_section.add_widgets(button_part, model_cards)
# 按钮部分 = 模版按钮 + 词表按钮

template_button = Button(label='模版按钮')
words_button = Button(label='词表按钮')

button_part.add_widgets(template_button, words_button)

# 卡片切换部分 = 模版正文部分 + 词表正文部分

model_main = div('column', '模版正文部分')
words_main = div('column', '词表正文部分')

model_cards.add_widgets(model_main, words_main)

## 模版正文部分 = 搜索框部分 + 模版正文内容 + 折叠按钮
model_search_part = div('row', '搜索框部分')

model_main_content = Tree(multiple=True)
model_node_a = Node(name='搭配')
model_node_a_a = Node(name="[搭配.属性-搭配.差异比较对象-搭配.手段-搭配.属性-搭配.差异被比较对象-搭配.感观]")
model_node_a.add_children(model_node_a_a)
model_main_content.add_node(model_node_a)

model_main.add_widgets(model_search_part, model_main_content)


# 搜索框部分 = 按钮 + 搜索输入框field
model_search_button = Button(icon='/url')
model_search_input_field = TextField(editable='True', text='搭配')
model_search_part.add_widgets(model_search_button, model_search_input_field)

## 词表正文部分 = 搜索框部分 + 词表正文内容
words_search_part = div('row', '搜索框部分')

words_main.add_widgets(words_search_part, )
words_main_content = Tree(multiple=True)

word_node_a = Node(name='消息.内容')
words_main_content.add_node(word_node_a)

# 搜索框部分 = 按钮 + 搜索输入框field
words_search_button = Button(icon='/url')
words_search_input_field = TextField(editable='True', text='地点')
words_search_part.add_widgets(words_search_button, words_search_input_field)



#######################测试集部分 = 测试集标签 + 正文 + 分页 + 分析按钮
test_section_label = Label(text='测试集')
single_test = TextField(text='whatever', editable=True)
pagination = Pagination(page=1, pages=2, page_size=1)
analyze_button = Button(label='分析')

test_section.add_widgets(test_section_label, single_test, pagination, analyze_button)

#######################运行信息部分 = 运行信息标签 + 2个textfield + 正文
info_lable = Label(text='运行信息')
kv_info_a = TextField(label='相似度', text=0.71)
kv_info_b = TextField(label='通顺度', text=0.71)
info_main = TextArea(text='blah blah', label='生成信息')

info_section.add_widgets(info_lable, kv_info_a, kv_info_b, info_main)

#########################规则编辑区 = 编辑区标签+ textfield正文
edit_label = Label(text='编辑区规则')
edit_main = TextArea(text='...', editable=True)
edit_section.add_widgets(edit_label, edit_main)



##
##
##
## 数据集的交互
data_popup = CustomWidget(
        layout=PopupLayout(position='trigger_right'),
        description='数据集弹框'
)

data_popup_material = div('column', '数据集实质')

data_popup.add_widgets(data_popup_material)

data_popup_label = Label(text='数据集')
data_popup_textfield_a = TextField(text='矮胖设计图1', label='名称')
data_popup_textfield_b = TextField(text='200条', label='数据量')

data_popup_material.add_widgets(data_popup_label, data_popup_textfield_a, data_popup_textfield_b)

data_button.add_method(
    name='pop_up',
    http_method='local',
    payload=[(data_button['id'], {})],
    body=[(data_popup['id'], data_popup.onto('position', 'layout', 'component'))],
)

##
##
##
## 点触交互

dot_popup = CustomWidget(
        layout=PopupLayout(position='trigger_right'),
        description='点触'
)

dot_popup_material = div('column', '点触实质')

dot_popup.add_widgets(dot_popup_material)

dot_popup_select = Select(option=[{"text": '生产成功', "value": '生产成功'},
                                  {"text": '生产失败', "value": '生产失败'}
                                  ], choice='生产成功')
dot_popup_dot_cluster = DotCluster(row_size=5, dot=[{"text": 10, "color": "red"}, {"text": 11, "color": "red"},{"text":12, "color": "red"},{"text":13, "color": "red"},{"text":14, "color": "red"}])
dot_popup_pagination = Pagination(page=1, pages=2, page_size=5)

dot_popup_material.add_widgets(dot_popup_select, dot_popup_dot_cluster, dot_popup_pagination)

dot_button.add_method(
    name='pop_up',
    http_method='local',
    payload=[(dot_button['id'], {})],
    body=[(dot_popup['id'], dot_popup.onto('position', 'layout', 'component'))],
)


dot_popup_pagination.add_method(
    name='paging',
    http_method='put',
    payload=[(dot_popup_pagination['id'], dot_popup_pagination.onto('page', 'pages', 'page_size')),
             (dot_popup_select['id'], {"choice": '生产成功'})],
    body=[(dot_popup_dot_cluster['id'], dot_popup_dot_cluster.onto('dot', 'row_size'))],
)


## 左边折叠
workbench['layout']['attributes']['foldable_vector'] = [True, False]
workbench['layout']['attributes']['folding_states'] = [False, False]


## 右边折叠
top_section['layout']['attributes']['foldable_vector'] = [False, True]
top_section['layout']['attributes']['folding_states'] = [False, False]


## 下面折叠
other_section['layout']['attributes']['foldable_vector'] = [False, True]
other_section['layout']['attributes']['folding_states'] = [False, False]


## cardlayout的两个button
template_button.add_method(
    name='turn_over',
    http_method='local',
    payload=[(template_button['id'], {})],
    body=[(model_cards['id'], model_cards.onto('index'))],
)


dot_button.add_method(
    name='turn_over',
    http_method='local',
    payload=[(dot_button['id'], {})],
    body=[(model_cards['id'], model_cards.onto('index'))],
)

model_search_button.add_method(
    name='model_search',
    http_method='get',
    payload=[(model_search_input_field['id'], model_search_input_field.onto('text'))],
    body=[(model_main_content['id'], model_main_content)]
)

words_search_button.add_method(
    name='words_search',
    http_method='get',
    payload=[(words_search_input_field['id'], words_search_input_field.onto('text'))],
    body=[(words_main_content['id'], words_main_content)]
)

## 测试机分页
pagination.add_method(
    name='paging',
    http_method='get',
    payload=[(pagination['id'], pagination.onto('page', 'pages', 'page_size'))],
    body=[(single_test['id'], single_test)]
)

## 编辑区
edit_main.add_method(
    name='update',
    http_method='put',
    payload=[(edit_main['id'], edit_main.onto('text'))],
    body=[(edit_main['id'], edit_main.onto('text'))]
)


## 两个树的交互
new_node_payload = Node(name='内饰')
new_node_payload['relation'] = 'child'

model_main_content.add_method(
    name='create',
    http_method='post',
    payload=[
        (model_main_content['id'], new_node_payload)],
    body=[(model_main_content['id'], new_node_payload)]
)


model_main_content.add_method(
    name='update',
    http_method='put',
    payload=[
        (model_node_a['id'], model_node_a)],
    body=[(model_node_a['id'], model_node_a)]
)

model_main_content.add_method(
    name='delete',
    http_method='del',
    payload=[
        (model_node_a['id'], model_node_a)
    ],
    body=[],
)

model_main_content.add_method(
    # TODO 编辑区？ 怎么知道
    name='click',
    http_method='get',
    payload=[
        (model_node_a_a['id'], model_node_a)
    ],
    body=[
        (edit_main['id'], edit_main)
    ]
)

#######第二棵树

new_node_payload_2 = Node(name='消息.可能性')
new_node_payload_2['relation'] = 'child'

words_main_content.add_method(
    name='create',
    http_method='post',
    payload=[
        (words_main_content['id'], new_node_payload_2)],
    body=[(words_main_content['id'], new_node_payload_2)]
)


words_main_content.add_method(
    name='update',
    http_method='put',
    payload=[
        (word_node_a['id'], word_node_a)],
    body=[(word_node_a['id'], model_node_a)]
)

words_main_content.add_method(
    name='delete',
    http_method='del',
    payload=[
        (word_node_a['id'], word_node_a)
    ],
    body=[],
)

words_main_content.add_method(
    name='click',
    http_method='get',
    payload=[
        (word_node_a['id'], word_node_a)
    ],
    body=[
        (edit_main['id'], edit_main)
    ]
)

if __name__ =="__main__":
    whole_thing.dump()
    print('?')
    # tree 的交互，点击影响编辑区