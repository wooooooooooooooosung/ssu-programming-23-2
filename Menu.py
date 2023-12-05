from flet import *
from T_Menu.menu_tab1 import *
from T_Menu.menu_tab2 import *
from T_Menu.menu_tab3 import *
from T_Menu.menu_tab4 import *
from T_Menu.menu_tab5 import *
from T_Menu.menu_tab6 import *
from T_Menu.menu_tab_jopports import *
from T_Menu.my_page import *
from T_Menu.tag_search import *

def tab_menu():
    
    total_menu = Tabs( animation_duration = 0,
        tabs=[
        Tab(
               text = menu2_text(),
               content = menu2_content(),
        ),
        Tab(
               text = menu3_text(),
               content = menu3_content(),
        ),
        Tab(
               text = menu4_text(),
               content = menu4_content(),
        ),
        Tab(
               text = menu5_text(),
               content = menu5_content(),
        ),
        Tab(
               text = menu6_text(),
               content = menu6_content(),
        ),
        ],
            expand = 1
        )

    total_column = Column(
            controls=[
                Row(alignment = alignment.center, width = 480, controls=[Text("게시물 보기", size=30, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF')]),
                total_menu])
    return total_column
