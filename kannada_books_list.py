from bs4 import BeautifulSoup
import requests
import pandas

#url
req = requests.get("https://www.goodreads.com/list/show/24308.Best_Kannada_Novels")
content = req.content
soup = BeautifulSoup(content, "html.parser")
#print(soup.prettify())

all = soup.find_all("div",id ="all_votes")
#print(all)
list_of_books = []
for item in all:
    a = len(item.find_all("span", itemprop ="name", role ="heading"))
    for i in range (1,a):
        dict = {}
        title_unprocessed = item.find_all("span", itemprop ="name", role ="heading")[i].text
        if "|" in title_unprocessed:
            dict["Title"] = title_unprocessed.split("|")[1]
        elif "[" in title_unprocessed:
            dict["Title"] = title_unprocessed.split("[")[1].replace("]", "")
        else:
            dict["Title"] = title_unprocessed
        dict["Author"] = item.find_all("a", {"class":"authorName"})[i].text
        dict["Rating"]=item.find_all("span", {"class": "greyText smallText uitext"})[i].text.replace("\n", "").split()[0]
        dict["Score"] =item.find_all("span", {"class": "smallText uitext"})[i].text.split()[1]
        list_of_books.append(dict)
    print(list_of_books)

df = pandas.DataFrame(list_of_books)
print(df)
df.to_csv("KannadaBooks.csv")
