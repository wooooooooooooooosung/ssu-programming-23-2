from flet import *
from T_Menu.menu_tab1 import *
from T_Menu.menu_tab2 import *
from T_Menu.menu_tab3 import *
from T_Menu.menu_tab4 import *
from T_Menu.menu_tab5 import *
from T_Menu.menu_tab6 import *
from T_Menu.menu_tab_jopports import *

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

    return total_menu
