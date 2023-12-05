#import db

from flet import *

def post_wirte_main():
    post_write = Container()

    post_tag_list = Row(controls=[])
    post_tag = TextField(label="태그를 입력하세요", 
        border=InputBorder.NONE, 
        filled=True, 
        width=300, 
        on_submit=lambda _: fn_post_write_tag()
    )
    def fn_post_write_tag():
        if len(post_tag_list.controls) == 5 :    
            print("5개가 최대")
            return
        post_tag_list.controls.append(
            Container(
                Text(
                    " # " + post_tag.value + " ", 
                    color=colors.WHITE,
                    font_family='나눔바른고딕OTF'
                ), 
                border_radius=30, 
                bgcolor=colors.GREEN_ACCENT_700
            )
        )
        post_tag.value = ""
        post_tag.focus()

    post_title = TextField(label="제목을 입력하세요", 
            border=InputBorder.NONE,
            filled=True, 
            width=300
        )
    post_sub_title = TextField(label="부제목을 입력하세요", 
            border=InputBorder.NONE,
            filled=True, 
            width=300
        )
    post_desc = TextField(label="설명을 입력하세요", 
            value="\n\n\n\n\n", 
            border=InputBorder.NONE,
            filled=True, 
            multiline=True, 
            max_lines=5, 
            width=300, 
        )
    post_radio = RadioGroup(content=Row([
            Radio(value="1", label="축구"), 
            Radio(value="2", label="야구"), 
            Radio(value="3", label="농구"), 
            Radio(value="4", label="라켓"), 
            Radio(value="5", label="기타"), 
        ]))

    '''
    date_picker = DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )
    def change_date(e):
        print(f"Date picker changed, value is {date_picker.value}")

    def date_picker_dismissed(e):
        print(f"Date picker dismissed, value is {date_picker.value}")
    '''
    post_end_title = TextField(label="경기일을 입력하세요(yyyy-MM-dd)", 
            border=InputBorder.NONE,
            filled=True, 
            width=300,
            #on_focus=date_picker.pick_date()
        )

    


    post_write.content = Column(
            controls=[
                Row(alignment = alignment.center, width = 480, controls=[Text("게시물 작성", size=30, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')]), 
                Row(alignment = alignment.center, width = 480, controls=[
                    Text("제목", text_align=TextAlign.RIGHT, width=70, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'),
                    post_title
                ]), 
                Row(alignment = alignment.center, width = 480, controls=[
                    Text("부제목", text_align=TextAlign.RIGHT, width=70, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_sub_title
                ]), 
                Row(alignment = alignment.center, width = 480, controls=[
                    Text("설명", text_align=TextAlign.RIGHT, width=70, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_desc
                ]), 
                Row(alignment = alignment.center, width = 480, controls=[
                    Text("카테고리", text_align=TextAlign.RIGHT, width=70, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_radio
                ]), 
                Row(alignment = alignment.center, width = 480, controls=[
                    Text("태그", text_align=TextAlign.RIGHT, width=70, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_tag, 
                    post_tag_list
                ]), 
                Row(), 
                Row(alignment = alignment.center, width = 480, controls=[
                    Text("마감일", text_align=TextAlign.RIGHT, width=70, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_end_title
                ]),
                Row(alignment = alignment.center, width = 480, controls=[Text('',width = 170),
                    ElevatedButton(text="게시", bgcolor=colors.GREEN_ACCENT_700, color=colors.WHITE, 
                        on_click=lambda _: fn_post_write_post(
                            post_title.value, 
                            post_sub_title.value, 
                            post_desc.value, 
                            post_radio.value, 
                            post_tag_list.controls
                        )), 
                ]),
            ]
        )
    def fn_post_write_post(title, sub_title, desc, radio, tag_list):
        if title == "":
            print("제목을 입력해주세요")
            return
        elif sub_title == "":
            print("부제목을 입력해주세요")
            return
        elif desc.replace("\n", "") == "":
            print("설명을 입력해주세요")
            return
        elif radio == None:
            print("카테고리를 입력해주세요")
            return
        
        tag = ""
        for i in range(len(tag_list)):
            tag = tag + tag_list[i].content.value.replace("#", "").replace(" ", "") + "," 

        if tag == "":
            print("태그를 입력해주세요")
    return post_write