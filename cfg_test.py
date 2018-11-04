from composite_widgets import DefaultWidget, CustomWidget
from atomic_widgets import (Button, CheckBox, DotCluster, Label, Pagination,
                            ProgressBar, Radio, ScrollBar, Select, TextArea,
                            TextField, TimeLine, Tree)

from layouts import BoxLayout, CardLayout


def div(direction, description):
    return CustomWidget(
        layout=BoxLayout(flex_direction=direction, justify_content='center'),
        description=description
)

# '整个页面' =  工具栏 + 工作台


whole_thing = div('column', '整个页面')

tools_view = div('row', '工具栏')
workbench = div('row','工作台')


whole_thing.add_widgets(tools_view, workbench)

# 工具栏 = 数据集button + 点触button #TODO method里面要写popup

data_button = Button(icon='/url')
dots_button = Button(icon='/url')

tools_view.add_widgets(data_button, dots_button)


# 工作台 = 模型部分 + 其他部分（测试集部分 + 运行信息部分 + 编辑）

model_section = div('column', '模型部分')
other_section = div('column', '其他部分')

workbench.add_widgets(model_section, other_section)

# 其他部分 = 上面部分（测试集部分 + 运行信息部分） + 编辑器
top_section = div('row', '上面部分')
edit_section = div('column', '上面部分')
other_section.add_widgets(top_section, edit_section)

# 上面部分 = 测试集部分 + 运行信息部分
test_section = div('column', '测试集部分')
info_section = div('column', '运行信息部分')
top_section.add_widgets(test_section, info_section)

# 模型部分 = 按钮部分 + 卡片切换部分

button_part = div('row', '模型部分——按钮部分')
model_cards = CustomWidget(layout=CardLayout(index=0), description='卡片切换部分')

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

model_main_content = Tree() #TODO solve this tree
fold_button = Button(label='<< 折叠导航栏')
model_main.add_widgets(model_search_part, model_main_content, fold_button)


# 搜索框部分 = 按钮 + 搜索输入框field
model_search_button = Button(icon='/url')
model_search_input_field = TextField(editable='True')
model_search_part.add_widgets(model_search_button, model_search_input_field)

## 词表正文部分 = 搜索框部分 + 词表正文内容
words_search_part = div('row', '搜索框部分')

words_main.add_widgets(words_search_part, )
words_main_content = Tree() #TODO solve this tree

# 搜索框部分 = 按钮 + 搜索输入框field
words_search_button = Button(icon='/url')
words_search_input_field = TextField(editable='True')
words_search_part.add_widgets(words_search_button, model_search_input_field)



#######################测试集部分 = 测试集标签 + 正文 + 分页 + 分析按钮
test_section_label = Label(text='测试集')
single_test = TextField(text='whatever', editable=True)
pagination = Pagination(page=1, pages=2)
analyze_button = Button(label='分析')

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



if __name__ =="__main__":
    whole_thing.dump()
    # 交互和隐藏还没做还有popup