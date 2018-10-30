from composite_widgets import DefaultWidget, CustomWidget
from atomic_widgets import (Button, CheckBox, DotCluster, Label, Pagination,
                            ProgressBar, Radio, ScrollBar, Select, TextArea,
                            TextField, TimeLine, Tree)


# 工作台 = 测试集 + 模型 + Runtime info

test_set = CustomWidget(layout='BoxLayout', description='工作台测试集部分')
model = CustomWidget(layout='BoxLayout', description='工作台模型部分')
runtime_info = CustomWidget(layout='BoxLayout', description='工作台运行时部分')

workbench = CustomWidget(layout='BoxLayout', description='整个工作台')  # 工作台
workbench.add_widgets(test_set, model, runtime_info)

# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------

# 测试集 = 测试集标题 + bucket页 + 分页组件

test_set_title = Label(text='测试集', description='测试集标签')
bucket_container = CustomWidget(layout='BoxLayout', description='bucket_container')  # TODO ! to be defined
test_set_pagination = Pagination(page=10, pages=10)

test_set.add_widgets(test_set_title, bucket_container, test_set_pagination)


# bucket = sentence_id + sentence + 6个label(标签, 素材体积, 句子数, 总字数, 点赞数, 转发数)
bucket = DefaultWidget(type='bucket', description='单个bucket结构')

sentence_id = Label(text='1')
sentence = Label(text='对开门设计 起亚Novo概念车正式亮相_汽车之家')
tag = Label(text='标签：标题')
volume = Label(text='素材体积：')
num_sentence = Label(text='句子数：1')
num_up = Label(text='点赞数：-')
num_repost = Label(text='转发数：-')

bucket.add_widgets(sentence_id, sentence, tag, volume, num_sentence, num_up, num_repost)

# bucket_container = 一个或者多个bucket 相加
bucket_container.add_widgets(bucket)

# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------

# 模型 = 模型标题label + 排序规则容器 + 筛选内容容器 + 裁剪规则容器 + 拼接规则容器 + 分析button

model_title = Label(text='模型', description='模型')
order_rule = CustomWidget(layout='BoxLayout', description='排序规则容器')
select_rule = CustomWidget(layout='BoxLayout', description='筛选规则容器')
clip_rule = CustomWidget(layout='BoxLayout', description='裁剪规则容器')
glue_rule = CustomWidget(layout='BoxLayout', description='拼接规则容器')
analysis = Button(label='分析', disable=False)
model.add_widgets(model_title, order_rule, select_rule, clip_rule, glue_rule, analysis)


# 单条排序规则 = 条件类别Label + 标签Seclet +  权重输入(textfield) + 新增按钮 + 删除按钮

single_order_rule = DefaultWidget(type='single_order_rule', description='单条排序规则')

condition_type = Label(text='标签条件（选填）', description='条件类别')
tag_select = TextField(label='标签:', editable=True)
weight_input = TextField(label='权重：', editable=True, text='10')
order_add_button = Button(icon='url/to/symbol', disable=False)
order_del_button = Button(label='删除', disable=True)  # TODO 第一个不能删除吗


single_order_rule.add_widgets(condition_type, tag_select, weight_input, order_add_button, order_del_button)


# 排序规则容器 = 排序规则容器标题 + 一个或者多个 默认的单条排序规则
order_rule_title = Label(text='排序规则')
order_rule.add_widgets(order_rule_title, single_order_rule)


# 默认的单条筛选排序规则 = 筛选内容textField + Select筛选条件 + Textfield边界值
select_content = TextField(text='筛选内容：筛选加权分')
select_condition_select = Select(label='筛选条件',option=[{"text": '大于', "value": '大于'},
                                         {"text": '小于', "value": '小于'}], choice='小于')
border_value = TextField(label='边界值：')
single_select_rule = DefaultWidget(type='single_select_rule', description='单条筛选规则')
single_select_rule.add_widgets(select_content, select_condition_select)


# 筛选内容容器 = 筛选规则容器标题 + 一个默认的筛选排序规则
select_rule_title = Label(text='筛选规则')
select_rule.add_widgets(select_rule_title, single_select_rule)



# 裁剪规则容器 = 默认文字排版 + 默认召回图片

word_arrangment = DefaultWidget(type='word_arrangment', description='文字排版')
pic_search = DefaultWidget(type='pic_search', description='召回图片')
clip_rule.add_widgets(word_arrangment, pic_search)

# 默认召回图片 = 召回图片title + 属性label + 关系Select + 值select +
#            +  输出数量textField+位置select +label图片选择顺序 + TODO 蛇皮表格

pic_title = Label(text='召回图片')
attr_label = Label(text='属性label：')
relation_select = Select(label='关系：', option=[{"text": '等于', "value": '等于'}], choice='等于')
value_select = TextField(label='值：', editable=True)
output_num = TextField(label='输出数量', editable=True)

pos_select = Select(label='位置：', option=[{"text": '前', "value": '前'},
                                         {"text": '后', "value": '后'}], choice='后')
pic_order_label = Label(text='label图片选择顺序')

pic_search.add_widgets(pic_title, attr_label, relation_select, value_select, output_num, pos_select, pic_order_label)

# 默认文字排版 = 粒度select + 最大字数（句子数）textfield+ Label多余文字处理 +CheckBox
granularity = Select(label='粒度：', option=[
    {"text": '字数', "value": '字数'},
    {"text": '句子数', "value": '句子数'}], choice='句子数')
max_word = TextField(label='最大字数（句子数）：')
extra_word_label = Label(text='最大字数（句子数）：')
extra_word = CheckBox(options=[{"text": "分段", "value": "分段"}, {"text": "删除尾句", "value": "删除尾句"}], checked="删除尾句")

word_arrangment.add_widgets(granularity, max_word, extra_word_label, extra_word)


# 拼接规则 = 2label + 4个select + checkbox
glue_rule_title = Label(text='拼接规则')
glue_rule_spec = Label(text='素材等价段落数')
glue_pic = TextField(label='图片(单位：段)', editable=True)
glue_word = TextField(label='文字(单位：段)', editable=True)
glue_video = TextField(label='视频(单位：段)', editable=True)
glue_para_limit = TextField(label='图片(单位：段)', editable=True)
preserve_last = CheckBox(options=[{"text": "保留最后一段", "value": "保留最后一段"}], checked="保留最后一段")

glue_rule.add_widgets(glue_rule_title, glue_rule_spec, glue_pic, glue_word, glue_video, glue_para_limit, preserve_last)

# ------------------------------------------------------
# ------------------------------------------------------
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

log_container = DefaultWidget(type='log_container', description='log_container') # TODO 本来应该是custom 但是custom就没有id, 跟最后分析的method冲突
preview_container = DefaultWidget(type='preview_container', description='preview_container')

card_layout.add_widgets(log_container, preview_container)


# log_container = 几个或者多个 log_example TextField
log_example = TextField(text="""ID： 2
作为哈弗F系列诞生的第二款车型，哈弗F7以哈弗HB-02概念车为原型。车厂针对市场需求对外观、内饰和动力系统进行了相应的改进。新车采用了哈弗最新的家族化设计风格，前脸处装配面积巨大的六边形中网，搭配鹰眼状的LED大灯，显得十分动感和犀利。
内饰方面，哈弗F7采用环抱式座舱设计，装备运动感强烈的三幅式平底方向盘，同时装配了全液晶仪表盘、大尺寸的中控屏幕和电子档把。哈弗F7配备智能语音控制系统、超级智能APP、智能互娱系统，ACC自适应巡航、车道保持、自动泊车等智能科技和主动安全系统。此外，F7还将搭载“i-pilot”智能领航系统，可实现L2级自动驾驶。
""")

log_container.add_widgets(log_example)

# preview_container = 若干个textField 和 #TODO 图未定义






##########################
#########################
####Method################
#########################
#########################

# bucket = sentence_id + sentence + 6个label(标签, 素材体积, 句子数, 总字数, 点赞数, 转发数)
c_bucket = DefaultWidget(type='bucket', description='单个bucket结构')

c_sentence_id = Label(text='1')
c_sentence = Label(text='对开门设计 起亚Novo概念车正式亮相_汽车之家')
c_tag = Label(text='标签：标题')
c_volume = Label(text='素材体积：')
c_num_sentence = Label(text='句子数：1')
c_num_up = Label(text='点赞数：-')
c_num_repost = Label(text='转发数：-')

c_bucket.add_widgets(c_sentence_id, c_sentence, c_tag, c_volume, c_num_sentence, c_num_up, c_num_repost)

test_set_pagination.add_method(
    name='paging',
    http_method='put',
    payload=[(test_set_pagination['id'], {"page": 1, "pages": 2})],
    body=[(c_bucket['id'], c_bucket)],
)

########################################################################################

tag_select.add_method(
    name='update',
    http_method='put',
    payload=[(tag_select['id'], {"text": "外观"})],
    body=[(tag_select['id'], {"text": "外观"})],     # TODO 确认以前返回和请求一样？
)

########################################################################################

weight_input.add_method(
    name='update',
    http_method='put',
    payload=[(weight_input['id'], {"text": "10"})],
    body=[(weight_input['id'], {"text": "10"})],     # TODO 确认以前返回和请求一样？
)

########################################################################################

select_condition_select.add_method(
    name='update',
    http_method='put',
    payload=[(select_condition_select['id'], {"choice": '大于'})],
    body=[(select_condition_select['id'], {"choice": '大于'})],
)

########################################################################################

border_value.add_method(
    name='update',
    http_method='put',
    payload=[(border_value['id'], {"text": '10'})],
    body=[(border_value['id'], {"text": '10'})],
)
########################################################################################

granularity.add_method(
    name='update',
    http_method='put',
    payload=[(granularity['id'], {"choice": '字数'})],
    body=[(granularity['id'], {"choice": '字数'})],
)
########################################################################################
max_word.add_method(
    name='update',
    http_method='put',
    payload=[(max_word['id'], {"text": '100'})],
    body=[(max_word['id'], {"text": '100'})],
)
########################################################################################

extra_word.add_method(
    name='update',
    http_method='put',
    payload=[(extra_word['id'], {"checked": '删除尾句'})],
    body=[(extra_word['id'], {"checked": '删除尾句'})],
)
########################################################################################


relation_select.add_method(
    name='update',
    http_method='put',
    payload=[(relation_select['id'], {"choice": '等于'})],
    body=[(relation_select['id'], {"choice": '等于'})],
)

########################################################################################

value_select.add_method(
    name='update',
    http_method='put',
    payload=[(value_select['id'], {"text": '动力'})],
    body=[(value_select['id'], {"text": '动力'})],
)
########################################################################################

output_num.add_method(
    name='update',
    http_method='put',
    payload=[(output_num['id'], {"text": '99'})],
    body=[(output_num['id'], {"text": '99'})],
)

########################################################################################

pos_select.add_method(
    name='update',
    http_method='put',
    payload=[(pos_select['id'], {"choice": '后'})],
    body=[(pos_select['id'], {"choice": '后'})],
)

########################################################################################

# glue_pic, glue_word, glue_video, glue_para_limit
glue_pic.add_method(
    name='update',
    http_method='put',
    payload=[(glue_pic['id'], {"text": '1'})],
    body=[(glue_pic['id'], {"text": '1'})],
)

glue_word.add_method(
    name='update',
    http_method='put',
    payload=[(glue_word['id'], {"text": '1'})],
    body=[(glue_word['id'], {"text": '1'})],
)

glue_video.add_method(
    name='update',
    http_method='put',
    payload=[(glue_video['id'], {"text": '1'})],
    body=[(glue_video['id'], {"text": '1'})],
)

glue_para_limit.add_method(
    name='update',
    http_method='put',
    payload=[(glue_para_limit['id'], {"text": '1'})],
    body=[(glue_para_limit['id'], {"text": '1'})],
)

########################################################################################

preserve_last.add_method(
    name='update',
    http_method='put',
    payload=[(preserve_last['id'], {"checked": None})],
    body=[(preserve_last['id'], {"checked": None})],
)

########################################################################################

analysis.add_method(
    name='analyze',
    http_method='post',
    payload=[
        (tag_select['id'], {"text": "外观"}),
        (weight_input['id'], {"text": "10"}),
        (select_condition_select['id'], {"choice": '大于'}),
        (border_value['id'], {"text": '10'}),
        (granularity['id'], {"choice": '字数'}),
        (max_word['id'], {"text": '100'}),
        (extra_word['id'], {"checked": '删除尾句'}),
        (relation_select['id'], {"choice": '等于'}),
        (value_select['id'], {"text": '动力'}),
        (output_num['id'], {"text": '99'}),
        (pos_select['id'], {"choice": '后'}),
        (glue_pic['id'], {"text": '1'}),
        (glue_word['id'], {"text": '1'}),
        (glue_video['id'], {"text": '1'}),
        (glue_para_limit['id'], {"text": '1'}),
        (preserve_last['id'], {"checked": None}),
    ],
    body=[
        (log_container['id'], log_container),
        (preview_container['id'], preview_container) # 如果不这样放在一个结果里返回 分不清预览和详情的边界
    ]
)
if __name__ == "__main__":
    # p = test_set_pagination
    # log_button.add_method(
    #     name='test_method',
    #     http_method='put',
    #     payload=[(p['id'], {"some": "thing"}), ('id1', {"some": "thing"})],
    #     body=[('id1', {"some": "thing"}), ('id1', {"some": "thing"})]
    # )
    workbench.dump()
    print('目前所有div 都是自定义 且没有type')