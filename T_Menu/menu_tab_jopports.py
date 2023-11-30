import db
from flet import *

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> cd361d3f67c9f3a6aa401f5747a538bf056b1434
>>>>>>> fdc43fdbe42b30d37db101fba99d4b7e29cee5de
def menujopports_content():
    main_banner = Image(
            src = f"/soccer.png",
            width = 480,
            height = 250,
            fit = ImageFit.CONTAIN)

<<<<<<< HEAD
    return main_banner
=======
<<<<<<< HEAD
    return main_banner
=======
    return main_banner
=======
def menujopports_text():
    text = 'HOME'
    return text

def menujopports_content():
    main_banner = Image(
            src = f"/soccer.png",
            width = 500,
            height = 250,
            fit = ImageFit.CONTAIN)
    
    top_rank = DataTable(
            columns=[
                DataColumn(Text("순위")),
                DataColumn(Text("이름")),
                DataColumn(Text("종목"), numeric=True),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text("1")),
                        DataCell(Text("Smith")),
                        DataCell(Text("농구")),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(Text("2")),
                        DataCell(Text("Brown")),
                        DataCell(Text("축구")),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(Text("3")),
                        DataCell(Text("Wong")),
                        DataCell(Text("야구")),
                    ],
                ),
            ],
        )

    return top_rank

def data_btn_next():

    return ElevatedButton(text = "다음", width = 200, height = 100,)

def data_btn_back():
    
    return ElevatedButton(text = "이전", width = 200, height = 100,)
>>>>>>> f981f4eba74a823f44575e275ef8f826b2634121
>>>>>>> cd361d3f67c9f3a6aa401f5747a538bf056b1434
>>>>>>> fdc43fdbe42b30d37db101fba99d4b7e29cee5de
