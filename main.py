from flet import *
from Menu import *


def main(page: Page):
    page.title = "Jobports"

    logo = Image(
            src = f"/잡포츠.png",
            width = 160,
            height = 80,
            fit = ImageFit.CONTAIN,)
    
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

    page.add(logo, tab_menu())
    page.update()


app(target = main, view = AppView.FLET_APP, assets_dir = "home_page")