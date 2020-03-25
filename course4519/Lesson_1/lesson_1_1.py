import requests

u = "https://stepik.org/media/attachments/lesson/209717/1.html"

r = requests.get(url=u)

text = r.text

