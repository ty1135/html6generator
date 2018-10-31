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

# 测试集 = 测试集标题 + PopLayout(过滤) + bucket页 + 分页组件

test_set_title = Label(text='测试集', description='测试集标签')
pop_up = CustomWidget(layout='PopLayout', description='第一个是触发点,第二是弹出的东西')
bucket_container = CustomWidget(layout='BoxLayout', description='bucket_container')  # TODO ! to be defined
test_set_pagination = Pagination(page=10, pages=10)

test_set.add_widgets(test_set_title, bucket_container, test_set_pagination)


# poplayout = 触发button + filter_condition

trigger_button = Button(label='筛选', disable=False)
filter_condition = CustomWidget(layout='BoxLayout', description='条件框')
pop_up.add_widgets(trigger_button, filter_condition)


# filter_condition  = checkbox + 确定button
test_set_conditions = CheckBox(options=[{"text": '标签', "value": "标签"}, {"text": '转发数', "value": "转发数"}],
                               label='测试集显示属性', checked=["标签", "转发数"])
filter_button = Button(label='确定', disable=False)
filter_condition.add_widgets(test_set_conditions, filter_button)

# bucket = sentence_id + sentence + 6个label(标签, 素材体积, 句子数, 总字数, 点赞数, 转发数)
bucket = DefaultWidget(type='rnc-single-test', description='单个bucket结构')

sentence_id = Label(text='1')
sentence = TextArea(text='对开门设计 起亚Novo概念车正式亮相_汽车之家', editable=False)
tag = TextField(label='标签：', text='标题', editable=False)
volume = TextField(label='素材体积：', text='10', editable=False)
num_sentence = TextField(label='句子数:', text='1', editable=False)
num_up = TextField(label='点赞数:', text='1', editable=False)
num_repost = TextField(label='转发数:', text='1', editable=False)

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


# 单条排序规则 = 条件类别Label + 标签textfield +  权重输入(textfield) + 新增按钮 + 删除按钮

single_order_rule = DefaultWidget(type='rnc-single-order-rule', description='单条排序规则')

condition_type = Label(text='标签条件（选填）', description='条件类别')
tag_select = TextField(label='标签:', editable=True)
weight_input = TextField(label='权重：', editable=True, text='10')
order_add_button = Button(icon='url/to/symbol', disable=False)
order_del_button = Button(label='删除', disable=True)


single_order_rule.add_widgets(condition_type, tag_select, weight_input, order_add_button, order_del_button)


# 排序规则容器 = 排序规则容器标题 + 一个或者多个 默认的单条排序规则
order_rule_title = Label(text='排序规则')
order_rule.add_widgets(order_rule_title, single_order_rule)


# 默认的单条筛选规则 = 筛选内容textfield + Select筛选条件 + Textfield边界值
select_content = TextField(label='筛选内容：', text='筛选加权分', editable=False)
select_condition_select = Select(label='筛选条件',option=[{"text": '大于', "value": '大于'},
                                         {"text": '小于', "value": '小于'}], choice='小于')
border_value = TextField(label='边界值：', editable=True)
single_select_rule = DefaultWidget(type='rnc-single-select-rule', description='单条筛选规则')
single_select_rule.add_widgets(select_content, select_condition_select)


# 筛选内容容器 = 筛选规则容器标题 + 一个默认的筛选排序规则
select_rule_title = Label(text='筛选规则')
select_rule.add_widgets(select_rule_title, single_select_rule)


# 裁剪规则容器 = 默认文字排版 + 默认召回图片

word_arrangment = DefaultWidget(type='rnc-text-typeset', description='文字排版')
pic_search = DefaultWidget(type='rnc-pic-search', description='召回图片')
clip_rule.add_widgets(word_arrangment, pic_search)

# 默认召回图片 = #召回图片title + 属性label + 关系Select + 值textfield +
#            +  输出数量textField+位置select +label图片选择顺序 + TODO 蛇皮表格

# pic_title = Label(text='召回图片')
attr_label = Label(text='属性label：')
relation_select = Select(label='关系：', option=[{"text": '等于', "value": '等于'}], choice='等于')
value_select = TextField(label='值：', editable=True)
output_num = TextField(label='输出数量', editable=True)

pos_select = Select(label='位置：', option=[{"text": '前', "value": '前'},
                                         {"text": '后', "value": '后'}], choice='后')
pic_order_label = Label(text='label图片选择顺序')

snake_table = {
  "version": 1,
  "id": "e2d1dde9-6d2e-42b9-a108-499fea2ca442",
  "view": {
    "name": "tree",
    "description": "树",
    "props": {
      "multiple": True,
    }
  },
  "model": {
    "title": "图片选择顺序",
    "node": [
      {
        "id": "42fbf196-192d-488d-a7cc-461ffa01251a",
        "name": "1",
        "number": 1,
        "action": [
          "create",
          "delete"
        ],
        "children": [
          {
            "id": "14145bea-22f5-427f-9282-e7a926d942ad",
            "name": "外观.正前",
            "number": 1,
            "action": [
              "update",
              "delete"
            ],
            "children": []
          }
        ]
      }]
  },
  "control": {
    "create": {
      "endpoint": "post /domain/resource",
      "payload": [
        {
          "id": "e2d1dde9-6d2e-42b9-a108-499fea2ca442",
          "value": {
            "relation": "child",
            "id": "e2d1dde9-6d2e-42b9-a108-499fea2ca442",
            "name": "2",
            "number": 0,
            "action": [
              "create",
              "update",
              "delete"
            ]
          }
        }
      ],
      "response": {
        "status": True,
        "body": {
          "id": "e2d1dde9-6d2e-42b9-a108-499fea2ca442",
          "value": {
            "relation": "child",
            "id": "e2d1dde9-6d2e-42b9-a108-499fea2ca442",
            "name": "2",
            "number": 0,
            "action": [
              "create",
              "update",
              "delete"
            ]
          }
        }
      }
    },
    "update": {
      "endpoint": "put /domain/resource",
      "payload": [
        {
          "id": "14145bea-22f5-427f-9282-e7a926d942ad",
          "value": {
            "id": "14145bea-22f5-427f-9282-e7a926d942ad",
            "name": "外观.侧面",
            "number": 0,
            "action": [
              "update",
              "delete"
            ]
          }
        }
      ],
      "response": {
        "status": True,
        "body": [
          {
            "id": "14145bea-22f5-427f-9282-e7a926d942ad",
            "value": {
              "id": "14145bea-22f5-427f-9282-e7a926d942ad",
              "name": "外观.侧面",
              "number": 0,
              "action": [
                "update",
                "delete"
              ]
            }
          }
        ]
      }
    },
    "delete": {
      "endpoint": "del /domain/resource",
      "payload": [
        {
          "id": "14145bea-22f5-427f-9282-e7a926d942ad",
          "value": {
            "id": "14145bea-22f5-427f-9282-e7a926d942ad",
            "name": "外观.侧面",
            "number": 0,
            "action": [
              "update",
              "delete"
            ]
          }
        }
      ],
      "response": {
        "status": True
      }
    }
  }
}

pic_search.add_widgets(attr_label, relation_select, value_select, output_num, pos_select, pic_order_label, snake_table)

# 默认文字排版 = 粒度select + 最大字数（句子数）textfield+ Label多余文字处理 +CheckBox
granularity = Select(label='粒度：', option=[
    {"text": '字数', "value": '字数'},
    {"text": '句子数', "value": '句子数'}], choice='句子数')
max_word = TextField(label='最大字数（句子数）：', editable=True)
extra_word_label = Label(text='最大字数（句子数）：')
extra_word = CheckBox(options=[{"text": "分段", "value": "分段"}, {"text": "删除尾句", "value": "删除尾句"}], checked="删除尾句")

word_arrangment.add_widgets(granularity, max_word, extra_word_label, extra_word)


# 拼接规则 =  拼接规则label + 单条默认拼接规则
glue_rule_title = Label(text='拼接规则')
single_glue_rule = DefaultWidget(type='rnc-glue-rule', desciption='拼接规则默认组件')

glue_rule.add_widgets(glue_rule_title, single_glue_rule)


# 单条默认拼接规则 = 4个select + checkbox

glue_rule_spec = Label(text='素材等价段落数')
glue_pic = TextField(label='图片(单位：段)', editable=True)
glue_word = TextField(label='文字(单位：段)', editable=True)
glue_video = TextField(label='视频(单位：段)', editable=True)
glue_para_limit = TextField(label='图片(单位：段)', editable=True)
preserve_last = CheckBox(options=[{"text": "保留最后一段", "value": "保留最后一段"}], checked="保留最后一段")

single_glue_rule.add_widgets(glue_rule_spec, glue_pic, glue_word, glue_video, glue_para_limit, preserve_last)

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

log_container = CustomWidget(layout='BoxLayout', description='log_container')
preview_container = CustomWidget(layout='BoxLayout', description='preview_container')

card_layout.add_widgets(log_container, preview_container)


# single_rnc_log = id_label + log_text + 若干个 key,value 的textField
single_rnc_log = DefaultWidget(type='rnc-single-log', description='rnc单条日志结构')
log_label = Label(text='ID: 3')
log_text = TextField(text="""ID： 2
作为哈弗F系列诞生的第二款车型，哈弗F7以哈弗HB-02概念车为原型。车厂针对市场需求对外观、内饰和动力系统进行了相应的改进。新车采用了哈弗最新的家族化设计风格，前脸处装配面积巨大的六边形中网，搭配鹰眼状的LED大灯，显得十分动感和犀利。
内饰方面，哈弗F7采用环抱式座舱设计，装备运动感强烈的三幅式平底方向盘，同时装配了全液晶仪表盘、大尺寸的中控屏幕和电子档把。哈弗F7配备智能语音控制系统、超级智能APP、智能互娱系统，ACC自适应巡航、车道保持、自动泊车等智能科技和主动安全系统。此外，F7还将搭载“i-pilot”智能领航系统，可实现L2级自动驾驶。
""", editable=False)
eg_kv_tf1 = TextField(label='加权分数', text='150')
eg_kv_tf2 = TextField(label='状态： ', text='显示')
eg_kv_tf3 = TextField(label='第一张图匹配到图像类别', text='外观.右后')
single_rnc_log.add_widgets(log_label, log_text, eg_kv_tf1, eg_kv_tf2, eg_kv_tf3)

# log_container = 几个或者多个 single_rnc_log
log_container.add_widgets(single_rnc_log)

# preview_container = 若干个label

para1 = Label(text='文章段落1')
pic1 = Label(icon='url/to/img1')
para2 = Label(text='文章段落2')
pic1 = Label(icon='url/to/img2')
preview_container.add_widgets(para1, pic1, para2, pic1)




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
    payload=[(test_set_pagination['id'], {"page": 1, "pages": 2}),
             (filter_condition['id'], {"checked": ["标签", "总字数"]})],
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
        (preview_container['id'], preview_container)
    ]
)

####################################################

filter_button.add_method(
    name='filter',
    http_method='get',
    payload=[
        (filter_condition['id'], {"checked": ["标签", "总字数"]}),
        (test_set_pagination['id'], {"page": 1, "pages": 2})],
    body=[(c_bucket['id'], c_bucket)]
)



if __name__ == "__main__":
    # p = test_set_pagination
    # log_button.add_method(
    #     name='test_method',
    #     http_method='put',
    #     payload=[(p['id'], {"some": "thing"}), ('id1', {"some": "thing"})],
    #     body=[('id1', {"some": "thing"}), ('id1', {"some": "thing"})]
    # )
    # ret = workbench.dump()
    ret = workbench.dump()
    print('目前所有div 都是自定义 且没有type')

    import subprocess


    def write_to_clipboard(output):
        process = subprocess.Popen(
            'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
        process.communicate(output.encode('utf-8'))

    write_to_clipboard(ret)