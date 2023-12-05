import db
from flet import *

def menu3_text():
    text = ' 농구 '
    return text

def menu3_content():
    list = db.executeQuery("SELECT * FROM post WHERE sID = 2")
    cmp = Column(controls=[])

    def button_clicked(e):
        print(e.control.tooltip)

    for i in range(len(list)):
        cmp.controls.append(
            Column([
                Image(
                    src = f"/tab2.jpg",
                    width = 480,
                    height = 250,
                    fit = ImageFit.CONTAIN
                ), 
                Row(controls=[
                    Text(
                        list[i][1], text_align=TextAlign.LEFT, width=235, weight=FontWeight.BOLD, font_family='나눔바른고딕OTF'
                    ),
                    Icon(name="REMOVE_RED_EYE", color="#c1c1c1"),  
                    Text(list[i][5], width=30, weight=FontWeight.BOLD, bgcolor="white", font_family='나눔바른고딕OTF'), 
                    ElevatedButton(text="게시물 보기", on_click=button_clicked, tooltip=list[i][1])
                ]), 
                Row()
            ], 
            alignment = MainAxisAlignment.START),
        )

    content = Column(
        [ cmp ],         
        alignment = alignment.center, 
        scroll = ScrollMode.AUTO
    )

    return content