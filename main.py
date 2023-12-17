from flet import *
import db
import datetime


def main(page: Page):

    # Program Default Setting
    page.title="잡포츠"
    page.window_width = 500
    page.window_min_width = 500
    page.window_max_width = 500
    page.window_height = 800
    page.window_min_height = 800
    page.window_max_height = 800

    # GV
    logo = Image(src = f"/logo.png", width = 160, height = 80, fit = ImageFit.CONTAIN)
    main_post_search = TextField(label="태그로 검색하기", prefix_icon="SEARCH", border_radius=30, on_submit=lambda _: fn_tag_search())
    detail_post_view = BottomSheet(content=Text("asd"), open=True)
    tag_search_datatable = DataTable(columns=[DataColumn(Text("제목　　　　　　　　　　", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("종목", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("상태", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("보기", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'))])
    post_tag_list = Row(controls=[])
    my_page = Column(controls=[], alignment = alignment.center, height=570, scroll = ScrollMode.AUTO)
    login_id = TextField(label="아이디를 입력하세요", border_radius=5)
    login_pw = TextField(label="비밀번호를 입력하세요", border_radius=5, password=True, can_reveal_password=True)
    login_idx = 0


    def fn_show_alert_dialog(msg):
        page.dialog = AlertDialog(
            title=Text(msg, text_align=TextAlign.CENTER, font_family='나눔바른고딕OTF')
        )
        page.dialog.open = True
        page.update()

    def fn_close_deatil_post(e):
        detail_post_view.open = False
        detail_post_view.update()

    def fn_show_user_chart(e):
        print(str(e.control.tooltip))
        count_list = db.executeQuery("SELECT sID, COUNT(sID), ROUND(AVG(playScore), 1) FROM POSTRESERVATION PR LEFT JOIN Post P ON PR.pID = P.pID WHERE PR.uID = "+str(e.control.tooltip)+" GROUP BY P.SID")
        s1, s2, s3, s4, s5 = 0, 0, 0, 0, 0 
        a1, a2, a3, a4, a5 = 0, 0, 0, 0, 0  
        c_max = 0
        for i in range(len(count_list)):
            if (int(count_list[i][0]) == 1) :
                s1 = int(count_list[i][1])
                a1 = float(count_list[i][2])
            elif (int(count_list[i][0]) == 2) :
                s2 = int(count_list[i][1])
                a2 = float(count_list[i][2])
            elif (int(count_list[i][0]) == 3) :
                s3 = int(count_list[i][1])
                a3 = float(count_list[i][2])
            elif (int(count_list[i][0]) == 4) :
                s4 = int(count_list[i][1])
                a4 = float(count_list[i][2])
            elif (int(count_list[i][0]) == 5) :
                s5 = int(count_list[i][1])
                a5 = float(count_list[i][2])
        c_max = max([s1, s2, s3, s4, s5])

        
        score_board = Column(controls=[])
        sport_list = ['', '축구', '농구', '야구', '라켓', '기타']

        
        for i in range(5):
            idx = i + 1
            tmp_list = db.executeQuery("SELECT * FROM POSTRESERVATION PR LEFT JOIN Post P ON PR.pID = P.pID LEFT JOIN USER U ON P.uID = U.uID WHERE PR.uID = "+str(e.control.tooltip)+" AND sID = " + str(idx))
            avg = 0
            
            desc_datatable = DataTable(columns=[DataColumn(Text("작성자", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("점수", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("평가", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')) ])
            
            for j in range(len(tmp_list)):
                avg = avg + int(tmp_list[j][3])
                if tmp_list[j][4] == "" or tmp_list[j][4] == None:

                    desc_datatable.rows.append(
                        DataRow(
                            [
                                DataCell(Text(tmp_list[j][21])), 
                                DataCell(Text(tmp_list[j][3])),
                                DataCell(Text("아직 평가를 남기지 않았습니다.")), 
                            ]
                        )
                    )
                else:
                    desc_datatable.rows.append(
                        DataRow(
                            [
                                DataCell(Text(tmp_list[j][21])), 
                                DataCell(Text(tmp_list[j][3])) ,
                                DataCell(Text(tmp_list[j][4])),
                            ]
                        )
                    )
            if len(tmp_list) != 0:
                avg = round(avg / len(tmp_list), 1) 



            score_board.controls.append(
                Column(controls=[
                    Text("\n" + sport_list[idx], weight=FontWeight.BOLD, font_family='나눔바른고딕OTF', size=17),
                    Text(" 총 " + str(len(tmp_list)) + "경기 / 평점 " + str(avg) + " 입니다.", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF', size=13),
                    Image(src = f"/star/star" + str(int(avg)) + ".png", width = 300, height = 50, fit = ImageFit.CONTAIN),
                    desc_datatable
                ])
            )

        page.dialog = AlertDialog(
            title=Text("집계", text_align=TextAlign.CENTER, font_family='나눔바른고딕OTF'), 
            content=Column(controls=[
                Column(controls=[
                    Text("참여 횟수", text_align=TextAlign.LEFT, size=20, width=500, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    BarChart(
                        bar_groups=[
                            BarChartGroup(x=0,
                                bar_rods=[
                                    BarChartRod(
                                        from_y=0,
                                        to_y=s1,
                                        width=20,
                                        color=colors.AMBER,
                                        tooltip=str(s1),
                                        border_radius=0,
                                    ),
                                ],
                            ),
                            BarChartGroup(
                                x=1,
                                bar_rods=[
                                    BarChartRod(
                                        from_y=0,
                                        to_y=s2,
                                        width=20,
                                        color=colors.BLUE,
                                        tooltip=str(s2),
                                        border_radius=0,
                                    ),
                                ],
                            ),
                            BarChartGroup(
                                x=2,
                                bar_rods=[
                                    BarChartRod(
                                        from_y=0,
                                        to_y=s3,
                                        width=20,
                                        color=colors.RED,
                                        tooltip=str(s3),
                                        border_radius=0,
                                    ),
                                ],
                            ),
                            BarChartGroup(
                                x=3,
                                bar_rods=[
                                    BarChartRod(
                                        from_y=0,
                                        to_y=s4,
                                        width=20,
                                        color=colors.ORANGE,
                                        tooltip=str(s4),
                                        border_radius=0,
                                    ),
                                ],
                            ),
                            BarChartGroup(
                                x=4,
                                bar_rods=[
                                    BarChartRod(
                                        from_y=0,
                                        to_y=s5,
                                        width=20,
                                        color=colors.GREEN,
                                        tooltip=str(s5),
                                        border_radius=0,
                                    ),
                                ],
                            ),
                        ],
                        border=border.all(1, colors.GREY_400),
                        left_axis=ChartAxis(
                            labels_size=40, title=Text("종목별 참여 횟수"), title_size=40
                        ),
                        bottom_axis=ChartAxis(
                            labels=[
                                ChartAxisLabel(value=0, label=Container(Text("축구"), padding=10)),
                                ChartAxisLabel(value=1, label=Container(Text("농구"), padding=10)),
                                ChartAxisLabel(value=2, label=Container(Text("야구"), padding=10)),
                                ChartAxisLabel(value=3, label=Container(Text("라켓"), padding=10)),
                                ChartAxisLabel(value=4, label=Container(Text("기타"), padding=10)),
                            ],
                            labels_size=40,
                        ),
                        horizontal_grid_lines=ChartGridLines(
                            color=colors.GREY_300, width=1, dash_pattern=[3, 3]
                        ),
                        tooltip_bgcolor=colors.with_opacity(0.5, colors.GREY_300),
                        max_y=c_max + 2,
                        interactive=True,
                        expand=True,
                    ),
                

                ], height=300),
                Text("\n\n\n종목별 평점 확인하기", text_align=TextAlign.LEFT, size=20, width=500, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                score_board
            ], height=570, scroll = ScrollMode.AUTO)
        )
        page.dialog.open = True
        page.update()

    def fn_deposit_apply(e):
        if e.control.text == ' 보증금 대기 ':
            query = "UPDATE PostReservation SET isUserCheck = 1 WHERE pRID = " + str(int(e.control.tooltip))
            db.executeUpdateSingle( query )
            fn_show_alert_dialog("보증금(3,000원)이\n입금되지 않았습니다.\n110-260-119670 신한 조우성")
            fn_my_page_refresh()


    tmp_drop = Dropdown(
                label="용병 평점",
                hint_text="용병의 평점을 입력하세요",
                options=[
                    dropdown.Option("1 점"),
                    dropdown.Option("2 점"),
                    dropdown.Option("3 점"),
                    dropdown.Option("4 점"),
                    dropdown.Option("5 점"),
                ],
                autofocus=True,
            )
    tmp_desc = TextField()

    def fn_desc_change(idx):
        nonlocal tmp_drop
        nonlocal tmp_desc

        page.dialog.open = False
        page.update()
        
        db.executeUpdateSingle("UPDATE PostReservation SET playScore = " + str(tmp_drop.value[0:1]) + ", playDesc = '" + tmp_desc.value + "' WHERE pRID = " + str(idx))
        fn_show_alert_dialog("작성되었습니다!")


    def fn_desc_apply(e):
        if e.control.text == ' 진행 ':    
            page.dialog = AlertDialog(
                title=Text("평가", text_align=TextAlign.CENTER, font_family='나눔바른고딕OTF'), 
                content=Column(controls=[
                    tmp_drop,
                    Text("설명", text_align=TextAlign.LEFT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    tmp_desc,
                    Row(controls=[ElevatedButton(text="적용", bgcolor="GREEN", color="WHITE", on_click=lambda _: fn_desc_change(e.control.tooltip))], alignment=MainAxisAlignment.END) 
                ], height=200)
            )
            page.dialog.open = True
            page.update()

        elif e.control.text == ' 미승인 ':
            query = "UPDATE PostReservation SET isPostCheck = 1 WHERE pRID = " + str(int(e.control.tooltip))
            db.executeUpdateSingle( query )
            fn_show_alert_dialog("해당 용병 참석을 승인했습니다!")
            fn_my_page_refresh()


    def fn_post_apply(e):
        print(e.control.tooltip)
        if e.control.text == ' 미승인 ':
            query = "UPDATE PostReservation SET isPostCheck = 1 WHERE pRID = " + str(int(e.control.tooltip))
            db.executeUpdateSingle( query )
            fn_show_alert_dialog("해당 용병 참석을 승인했습니다!")
            fn_my_page_refresh()
        
    def fn_my_page_refresh():
        nonlocal my_page

        nonlocal login_idx

        sport_list = ['', '축구', '농구', '야구', '라켓', '기타']
        user_list = db.executeQuery("SELECT * FROM User WHERE uID = " + str(login_idx))
        post_list = db.executeQuery("SELECT * FROM POSTRESERVATION PR LEFT JOIN POST P ON PR.pID = P.pID LEFT JOIN USER U ON PR.uID = U.uID WHERE P.uID = " + str(login_idx))
        apply_list = db.executeQuery("SELECT * FROM POSTRESERVATION PR LEFT JOIN POST P ON PR.pID = P.pID LEFT JOIN USER U ON P.uID = U.uID WHERE PR.uID = " + str(login_idx))
        

        my_page.controls = [
            Row(controls=[
                Text("내 정보", text_align=TextAlign.LEFT, size=20, width=120, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                ElevatedButton(text="집계", bgcolor="GREEN", color="WHITE", tooltip=int(login_idx), on_click=fn_show_user_chart), 
            ]), 
            Row(controls=[DataTable(
                width=450, 
                columns=[
                    DataColumn(Text("아이디", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                    DataColumn(Text("이름", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                    DataColumn(Text("생년월일", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                ],
                rows=[
                    DataRow(
                        cells=[
                            DataCell(Text(user_list[0][1], font_family='나눔바른고딕OTF')),
                            DataCell(Text(user_list[0][3], font_family='나눔바른고딕OTF')),
                            DataCell(Text(user_list[0][4], font_family='나눔바른고딕OTF')),
                        ],
                    ),   
                ]        
            )]),
            Row(controls=[DataTable(
                width=450, 
                columns=[
                    DataColumn(Text("휴대폰", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                    DataColumn(Text("성별", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), 
                    DataColumn(Text("주소", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'))
                ],
                rows=[
                    DataRow(
                        cells=[
                            DataCell(Text(user_list[0][5], font_family='나눔바른고딕OTF')),
                            DataCell(Text(user_list[0][6], font_family='나눔바른고딕OTF')),
                            DataCell(Text(user_list[0][7], font_family='나눔바른고딕OTF'))
                        ],
                    ),   
                ]        
            )]),
            Row(controls=[DataTable(
                width=450, 
                columns=[
                    DataColumn(Text("내 계좌번호", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'))
                ],
                rows=[
                    DataRow(
                        cells=[
                            DataCell(Text("110-260-119670 신한 조우성", font_family='나눔바른고딕OTF')),
                        ],
                    ),   
                ]        
            )]),
        ]
        post_datatable = DataTable(columns=[DataColumn(Text("게시물", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("신청자", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("상태", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("채팅", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')) ])
        apply_datatable = DataTable(columns=[DataColumn(Text("게시물", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("상태", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')), DataColumn(Text("채팅", weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')) ])
        
        # 나의 용병 모집
        for i in range(len(post_list)):
            st_text=[' 미승인 ', ' 보증금 대기 ', ' 진행 ']
            st_bg = ["RED", "YELLOW", "GREEN"]
            st_color = ["WHITE", "BLACK", "WHITE"]
            
            st = 0
            # 미승인
            if post_list[i][1] == 0 and post_list[i][2] == 0 :
                st = 0
            # 보증금 대기중
            elif post_list[i][1] == 1 and post_list[i][2] == 0 :
                st = 1
            # 진행 확정
            elif post_list[i][1] == 1 and post_list[i][2] == 1 :
                st = 2

            post_datatable.rows.append(
                DataRow(
                    [
                        DataCell(TextButton(post_list[i][8], on_click=fn_show_detail_post, tooltip=post_list[i][7])), 
                        DataCell(TextButton(post_list[i][21], tooltip=post_list[i][18], on_click=fn_show_user_chart)), 

                        DataCell(ElevatedButton(text=st_text[st], bgcolor=st_bg[st], color=st_color[st], tooltip=post_list[i][0], on_click=fn_desc_apply)),    
                        DataCell(IconButton(icon=icons.WECHAT, icon_color="BLACK", on_click=lambda _: page.go('/chat'), tooltip=post_list[i][7])), 
                    ]
                )
            )
            



        # 나의 용병 신청
        for i in range(len(apply_list)):
            st_text=[' 미승인 ', ' 보증금 대기 ', ' 진행 ']
            st_bg = ["RED", "YELLOW", "GREEN"]
            st_color = ["WHITE", "BLACK", "WHITE"]
            
            st = 0
            # 미승인
            if apply_list[i][1] == 0 and apply_list[i][2] == 0 :
                st = 0
            # 보증금 대기중
            elif apply_list[i][1] == 1 and apply_list[i][2] == 0 :
                st = 1
            # 진행 확정
            elif apply_list[i][1] == 1 and apply_list[i][2] == 1 :
                st = 2

            apply_datatable.rows.append(
                DataRow(
                    [
                        DataCell(TextButton(apply_list[i][8], on_click=fn_show_detail_post, tooltip=apply_list[i][7])), 
                        DataCell(ElevatedButton(text=st_text[st], bgcolor=st_bg[st], color=st_color[st], tooltip=apply_list[i][0], on_click=fn_deposit_apply)),    
                        DataCell(IconButton(icon=icons.WECHAT, icon_color="BLACK", on_click=lambda _: page.go('/chat'), tooltip=apply_list[i][7])), 
                    ]
                )
            )

        my_page.controls.append(Text("\n\n\n나의 용병 모집", text_align=TextAlign.LEFT, size=20, width=120, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'))
        my_page.controls.append(Row(controls=[post_datatable], alignment = alignment.center, width=800, scroll = ScrollMode.AUTO))

        my_page.controls.append(Text("\n\n\n나의 용병 신청", text_align=TextAlign.LEFT, size=20, width=120, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'))
        my_page.controls.append(Row(controls=[apply_datatable], alignment = alignment.center, width=500, scroll = ScrollMode.AUTO))

        page.update()



    #
    #
    # 개별 게시물 확인
    #
    #
    def fn_apply_post(e):
        nonlocal login_idx

        if len(db.executeQuery("SELECT * FROM PostReservation WHERE uID = " + str(login_idx) + " AND pID = " + str(int(e.control.tooltip)) )):
            fn_show_alert_dialog("이미 신청한 게시물입니다.")
            return


        db.executeUpdate("INSERT INTO PostReservation(isPostCheck, isUserCheck, playScore, playDesc, pID, uID) VALUES(0, 0, 0, NULL, ?, ?)", [e.control.tooltip, login_idx])
        fn_show_alert_dialog("신청이 완료되었습니다. \n진행 현황은 마이페이지에서 확인 가능합니다.")

        detail_post_view.open = False
        detail_post_view.update()

    def fn_show_detail_post(e):
        nonlocal post_tag_list
        post_tag_list.controls = None
        
        db.executeUpdateSingle("UPDATE Post SET postView = postView + 1 WHERE pID = " + str(e.control.tooltip))
        list = db.executeQuery("SELECT * FROM POST P LEFT JOIN USER U ON P.uID = U.uID WHERE P.pID=" + str(e.control.tooltip))
        post_status = datetime.datetime.strptime(list[0][7], '%Y-%m-%d %H:%M') < datetime.datetime.now()

        sp = list[0][4].split(',')
        for i in range(len(sp)): 
            post_tag_list.controls.append(
                Container(
                    Text(" # " + sp[i] + " ", color=colors.WHITE, font_family='나눔바른고딕OTF'), 
                    border_radius=30, 
                    bgcolor=colors.GREEN_ACCENT_700
                )
            )

        detail_post_view.content=Column(
            controls=[
                Row(), 
                Row(controls=[
                    Text("제목", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    TextField(value=list[0][1], read_only=True)
                ]), 
                Row(controls=[
                    Text("부제목", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    TextField(value=list[0][2], read_only=True)
                ]), 
                Row(controls=[
                    Text("설명", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    TextField(value=list[0][3], read_only=True)
                ]), 
                Row(controls=[
                    Text("경기일", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    TextField(value=list[0][7], read_only=True), 
                ]), 
                Row(controls=[
                    Text("태그", text_align=TextAlign.RIGHT, width=100, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    post_tag_list
                ]), 
                Row(controls=[
                    Text("작성자: " + list[0][14], text_align=TextAlign.RIGHT, width=150, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    Text("연락처: " + list[0][16], text_align=TextAlign.CENTER, width=180, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    Icon(name="REMOVE_RED_EYE", color="#c1c1c1"),  
                    Text(list[0][5], width=30, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                ]), 
                Row(),
                Row(controls=[
                    ElevatedButton(text="신청", bgcolor="GREEN", color="WHITE", tooltip=list[0][0], on_click=fn_apply_post, disabled=True if (list[0][11] == 1 or post_status) else False), 
                    Text("", width=60)
                ], alignment=MainAxisAlignment.END), 
            ]
        )

        detail_post_view.open = True
        detail_post_view.update()


    #
    #
    # 메인 페이지 태그로 게시물 검색
    #
    #
    def fn_tag_search():
        list = db.executeQuery("SELECT * FROM Post WHERE postTag LIKE '%" + main_post_search.value + "%';")
        sport_list = ['', '축구', '농구', '야구', '라켓', '기타']
        
        tag_search_datatable.rows = None

        for i in range(len(list)):
            # 상태
            post_status = datetime.datetime.strptime(list[i][7], '%Y-%m-%d %H:%M') >= datetime.datetime.now()

            tag_search_datatable.rows.append(
                DataRow(
                    [
                        DataCell(Text(list[i][1], font_family='나눔바른고딕OTF')), 
                        DataCell(Text(sport_list[list[i][9]], font_family='나눔바른고딕OTF')), 
                        DataCell(Text(
                            "모집중" if post_status else "마감", 
                            color=colors.GREEN_600 if post_status else colors.RED_600, 
                            font_family='나눔바른고딕OTF'
                        )), 
                        DataCell(IconButton(icon=icons.SUBDIRECTORY_ARROW_RIGHT, icon_color="BLACK", on_click=fn_show_detail_post, tooltip=list[i][0])), 
                    ]
                )
            )

        page.update()



    # 게시물 보기_탭별 메뉴 View
    def fn_get_post_tab_menu(idx):
        list = []
        
        if idx == 0:
            # 전체 게시물 조회
            list = db.executeQuery("SELECT * FROM post P LEFT JOIN USER U ON P.uID = U.uID")
        else:
            # 분야별 게시물 조회
            list = db.executeQuery("SELECT * FROM POST P LEFT JOIN USER U ON P.uID = U.uID WHERE P.sID = " + str(idx))
        
        # 게시물 없을 시
        if len(list) == 0:
            return Text("\n     등록된 게시물이 없습니다!")

        cmp = Column(controls=[])        
        
        for i in range(len(list)):
            post_status = datetime.datetime.strptime(list[i][7], '%Y-%m-%d %H:%M') >= datetime.datetime.now()

            cmp.controls.append(
                Column([
                    Image(src = f"/tab" + str(list[i][9]) + ".jpg", width = 480, height = 250, fit = ImageFit.CONTAIN), 
                    Row(controls=[
                        Text("   " + list[i][1], text_align=TextAlign.LEFT, width=400, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'),
                        Text(
                            "모집중" if post_status else "마감", 
                            color=colors.GREEN_600 if post_status else colors.RED_600, 
                            font_family='나눔바른고딕OTF'
                        )
                    ]), 
                    Row(controls=[
                        Text("   작성자: " + list[i][14], width=150, bgcolor="white", font_family='나눔바른고딕OTF'), 
                        Text("경기일: " + list[i][7], width=220, bgcolor="white", font_family='나눔바른고딕OTF'), 
                        Icon(name="REMOVE_RED_EYE", color="#c1c1c1"),  
                        Text(list[i][5], width=30, weight=FontWeight.BOLD, bgcolor="white", font_family='나눔바른고딕OTF'), 
                    ]),
                    Row(controls=[
                        ElevatedButton(text="게시물 보기", width=460, color="GREEN", bgcolor="WHITE", on_click=fn_show_detail_post, tooltip=list[i][0])
                    ]), 
                    Row()
                ], 
                alignment = MainAxisAlignment.START),
            )
        return Column([ cmp ], alignment = alignment.center, scroll = ScrollMode.AUTO)



    #
    #
    # 게시물 작성
    #
    #
    write_post_tag = TextField(label="태그를 입력하세요", 
        border=InputBorder.NONE, 
        filled=True, 
        width=300, 
        on_submit=lambda _: fn_post_write_tag()
    )
    def fn_post_write_tag():
        if len(post_tag_list.controls) == 5 :    
            fn_show_alert_dialog("태그는 5개가 최대입니다.")
            return
        post_tag_list.controls.append(
            Container(
                Text(
                    " # " + write_post_tag.value + " ", 
                    color=colors.WHITE,
                    font_family='나눔바른고딕OTF'
                ), 
                border_radius=30, 
                bgcolor=colors.GREEN_ACCENT_700
            )
        )
        write_post_tag.value = ""
        write_post_tag.focus()
        page.update()

    def write_post():
        nonlocal post_tag_list
        write_post_title = TextField(label="제목을 입력하세요", border=InputBorder.NONE, filled=True, width=300)
        write_post_sub_title = TextField(label="부제목을 입력하세요", border=InputBorder.NONE, filled=True, width=300)
        write_post_desc = TextField(label="설명을 입력하세요", value="\n\n\n", border=InputBorder.NONE, filled=True, multiline=True, max_lines=3, width=300)
        write_post_radio = RadioGroup(content=Row([Radio(value="1", label="축구"), Radio(value="2", label="야구"), Radio(value="3", label="농구"), Radio(value="4", label="라켓"), Radio(value="5", label="기타") ]))
        write_post_end_title = TextField(label="경기일을 입력하세요(yyyy-MM-dd hh:mm)", border=InputBorder.NONE, filled=True, width=300)
        write_post_dead_line = TextField(label="모집 인원 수를 입력하세요", border=InputBorder.NONE, filled=True, multiline=True, width=300)
        
        return Column(
            controls=[
                Row(controls=[
                    Text("제목", text_align=TextAlign.RIGHT, width=80, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    write_post_title
                ]), 
                Row(controls=[
                    Text("부제목", text_align=TextAlign.RIGHT, width=80, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    write_post_sub_title
                ]), 
                Row(controls=[
                    Text("설명", text_align=TextAlign.RIGHT, width=80, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    write_post_desc
                ]), 
                Row(controls=[
                    Text("카테고리", text_align=TextAlign.RIGHT, width=80, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    write_post_radio
                ]), 
                Row(controls=[
                    Text("태그", text_align=TextAlign.RIGHT, width=80, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    write_post_tag
                ]), 
                Row(controls=[Text("", width=80), post_tag_list]), 
                Row(controls=[
                    Text("마감일", text_align=TextAlign.RIGHT, width=80, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    write_post_end_title
                ]), 
                Row(controls=[
                    Text("모집 인원", text_align=TextAlign.RIGHT, width=80, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'), 
                    write_post_dead_line
                ]), 
                Row(controls=[
                    ElevatedButton(text="게시", bgcolor="GREEN", color="WHITE", 
                    on_click=lambda _: fn_post_write_post(
                            write_post_title.value, 
                            write_post_sub_title.value, 
                            write_post_desc.value, 
                            write_post_radio.value, 
                            post_tag_list.controls, 
                            write_post_end_title.value,
                            write_post_dead_line.value
                        )), 
                    Text("", width=60)
                ], alignment=MainAxisAlignment.END)
            ]
        )
    def fn_post_write_post(title, sub_title, desc, radio, tag_list, end_date, dead_line):
        nonlocal login_idx

        if title == "":
            fn_show_alert_dialog("제목을 입력해주세요")
            return
        elif sub_title == "":
            fn_show_alert_dialog("부제목을 입력해주세요")
            return
        elif desc.replace("\n", "") == "":
            fn_show_alert_dialog("설명을 입력해주세요")
            return
        elif radio == None:
            fn_show_alert_dialog("카테고리를 입력해주세요")
            return
        
        tag = ""
        for i in range(len(tag_list)):
            tag = tag + tag_list[i].content.value.replace("#", "").replace(" ", "")
            if i != len(tag_list) - 1 :
                tag = tag + "," 
        if tag == "":
            fn_show_alert_dialog("태그를 입력해주세요")
            return

        try:
            tmp = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M')
        except:
            fn_show_alert_dialog("날짜 형식을 맞춰주세요")
            return

        try:
            tmp = int(dead_line)
        except:
            fn_show_alert_dialog("모집 인원 수는 숫자로 입력해주세요")
            return

        db.executeUpdate(
            'INSERT INTO Post(postTitle, postSubTitle, postDesc, postTag, postView, postDate, postEndDate, postDeadline, sID, uID) VALUES(?, ?, ?, ?, 1, datetime(\'now\',\'localtime\'), ?, ?, ?, ?)',
            [ title, sub_title, desc.replace("\n", ""), tag, end_date, dead_line, radio, login_idx ]
        )

        page.go('/')
        fn_show_alert_dialog("게시글이 작성 완료되었습니다.")



    def fn_login():
        nonlocal login_id
        nonlocal login_pw
        nonlocal login_idx

        if len(login_id.value) == 0 or login_id == None:
            fn_show_alert_dialog("아이디를 입력해주세요!")
            return
        elif len(login_pw.value) == 0 or login_pw == None:
            fn_show_alert_dialog("비밀번호를 입력해주세요!")
            return

        valid = db.executeQuery("SELECT * FROM User WHERE userID = '" + login_id.value + "' AND userPW = '" + login_pw.value + "';")
        if len(valid) == 0:
            fn_show_alert_dialog("일치하는 계정이 없습니다.")
            return
        
        fn_show_alert_dialog(valid[0][3] + "님, 환영합니다!")
        login_idx = int(valid[0][0])
        page.go('/')

    #
    #
    # Page Init
    #
    #
    def change_page(e):
        if e.control.selected_index == 2:
            nonlocal post_tag_list
            post_tag_list.controls = None
            page.update()
        elif e.control.selected_index == 3:
            fn_my_page_refresh()

        page_list = ['/', '/post_read', '/post_write', '/my_page']
        page.go(page_list[e.control.selected_index])


    page.overlay.append(detail_post_view) 
    page.navigation_bar = NavigationBar(
        on_change = change_page,
        selected_index = 0,
        bgcolor=colors.WHITE, 
        destinations = [
            NavigationDestination(icon = icons.HOME_ROUNDED, label="메인 페이지"),
            NavigationDestination(icon = icons.REMOVE_RED_EYE_ROUNDED, label = "게시글 보기"),
            NavigationDestination(icon = icons.POST_ADD_ROUNDED, label="게시글 작성"),
            NavigationDestination(icon = icons.TAG_FACES_SHARP, label = "마이 페이지"),
        ]
    )

    
    post_read_tab = Tabs(animation_duration = 0,
        tabs=[
            Tab(text="전체", content=fn_get_post_tab_menu(0)),
            Tab(text="축구", content=fn_get_post_tab_menu(1)),
            Tab(text="농구", content=fn_get_post_tab_menu(2)),
            Tab(text="야구", content=fn_get_post_tab_menu(3)),
            Tab(text="라켓", content=fn_get_post_tab_menu(4)),
            Tab(text="기타", content=fn_get_post_tab_menu(5)),
        ],
        expand = 1
    )

    pages = {
        '/login': View(
                "/login",
                [
                    Text("\n\n\n\n\n\n\n"),
                    Row(controls=[
                        Image(
                            src=f"./logo.png",
                            width=200,
                            height=100,
                            fit=ImageFit.CONTAIN,
                        )
                    ], alignment=MainAxisAlignment.CENTER), 
                    Row(controls=[
                        Text("　　　　　"),
                        login_id,
                    ]),
                    Row(controls=[
                        Text("　　　　　"),
                        login_pw,
                    ]),
                    Row(controls=[
                        Text("　　　　　"),
                        ElevatedButton(width=300, height=50, text="로그인", bgcolor="GREEN", color="WHITE", on_click=lambda _: fn_login(),
                            style=ButtonStyle(
                                shape={
                                    MaterialState.DEFAULT: RoundedRectangleBorder(radius=5),
                                }
                            )
                        )
                    ]),
                    Row(controls=[
                        Text("　　　　　　　　　"),
                        TextButton("아직 회원이 아니신가요?")
                    ]), 
                    Row(controls=[
                        Text("　　　　　 　　　　"),
                        TextButton("아이디 / 비밀번호 찾기")
                    ])
                ],
            ), 
        '/': View(
                "/",
                [
                    Row([ logo, main_post_search]), 
                    Column(
                        [tag_search_datatable], 
                        height=300, 
                        scroll=ScrollMode.AUTO
                    ), 
                    Image(
                        src=f"./banner.png",
                        width=500,
                        height=300,
                        fit=ImageFit.CONTAIN,
                    ), 
                    page.navigation_bar
                ],
            ),
        '/post_write': View(
                "/post_write",
                [
                    logo,
                    write_post(),
                    page.navigation_bar
                ],
            ), 
        '/post_read': View(
                "/post_read",
                [
                    logo, 
                    post_read_tab, 
                    page.navigation_bar
                ],
            ), 
        '/my_page': View(
                "/my_page",
                [
                    logo, 
                    my_page,
                    page.navigation_bar
                ],
            ), 
        '/chat': View(
                "/chat",
                [
                    logo, 
                    Row(controls=[
                        IconButton(
                            icon="ARROW_BACK",
                            icon_size=20, 
                            tooltip="메인으로", 
                            on_click=lambda _: page.go('/my_page')
                        )
                    ]),

                    Text("\n채팅방",weight=FontWeight.BOLD, font_family='나눔바른고딕OTF', size=20),
                    Text("\n"),
                    Row(controls=[
                        Container(
                            Text(" 테스트 채팅방입니다. ", color=colors.WHITE, font_family='나눔바른고딕OTF'), 
                            border_radius=15, 
                            bgcolor=colors.GREEN_ACCENT_700
                        )
                    ]),
                    Row(controls=[
                        Text("　　　　　　　　　　　　　　　　　　　　　　　　　"),
                        Container(
                            Text(" 안녕하세요. ", color="GREEN", font_family='나눔바른고딕OTF'), 
                            border_radius=15, 
                            border = border.all(2, "GREEN"),
                            bgcolor="WHITE", 
                            alignment = alignment.center_right
                        )
                    ]),
                    Row(controls=[
                        Container(
                            Text(" 용병글 보고 연락드립니다! ", color=colors.WHITE, font_family='나눔바른고딕OTF'), 
                            border_radius=15, 
                            bgcolor=colors.GREEN_ACCENT_700
                        )
                    ]),
                    Row(controls=[
                        Text("　　　　　　　　　　　　　　　　　　　　　　　"),
                        Container(
                            Text(" 네 확인해보고\n 승인해드릴게요! ", color=colors.GREEN, font_family='나눔바른고딕OTF'), 
                            border_radius=5, 
                            bgcolor="WHITE",
                            border = border.all(2, "GREEN"), 
                            alignment = alignment.center_right
                        )
                    ]),
                    Row(controls=[
                        Container(
                            Text(" testestsetstet ", color=colors.WHITE, font_family='나눔바른고딕OTF'), 
                            border_radius=30, 
                            bgcolor=colors.GREEN_ACCENT_700
                        )
                    ]),
                    Text("\n\n\n\n\n\n\n\n\n\n"),
                    Row(controls=[
                        TextField(label="채팅을 입력하세요.", prefix_icon="wechat", border_radius=30, width=460)
                    ])
                ],
            ), 
        
    }

    def route_change(route):
        page.views.clear()
        page.views.append(pages[page.route])

    page.on_route_change = route_change
    page.go(page.route)
    page.go('/login')
    fn_tag_search()

if __name__ == '__main__':
    db.init()
    app(target = main, view = AppView.FLET_APP, assets_dir = "assets")
