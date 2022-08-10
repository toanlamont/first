import requests
from bs4 import BeautifulSoup


results = []
r = requests.get("http://ketqua1.net")
tree = BeautifulSoup(markup=r.text, features="html.parser")
nodes = tree.find_all(name="td", attrs={"class": "chu17"})

for node in nodes:
    results.append(node.text)
def check(num):
    if str(num) in results:
        return 'Chúc mừng, bạn đã trúng lô'
    else:
        return "Bạn đã trượt lô, chúc bạn mm lần sau"
print(check(19))
print(results)