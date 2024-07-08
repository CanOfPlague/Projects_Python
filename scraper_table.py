import requests
from bs4 import BeautifulSoup as bs

def main():
    print("Entern url: ") 
    url = input()
    response = requests.get(url)

    soup = bs(response.content, "html.parser")

    data = []
    table = soup.find('table')
    table_body = table.find('tbody')

    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [element.text.strip() for element in cols]
        data.append([element for element in cols if element])
    print()

if __name__ == "__main__":
    main()