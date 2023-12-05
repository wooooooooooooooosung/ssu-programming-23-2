from flet import *
from Menu import *
import db


def main(page: Page):
    page.title = "Jobports"
    page.window_width = 480
    page.window_height = 800
    page.window_max_width = 480
    page.window_max_height = 800
    page.window_min_width = 480
    page.window_min_height = 800

    logo = Image(
            src = f"/잡포츠.png",
            width = 160,
            height = 80,
            fit = ImageFit.CONTAIN,)
    
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
                    tag_search(),
                    main_page_column(),
                    page.navigation_bar,
                ],
            ),
        '/post_write': View(
                "/post_write",
                [
                    tag_search(),
                    post_wirte_main(),
                    page.navigation_bar,
                ],
            ), 
        '/post_read': View(
                "/post_read",
                [
                    tag_search(),
                    tab_menu(),
                    page.navigation_bar,
                ],
            ), 
        '/my_page': View(
                "/my_page",
                [
                    tag_search(),
                    my_page(),
                    page.navigation_bar,
                ],
            ),
        '/tag_page': View(
                "/tag_page",
                [
                    tag_search(),
                    page.navigation_bar,
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
    app(target = main, view = AppView.FLET_APP, assets_dir = "home_page")


