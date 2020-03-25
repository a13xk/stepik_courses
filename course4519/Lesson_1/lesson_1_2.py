import requests
from bs4 import BeautifulSoup

u = "https://stepik.org/media/attachments/lesson/209719/2.html"

r = requests.get(url=u)

text = r.text
soup = BeautifulSoup(text, "html.parser")

code_tags = soup.find_all(name="code")
code_tag_texts = list()
for code_tag in code_tags:
    code_tag_texts.append(code_tag.text)
text_frequency = dict()
for t in code_tag_texts:
    if not text_frequency.get(t):
        text_frequency[t] = 1
    else:
        text_frequency[t] = text_frequency[t] + 1
text_frequency_sorted = sorted(text_frequency.items(), key=lambda x: x[1], reverse=True)
res_list = list()
for t in text_frequency_sorted:
    if t[1] > 3:
        res_list.append(t[0])
res_list_sorted = sorted(res_list)

res_str = " ".join(res_list)
res_str_sorted = " ".join(res_list_sorted)
pass


