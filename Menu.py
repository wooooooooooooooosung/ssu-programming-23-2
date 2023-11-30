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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
               text = menujopports_text(),
               content = menujopports_content(),
        ),
        Tab(
               text = menu1_text(),
               content = menu1_content(),
        ),
        Tab(
>>>>>>> f981f4eba74a823f44575e275ef8f826b2634121
>>>>>>> cd361d3f67c9f3a6aa401f5747a538bf056b1434
>>>>>>> fdc43fdbe42b30d37db101fba99d4b7e29cee5de
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
