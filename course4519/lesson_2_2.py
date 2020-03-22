import xlrd

workbook = xlrd.open_workbook('salaries.xlsx')
sheet_names = workbook.sheet_names()
sheet = workbook.sheet_by_name(sheet_names[0])

job_titles = sheet.row_values(0)[1:8]

cities = list()

for row in range(1, 9):
    salary = dict()
    salary['city'] = sheet.row_values(row)[0]
    salary['values'] = sheet.row_values(row)[1:8]
    salary['title_and_salary'] = list(zip(job_titles, salary['values']))
    salary['title_by_salary'] = sorted(salary['title_and_salary'], key=lambda tup: tup[1])
    salary['highest_median'] = salary['title_by_salary'][3]
    cities.append(salary)

max_highest_salary_city = dict()
max_highest_salary_city['highest_median'] = 0.0
for city in cities:
    if city.get("highest_median")[1] > max_highest_salary_city.get("highest_median"):
        max_highest_salary_city['highest_median'] = city.get("highest_median")[1]
        max_highest_salary_city['job_title'] = city.get("highest_median")[0]
        max_highest_salary_city['city'] = city.get("city")

print(f"""Регион с самой высокой медианной зарплатой:
{max_highest_salary_city.get("city")}, {max_highest_salary_city.get("job_title")}, {max_highest_salary_city.get("highest_median")} 
""")

jobs_all_cities = list()
for column in range(1, 8):
    salary = dict()
    salary['job_title'] = job_titles[column-1]
    salary['values'] = sheet.col_values(column)[1:9]
    salary['highest_mean'] = sum(salary.get("values"))/len(salary.get("values"))
    jobs_all_cities.append(salary)

max_highest_salary_job_title = dict()
max_highest_salary_job_title['highest_mean'] = 0.0
for job in jobs_all_cities:
    if job.get("highest_mean") > max_highest_salary_job_title.get("highest_mean"):
        max_highest_salary_job_title["highest_mean"] = job.get("highest_mean")
        max_highest_salary_job_title["job_title"] = job.get("job_title")
print(f"""Название профессии с самой высокой средней зарплатой по всем регионам:
{max_highest_salary_job_title.get("job_title")}, {max_highest_salary_job_title.get("highest_mean")}
""")
