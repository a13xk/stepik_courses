import requests
from bs4 import BeautifulSoup

page_url1 = "https://stepik.org/media/attachments/lesson/209723/3.html"
page_url2 = "https://stepik.org/media/attachments/lesson/209723/4.html"
page_url3 = "https://stepik.org/media/attachments/lesson/209723/5.html"

# r = requests.get(url=page_url1)
r = requests.get(url=page_url3)
if r.status_code == 200:
    html_text = r.text

    soup = BeautifulSoup(html_text, "html.parser")
    td_tags = soup.find_all(name="td")
    numbers = list()
    for td in td_tags:
        n = int(td.string.strip())
        numbers.append(n)
    the_sum = sum(numbers)
    print(f"The sum of all numbers in table: {the_sum}")
else:
    print(f"Failed to get '{page_url1}")
