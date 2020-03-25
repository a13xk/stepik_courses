
import pathlib
import xlrd
import os
import requests
import shutil
from zipfile import ZipFile

calculations_url = "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip"
current_dir = pathlib.Path("/home/alex/Documents/Stepik/course4519")
archive_zip_filename = current_dir.joinpath("archive.zip")
unzipped_dir = current_dir.joinpath("unzipped")

# r = requests.get(url=calculations_url)
# if r.status_code == 200:
#     with open(file=archive_zip_filename, mode="wb") as f:
#         f.write(r.content)

# shutil.rmtree(str(unzipped_dir))
# os.mkdir(str(unzipped_dir))
# with ZipFile(file=str(archive_zip_filename), mode="r") as zip_file:
#     zip_file.extractall(path=str(unzipped_dir))

xlsx_files_paths = sorted(list([xlsx_file for xlsx_file in sorted(unzipped_dir.glob("**/*.xlsx"))]))

total = list()

for xlsx_file in xlsx_files_paths:
    workbook = xlrd.open_workbook(str(xlsx_file))
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])

    employee = dict()
    employee['name'] = sheet.col_values(1)[1]
    employee['salary'] = sheet.col_values(3)[1]
    total.append(employee)

total_sorted = sorted(total, key=lambda x: x.get("name"))

for t in total_sorted:
    print(f"{t.get('name')} {int(t.get('salary'))}")
pass
