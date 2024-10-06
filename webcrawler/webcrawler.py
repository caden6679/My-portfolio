"""
File: webcrawler.py
Name: Caden
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.tbody.find_all('td')
        line = 0
        total_man = 0
        total_woman = 0
        for tag in tags:
            line += 1
            if line % 5 == 0:
                total_woman += int(tag.text.replace(',', ''))
            elif line % 5 == 3:
                total_man += int(tag.text.replace(',', ''))
        print(f"Male Number: {total_man}", '\n'f"Female Number: {total_woman}")


if __name__ == '__main__':
    main()
