import db
from flet import *

'''
db.executeUpdate(
        'INSERT INTO Post(postTitle, postSubTitle, postDesc, postTag, postView, postDate, postEndDate, postDeadline, sID, uID) VALUES(?, ?, ?, ?, 0, datetime(\'now\',\'localtime\'), ?, ?, ?, 1)',
        ['asd', 'asd', 'asd', 'asd', '2023-11-11 17:00', 2, 1 ]
    )
'''

def main(page: Page):

    # 게시물 작성 뷰
    post_write = Container()
    post_tag_list = Row(controls=[])
    post_tag = TextField(label="태그를 입력하세요", 
        border=InputBorder.NONE, 
        filled=True, 
        width=500, 
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
        page.update()
    
    def fn_post_write():
        nonlocal post_tag_list
        post_tag_list = Row(controls=[])
        post_title = TextField(label="제목을 입력하세요", 
            border=InputBorder.NONE,
            filled=True, 
            width=500
        )
        post_sub_title = TextField(label="부제목을 입력하세요", 
            border=InputBorder.NONE,
            filled=True, 
            width=500
        )
        post_desc = TextField(label="설명을 입력하세요", 
            value="\n\n\n\n\n", 
            border=InputBorder.NONE,
            filled=True, 
            multiline=True, 
            max_lines=5, 
            width=500, 
        )
        post_radio = RadioGroup(content=Row([
            Radio(value="1", label="축구"), 
            Radio(value="2", label="야구"), 
            Radio(value="3", label="농구"), 
            Radio(value="4", label="라켓"), 
            Radio(value="5", label="기타"), 
        ]))
        post_end_title = TextField(label="경기일을 입력하세요(yyyy-MM-dd)", 
            border=InputBorder.NONE,
            filled=True, 
            width=500
        )
        post_write.content = Column(
            controls=[
                Row(controls=[
                    IconButton(
                        icon="ARROW_BACK",
                        icon_size=30, 
                        tooltip="메인으로", 
                        on_click=lambda _: page.go('/')
                    )
                ]), 
                Row(controls=[Text("     게시물 작성", size=30, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')]), 
                Row(controls=[
                    Text("제목", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_title
                ]), 
                Row(controls=[
                    Text("부제목", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_sub_title
                ]), 
                Row(controls=[
                    Text("설명", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_desc
                ]), 
                Row(controls=[
                    Text("카테고리", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_radio
                ]), 
                Row(controls=[
                    Text("태그", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_tag, 
                    post_tag_list
                ]), 
                Row(), 
                Row(controls=[
                    Text("마감일", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_end_title
                ]), 
                Row(controls=[
                    Text(width=250), 
                    ElevatedButton(text="게시", bgcolor=colors.GREEN_ACCENT_700, color=colors.WHITE, 
                        on_click=lambda _: fn_post_write_post(
                            post_title.value, 
                            post_sub_title.value, 
                            post_desc.value, 
                            post_radio.value, 
                            post_tag_list.controls
                        )), 
                    ElevatedButton(text="닫기", on_click=lambda _: page.go('/'))
                ]), 
            ]
        )
        page.go('/post_write')


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
            return

        













    # 마이페이지 뷰
    my_page = Container()
    def fn_my_page():
        list = db.executeQuery("SELECT * FROM User WHERE uID = 1")

        my_page.content = Column(
            controls=[
                Row(controls=[IconButton(
                    icon="ARROW_BACK",
                    icon_size=30,   
                    tooltip="메인으로", 
                    on_click=lambda _: page.go('/')
                )]), 
                Row(), Row(), 
                Row(controls=[Text("     내 정보", size=30, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')]), 
                Row(
                    controls=[DataTable(
                        columns=[
                            DataColumn(Text("아이디", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                            DataColumn(Text("이름", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                            DataColumn(Text("생년월일", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                            DataColumn(Text("휴대폰", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                            DataColumn(Text("성별", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                            DataColumn(Text("주소", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'))
                        ],
                        rows=[
                            DataRow(
                                cells=[
                                    DataCell(Text(list[0][1], font_family='나눔바른고딕OTF')),
                                    DataCell(Text(list[0][3], font_family='나눔바른고딕OTF')),
                                    DataCell(Text(list[0][4], font_family='나눔바른고딕OTF')),
                                    DataCell(Text(list[0][5], font_family='나눔바른고딕OTF')),
                                    DataCell(Text(list[0][6], font_family='나눔바른고딕OTF')),
                                    DataCell(Text(list[0][7], font_family='나눔바른고딕OTF'))
                                ],
                            ),   
                        ]        
                )]),
            ]
        )
        
        page.go('/my_page')




    # 태그 리스트 뷰 
    search = Container()
    def fn_tag_search():
        dt = DataTable(
            columns=[
                DataColumn(Text("제목", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')),
                DataColumn(Text("작성자", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')),
                DataColumn(Text("태그", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                DataColumn(Text("작성일", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                DataColumn(Text("조회수", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                DataColumn(Text("상태", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                DataColumn(Text("게시물 보기", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'))
            ],
        )
        list = db.executeQuery("SELECT * FROM Post p LEFT JOIN `USER` u ON p.uID = u.uID WHERE postTag LIKE '%" + tag_text.value + "%';")
        
        for i in range(len(list)):
            # 태그 텍스트
            tags = Row(controls=[])
            tag_split = list[i][4].split(",")
            for j in range(len(tag_split)):
                tags.controls.append(
                    Container(
                        Text(
                            "# " + tag_split[j], 
                            color=colors.WHITE,
                            font_family='나눔바른고딕OTF'
                        ), 
                        #border_radius=30, 
                        bgcolor=colors.BLUE_600
                    )
                )

            post_status = True

            dt.rows.append(
                DataRow(
                    [
                        DataCell(Text(list[i][1], font_family='나눔바른고딕OTF')), 
                        DataCell(Text(list[i][4], font_family='나눔바른고딕OTF')), 
                        DataCell(tags), 
                        DataCell(Text(list[i][6], font_family='나눔바른고딕OTF')), 
                        DataCell(Text(list[i][5], font_family='나눔바른고딕OTF')), 
                        DataCell(Text(
                            "모집중" if post_status else "마감", 
                            color=colors.GREEN_600 if post_status else colors.RED_600, 
                            font_family='나눔바른고딕OTF'
                        )), 
                        DataCell(TextButton("게시물 바로가기"))
                    ]
                )
            )

            # 리스트
            

        search.content = Column(
            controls=[
                Row(controls=[IconButton(
                    icon="ARROW_BACK",
                    icon_size=30, 
                    tooltip="메인으로", 
                    on_click=lambda _: page.go('/')
                )]), 
                Row(controls=[
                    dt
                ])
            ]
        )
        page.go('/search')















    # MainView에서 사용하는 오브젝트
    tag_text = TextField(
        label="태그로 검색하기", 

        prefix_icon="SEARCH", 
        border_radius=30, 
        on_submit=lambda _: fn_tag_search()
    )

    # 메인 뷰
    mainView = Container(
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                            content=Image(
                                src=f"./img/title.png",
                                width=110,
                                height=50,
                                fit=ImageFit.CONTAIN,
                            ), 
                            margin=margin.only(right=250)
                        ), 
                        tag_text,
                        Container(margin=margin.only(left=300)), 
                        IconButton(
                            icon="insert_emoticon",
                            #icon_color="pink600",
                            icon_size=30, 
                            tooltip="마이페이지", 

                            on_click=lambda _: fn_post_write()
                        ), 
                        IconButton(
                            icon="insert_emoticon",
                            #icon_color="pink600",
                            icon_size=30, 
                            tooltip="마이페이지", 

                            on_click=lambda _: fn_my_page()
                        ), 
                    ]
                ), 

                
                Text("Main"),
            ]
            
        )
    )
    

    # 태그 검색 컨테이너
    # 태그 검색 시 마다 새로 만듬

    pages = {
        '/': View(
                "/",
                [
                   mainView
                ],
            ),
        '/search': View(
                "/search",
                [
                    search
                ],
            ), 
        '/post_write': View(
                "/post_write",
                [
                    post_write
                ],
            ), 
        '/my_page': View(
                "/my_page",
                [
                    my_page
                ],
            ), 
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    
    page.on_route_change = route_change
    page.go(page.route)
   
if __name__ == '__main__':
    db.init()
    #app(target=main, view=AppView.WEB_BROWSER)
    app(target=main)
