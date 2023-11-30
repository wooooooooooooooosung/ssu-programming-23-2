from flet import *
from Menu import *


def main(page: Page):
    page.title = "Jobports"
<<<<<<< HEAD
    page.window_width = 480
    page.window_height = 800
=======
<<<<<<< HEAD
    page.window_width = 480
    page.window_height = 800
=======
<<<<<<< HEAD
    page.window_width = 480
    page.window_height = 800
=======

>>>>>>> f981f4eba74a823f44575e275ef8f826b2634121
>>>>>>> cd361d3f67c9f3a6aa401f5747a538bf056b1434
>>>>>>> fdc43fdbe42b30d37db101fba99d4b7e29cee5de
    logo = Image(
            src = f"/잡포츠.png",
            width = 160,
            height = 80,
            fit = ImageFit.CONTAIN,)
    
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> cd361d3f67c9f3a6aa401f5747a538bf056b1434
>>>>>>> fdc43fdbe42b30d37db101fba99d4b7e29cee5de
    def change_page(e):
        my_index = e.control.selected_index

        if my_index == 0:
            page.go('/')
        elif my_index == 1:
            page.go('/post_write')
        elif my_index == 2:
            page.go('/post_read')
        elif my_index == 3:
            page.go('/my_page')

    page.navigation_bar = NavigationBar(
        bgcolor = "black",
        on_change = change_page,
        selected_index = 0,
        destinations = [
            NavigationDestination(icon = icons.HOME_ROUNDED, label="메인 페이지"),
            NavigationDestination(icon = icons.POST_ADD_ROUNDED, label="게시글 작성"),
            NavigationDestination(icon = icons.REMOVE_RED_EYE_ROUNDED, label = "게시글 보기"),
            NavigationDestination(icon = icons.TAG_FACES_SHARP, label = "마이 페이지"),
        ]
    )

    pages = {
        '/': View(
                "/",
                [
                    logo,
                    menujopports_content(),
                    page.navigation_bar,
                ],
            ),
        '/post_write': View(
                "/post_write",
                [
                    logo,
                    post_wirte_main(),
                    page.navigation_bar,
                ],
            ), 
        '/post_read': View(
                "/post_read",
                [
                    logo,
                    tab_menu(),
                    page.navigation_bar,
                ],
            ), 
        '/my_page': View(
                "/my_page",
                [
                    logo,
                    page.navigation_bar,
                ],
            ), 
    }
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
    page.navigation_bar = NavigationBar(
        destinations = [
            NavigationDestination(icon = icons.EXPLORE, label="Explore"),
            NavigationDestination(icon = icons.COMMUTE, label="Commute"),
            NavigationDestination(
                icon=icons.BOOKMARK_BORDER,
                selected_icon = icons.BOOKMARK,
                label = "Explore",
            ),
        ]
    )
>>>>>>> f981f4eba74a823f44575e275ef8f826b2634121
>>>>>>> cd361d3f67c9f3a6aa401f5747a538bf056b1434
>>>>>>> fdc43fdbe42b30d37db101fba99d4b7e29cee5de

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> cd361d3f67c9f3a6aa401f5747a538bf056b1434
>>>>>>> fdc43fdbe42b30d37db101fba99d4b7e29cee5de
    
    page.on_route_change = route_change
    page.go(page.route)

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> f981f4eba74a823f44575e275ef8f826b2634121
>>>>>>> cd361d3f67c9f3a6aa401f5747a538bf056b1434
>>>>>>> fdc43fdbe42b30d37db101fba99d4b7e29cee5de

app(target = main, view = AppView.FLET_APP, assets_dir = "home_page")