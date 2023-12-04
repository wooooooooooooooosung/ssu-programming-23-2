
from flet import *

def menujopports_content():
    data_table_frame = DataTable(
            columns=[
                DataColumn(Text("First name")),
                DataColumn(Text("Last name")),
                DataColumn(Text("Age"), numeric=True),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text("John")),
                        DataCell(Text("Smith")),
                        DataCell(Text("43")),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(Text("Jack")),
                        DataCell(Text("Brown")),
                        DataCell(Text("19")),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(Text("Alice")),
                        DataCell(Text("Wong")),
                        DataCell(Text("25")),
                    ],
                ),
            ],
        )
    return data_table_frame


def mainpage_banner():
    page_banner = Image(
            src = f"/soccer.png",
            width = 480,
            height = 250,
            fit = ImageFit.CONTAIN)
    
    return page_banner