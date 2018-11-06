from composite_widgets import DefaultWidget, CustomWidget
from atomic_widgets import (Button, CheckBox, DotCluster, Label, Pagination,
                            ProgressBar, Radio, ScrollBar, Select, TextArea,
                            TextField, TimeLine, Tree, Node, TreeSelect, TreeSelectNode, EditableSelect)

from layouts import (BoxLayout, CardLayout, PopupLayout, FlowLayout, BorderLayout, BoxLayout,
                     CardLayout, PopupLayout, GridLayout)


def div(direction, description):
    return CustomWidget(
        layout=BoxLayout(flex_direction=direction, justify_content='center'),
        description=description
)

#####################################################################################################
# 整个页面 = 左边菜单栏 + 右边Cardlayout
the_whole_stuff = div('row', "整个页面")
the_whole_stuff['layout']['attributes']['foldable_vector'] = [True, False]
the_whole_stuff['layout']['attributes']['folding_states'] = [False, False]

left_menu = div('column', "左边菜单栏")
right_card_layout = CustomWidget(layout=CardLayout(index=0), description="右边卡片")

the_whole_stuff.add_widgets(left_menu, right_card_layout)


# 左边菜单栏 = 百晓生调参Label + 菜单列表
label_wiki = Label(text='百晓生调参')
menu_list = div('column', "菜单列表")

left_menu.add_widgets(label_wiki, menu_list)

# 菜单列表 = Button * n
goods_button = Button(label='商品榜单')
fine_goods_button = Button(label='有好货')
menu_list.add_widgets(goods_button, fine_goods_button)

# 右边Cardlayout = goods_card + fine_goods_card
goods_card = div('column', "整个商品榜单对应的右边部分")
fine_goods_card = div('column', "welcome未定义")

right_card_layout.add_widgets(goods_card, fine_goods_card)

# goods_card = 场景div + 查询div+ 榜单内容div + 商品内容div
scene_div = div('column', '场景div')
search_div = div('column', '查询div')
rank_content_div = div('column', '榜单内容div')
goods_content_div = div('column', '商品内容div')

goods_card.add_widgets(scene_div, search_div, rank_content_div, goods_content_div)

# 场景div = scene_top(场景Label+ textfield + button) + 场景实物div
scene_top = div('row', 'scene_top')

scene_real = div('column', "场景实物div")

scene_div.add_widgets(scene_top, scene_real)

# scene_top = 场景Label+ scene_search
scene_label = Label(text='场景')
scene_search = div('row', '场景搜索部分')
scene_top.add_widgets(scene_label, scene_search)

# scene_search = textfield + button
scene_search_textfield = TextField(description="这是关键字输入框", text='10')
scene_search_button = Button(icon='url/to/search/icon')
scene_search.add_widgets(scene_search_textfield, scene_search_button)

# 场景实物div = TreeSelect + CheckBox
tree_select = TreeSelect(label='名称', editable=False, tree_direction='horizontal', value=11)

node_a = TreeSelectNode(text='季节')
node_aa = TreeSelectNode(text='夏')
node_a.add_children(node_aa)

node_b = TreeSelectNode(text='外出')
node_bb = TreeSelectNode(text='气-晴')
node_b.add_children(node_bb)

tree_select.add_node(node_a, node_b)

scene_check_box = CheckBox(label='样式', options=[
    dict(text='两跳-横向排版', value='horizontal'),
    dict(text='两跳-纵向排版', value='vertical'),
], checked='vertical')


scene_real.add_widgets(tree_select, scene_check_box)

#### 查询div = 查询top + 查询实质
search_top = div('row', '场景查询顶端')
search_real = div('column', "搜索实质部分")
search_div.add_widgets(search_top, search_real)

# 查询top = label + search查询部分
search_top_label = Label(text='查询')
search_top_search_div = div('row', '查询的查询部分')
search_top.add_widgets(search_top_label, search_top_search_div)

# search查询部分 = textfield + button
search_search_text_field = TextField(text='11')
search_search_button = Button(icon='url/to/search/button')
search_top_search_div.add_widgets(search_search_text_field, search_search_button)

# search_real = search_box * n
# search_real = search_bucket + button +textfield + 执行button

search_bucket = CustomWidget(
    layout=FlowLayout(flex_direction='row', justify_content='flex-start'),
    description="search_real_div"
)
long_add_button = Button(icon='url/to/adding/symbol')
final_text_field = TextField(label='榜单导语', text='faefaew', editable=True)
do_it_button = Button(label='执行')
search_real.add_widgets(search_bucket, long_add_button, final_text_field)

# search_bucket = search_box * n
search_box = div('row', "search_box")
search_bucket.add_widgets(search_box)
# 单个搜索框 = 左边内容 + 右边buttons
search_box_left = div('column', '单个搜索框的实质内容')
search_box_right = div('column', "按键部分")

search_box.add_widgets(search_box_left, search_box_right)

# 搜索box左边 = label + textarea + textfield*3
search_box_label = Label(text='#4 夏季防晒,防晒霜')
search_box_textarea = TextArea(label='过滤', text="""
hepburn_category_level_1等于美妆饰品
hepburn_category_level_2等于美容护肤/美体/精油
hepburn_category_level_3等于防晒
sku_title相似夏季|防晒|防晒霜
zk_price小于150""")
search_box_textfield1 = TextField(label='排序：', text='sku_sold 升序')
search_box_textfield2 = TextField(label='范围：', text='4')
search_box_textfield3 = TextField(label='数量：', text='4')

search_box_left.add_widgets(
    search_box_label,
    search_box_textarea,
    search_box_textfield1,
    search_box_textfield2,
    search_box_textfield3
)

# 搜索box右边 = 两个button
search_box_update_button = Button(label='修改')
search_box_delete_button = Button(label='删除')
search_box_right.add_widgets(search_box_update_button, search_box_delete_button)

####榜单内容
# rank_content_div = 榜单top_div + 榜单实质 rank_content_real
rank_top = div('row', "榜单top")
rank_real = div('column', "榜单实质")
rank_content_div.add_widgets(rank_top, rank_real)

# 榜单top_div = label
top_label = Label(text='榜单内容')
rank_top.add_widgets(top_label)

# rank_real = 行 * n
line1 = EditableSelect(label='标题', option=[{"text": "apple"}, {"text": "adult"}, {"text": "ability"}], value='apple')
line2_struct = div('column', "榜单首图部分")
line3_struct = div('column', "背景拼贴元素部分")

rank_real.add_widgets(line1, line2_struct, line3_struct)

# single1
single_rank_pic_1 = div('row', "单条榜单首图1")
# single_rank_pic = text_field + button
single_rank_pic_textfield1 = TextField(label='榜单首图', text='whatever')
single_rank_pic_add_button = Button(icon='any/url')
single_rank_pic_1.add_widgets(single_rank_pic_textfield1, single_rank_pic_add_button)

# single2
single_rank_pic_2 = div('row', "单条榜单首图2")
single_rank_pic_textfield2 = TextField(text='whatever')
single_rank_pic_del_button = Button(icon='any/url')
single_rank_pic_2.add_widgets(single_rank_pic_textfield2, single_rank_pic_del_button)

# line2_struct = 单条榜单首图 * n
line2_struct.add_widgets(single_rank_pic_1, single_rank_pic_2)


# line3_struct = 背景拼贴元素* n
###########
# single1
single_bkgd_pic_1 = div('row', "单条榜单首图1")
# single_bkgd_pic = text_field + button
single_bkgd_pic_textfield1 = TextField(label='背景拼贴元素', text='whatever')
single_bkgd_pic_add_button = Button(icon='any/url')
single_bkgd_pic_1.add_widgets(single_bkgd_pic_textfield1, single_bkgd_pic_add_button)

# single2
single_bkgd_pic_2 = div('row', "单条榜单首图2")
single_bkgd_pic_textfield2 = TextField(text='whatever')
single_bkgd_pic_del_button = Button(icon='any/url')
single_bkgd_pic_2.add_widgets(single_bkgd_pic_textfield2, single_bkgd_pic_del_button)

# line2_struct = 单条榜单首图 * n
line3_struct.add_widgets(single_bkgd_pic_1, single_bkgd_pic_2)

##################商品内容 goods_content_div = goods_top + good_real
goods_top = div('row', "goods_top_div")
goods_real = div('column', "goods_real_div")
goods_content_div.add_widgets(goods_top, goods_real)

# goods_top = label + 预览按钮 + 保存按钮
goods_top_label = Label(text='商品内容')
preview_button = Button(label='预览')
save_button = Button(label='保存')
goods_top.add_widgets(goods_top_label, preview_button, save_button)


# goods_real = single_sku *n
single_sku = div('column', "单个sku")
goods_real.add_widgets(single_sku)

#single_sku = delete_button +type_div + textfield_div
sku_delete_button = Button(label='删除')
type_div = CustomWidget(
    layout=GridLayout(row_size=2, column_size=2),
    description="sku上面textfield的部分"
)
textfield_div = div('column', "sku下面textfield的部分")

single_sku.add_widgets(type_div, textfield_div)

# type_div = 4 个 textfield
text_field1 = TextField(label='一级品类', text='美妆饰品', editable=True)
text_field2 = TextField(label='2级品类', text='', editable=True)
text_field3 = TextField(label='3级品类', text='', editable=True)
text_field4 = TextField(label='商品标签', text='防嗮', editable=True)

type_div.add_widgets(text_field1, text_field2, text_field3, text_field4)

# textfield_div = 标题editable_select + 商品附图bucket + 描述editable_select + 优惠信息bucket + 行动点bucket
title_editable_select = EditableSelect(label='标题', option=[{"text": "apple"}, {"text": "adult"}, {"text": "ability"}], value='apple')
goods_pic_bucket = div('column', '商品附图bucket')
des_editable_select = EditableSelect(label='描述', option=[{"text": "apple"}, {"text": "adult"}, {"text": "ability"}], value='apple')
sale_info_bucket = div('column', '优惠信息bucket')
action_bucket = div('column', '行动点bucket')

textfield_div.add_widgets(title_editable_select, goods_pic_bucket, des_editable_select, sale_info_bucket, action_bucket)

# 商品附图bucket, 优惠信息bucket, 行动点bucket

# goods_pic_bucket

# single1
single_goods_pic_1 = div('row', "single商品附图row")
# single_rank_pic = text_field + button
single_goods_pic_textfield1 = TextField(label='商品附图', text='whatever')
single_goods_pic_add_button = Button(icon='any/url')
single_goods_pic_1.add_widgets(single_goods_pic_textfield1, single_goods_pic_add_button)

# single2
single_goods_pic_2 = div('row', "single商品附图row2")
single_goods_pic_textfield2 = TextField(text='whatever')
single_goods_pic_del_button = Button(icon='any/url')
single_goods_pic_2.add_widgets(single_goods_pic_textfield2, single_goods_pic_del_button)

goods_pic_bucket.add_widgets(single_goods_pic_1, single_goods_pic_2)

## sale_info_bucket

single_sale1 = div('row', "single优惠信息row")
# single_rank_pic = text_field + button
single_sale_textfield1 = TextField(label='优惠信息', text='whatever')
single_sale_add_button = Button(icon='any/url')
single_sale1.add_widgets(single_sale_textfield1, single_sale_add_button)

# single2
single_sale2 = div('row', "single优惠信息row2")
single_sale_textfield2 = TextField(text='whatever')
single_sale_del_button = Button(icon='any/url')
single_sale2.add_widgets(single_sale_textfield2, single_sale_del_button)

sale_info_bucket.add_widgets(single_sale1, single_sale2)

## action_bucket

single_action1 = div('row', "single行动点row")
# single_rank_pic = text_field + button
single_action_textfield1 = TextField(label='行动点', text='whatever')
single_action_add_button = Button(icon='any/url')
single_action1.add_widgets(single_action_textfield1, single_action_add_button)

# single2
single_action2 = div('row', "single行动点row2")
single_action_textfield2 = TextField(text='whatever')
single_action_del_button = Button(icon='any/url')
single_action2.add_widgets(single_action_textfield2, single_action_del_button)

action_bucket.add_widgets(single_action1, single_action2)




##########################
##########################
##########################

scene_search_button.add_method(
    name='search',
    http_method='get',
    payload=[(scene_search_textfield['id'], scene_search_textfield.onto('text'))],
    body=[
        (tree_select['id'], tree_select.onto('value')),
        (scene_check_box['id'], scene_check_box.onto('checked')),
        (search_bucket['id'], search_bucket.onto('component')),
        (final_text_field['id'], final_text_field.onto('text')),
        (rank_real['id'], rank_real.onto('component')),
        (goods_real['id'], goods_real.onto('component'))
    ]
)


search_search_button.add_method(
    name='search',
    http_method='get',
    payload=[(search_search_text_field['id'], search_search_text_field.onto('text'))],
    body=[
        (search_bucket['id'], search_bucket.onto('component')),
    ]
)

search_box_delete_button.add_method(
    name='del',
    http_method='del',
    payload=[
        (search_box['id'], {})
    ],
    body=[]
)

do_it_button.add_method(
    name='exc',
    http_method='post',
    payload=[
        (tree_select['id'], tree_select.onto('value')),
        (scene_check_box['id'], scene_check_box.onto('checked')),
        (search_bucket['id'], search_bucket.onto('component')),
        (final_text_field['id'], final_text_field.onto('text')),
    ],
    body=[
        (rank_real['id'], rank_real.onto('component')),
        (goods_real['id'], goods_real.onto('component'))
    ]
)

######
single_rank_pic_add_button.add_method(
    name='add',
    http_method='local',
    payload=[
        (single_rank_pic_add_button['id'], {})
    ],
    body=[
        (line2_struct.clone()['id'], line2_struct.clone().onto('component'))
    ]
)

single_rank_pic_del_button.add_method(
    name='del',
    http_method='local',
    payload=[
        (single_rank_pic_2['id'], {})
    ],
    body=[]
)


single_bkgd_pic_add_button.add_method(
    name='add',
    http_method='local',
    payload=[
        (single_bkgd_pic_add_button.clone()['id'], {})
    ],
    body=[
        (line3_struct.clone()['id'], line3_struct.clone().onto('component'))
    ]
)

single_bkgd_pic_del_button.add_method(
    name='del',
    http_method='local',
    payload=[
        (single_bkgd_pic_2['id'], {})
    ],
    body=[]
)


####

single_goods_pic_add_button.add_method(
    name='add',
    http_method='local',
    payload=[
        (single_goods_pic_add_button.clone()['id'], {})
    ],
    body=[
        (goods_pic_bucket.clone()['id'], goods_pic_bucket.clone().onto('component'))
    ]
)

single_goods_pic_del_button.add_method(
    name='del',
    http_method='local',
    payload=[
        (single_goods_pic_2['id'], {})
    ],
    body=[]
)

###

single_sale_add_button.add_method(
    name='add',
    http_method='local',
    payload=[
        (single_sale_add_button.clone()['id'], {})
    ],
    body=[
        (sale_info_bucket.clone()['id'], sale_info_bucket.clone().onto('component'))
    ]
)

single_sale_del_button.add_method(
    name='del',
    http_method='local',
    payload=[
        (single_sale2['id'], {})
    ],
    body=[]
)
###

single_action_add_button.add_method(
    name='add',
    http_method='local',
    payload=[
        (single_action_add_button.clone()['id'], {})
    ],
    body=[
        (action_bucket.clone()['id'], action_bucket.clone().onto('component'))
    ]
)

single_action_del_button.add_method(
    name='del',
    http_method='local',
    payload=[
        (single_action2['id'], {})
    ],
    body=[]
)

sku_delete_button.add_method(
    name='del',
    http_method='local',
    payload=[
        (single_sku['id'], {}),
    ],
    body=[]
)

preview_popup = CustomWidget(
    layout=PopupLayout(position='window_center'),
    description='预览popup',
)

##
preview_content = div('column', '预览页面')

preview_content_label1 = Label(text='blah')
preview_content_label2 = Label(icon='url/to/image')
preview_content.add_widgets(preview_content_label1, preview_content_label2)

preview_popup.add_widgets(preview_content)


preview_button.add_method(
    name='preview',
    http_method='get',
    payload=[
        (goods_real['id'], goods_real.onto('component')),
        (rank_real['id'], rank_real.onto('component')),
    ],
    body=[(preview_popup['id'], preview_popup)]
)


save_button.add_method(
    name='save',
    http_method='post',
    payload=[
        (goods_real['id'], goods_real.onto('component')),
        (rank_real['id'], rank_real.onto('component')),
    ],
    body=[]
)

###

update_add_popup = CustomWidget(
    layout=PopupLayout(position='window_center'),
    description='更新和添加的popup',
)


update_add_popup_content = div('column', 'update_add_popup_content')

update_add_popup.add_widgets(update_add_popup_content)

# update_add_popup_content = 3个textfield + 过滤box + 排序box + button_pairs

popup_textfield1 = TextField(label='描述范围', text='事情')
popup_textfield2 = TextField(label='范围', text='6')
popup_textfield3 = TextField(label='数量', text='6')

filter_box = div('row', '过滤整个box')
order_box = div('row', '排序整个box')

button_pairs = div('row', "取消按钮和保存按钮的行")
button_pairs_cancel_button = Button(label='取消')
button_pairs_add_button = Button(label='保存')

button_pairs.add_widgets(button_pairs_cancel_button, button_pairs_add_button)

update_add_popup_content.add_widgets(popup_textfield1, popup_textfield2, popup_textfield3, filter_box,
                                     order_box, button_pairs)

# filter_box = title_box + real_filter
title_box = div('row', '标题layout')
real_filters = div('column', "过滤真实部分")
filter_box.add_widgets(title_box, real_filters)

# title_box = Label()
filter_label = Label(text='过滤：')
title_box.add_widgets(filter_label)

# real_filters = single_filter * n + add_button
single_filter = div('column', "一个过滤box")
add_button_beneath_single_filter = Button(icon='/url/to/image')
real_filters.add_widgets(single_filter, add_button_beneath_single_filter)

# single_filter = 字段textfield, 运算符select , 条件select
field_textfield = TextField(label='字段', text='hepburn_category_level_1')


####
# order_box = order_title_box + real_order
order_title_box = div('row', '整个排序标题部分')
real_order = div('column', "排序真实部分")
order_box.add_widgets(order_title_box, real_order)

# order_title_box = Label()
order_label = Label(text='排序：')
order_title_box.add_widgets(order_label)

# real_order = single_order * n + add_button
single_order = div('column', "一个排序box")
add_button_beneath_single_order = Button(icon='/url/to/image')
real_order.add_widgets(single_order, add_button_beneath_single_order)

# single_order  = 字段textfield + 方向select
order_field_textfield = TextField(label='字段', text='sku_sold')


direction_select = Select(label='方向', option=[
    dict(text='降序', value='降序'),
    dict(text='升序', value='升序')
], choice='升序')


real_filters.add_widgets(order_field_textfield, direction_select)
###################################


search_box_update_button.add_method(
    name='click',
    http_method='local',
    payload=[
        (search_box_left['id'], search_box_left.onto('component')),
    ],
    body=[(update_add_popup['id'], update_add_popup)]
)

long_add_button.add_method(
    name='click',
    http_method='local',
    payload=[
        (long_add_button['id'], {}),
    ],
    body=[(update_add_popup['id'], update_add_popup)]
)


###
button_pairs_add_button.add_method(
    name='add',
    http_method='post',
    payload=[(update_add_popup_content['id'], update_add_popup_content.clone().onto('component'))],
    body=[(search_bucket['id'], search_bucket.clone())]
)


if __name__ == "__main__":

    the_whole_stuff.dump()