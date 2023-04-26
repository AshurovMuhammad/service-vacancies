import requests
from bs4 import BeautifulSoup
from random import randint

__all__ = ('hh', 'superjob')

# url = "https://hh.uz/search/vacancy?text=python&salary=&area=2759&ored_clusters=true"
url = "https://www.superjob.ru/vacancy/search/?keywords=Python"

headers = [{
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
},
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134   Safari/537.36 OPR/89.0.4447.71',
        'Accept': '*/*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
]


def hh(url):
    resp = requests.get(url, headers=headers[randint(0, 2)])
    jobs = []
    errors = []
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        main_div = soup.find("main", class_="vacancy-serp-content")
        if main_div:
            div_lst = main_div.find_all('div', class_="serp-item")
            for div in div_lst:
                title = div.find('h3').text
                href = div.find('h3').a['href']
                content = div.find_all('div', class_='vacancy-serp-item__info')
                if len(content) > 1:
                    content = content[1].text
                else:
                    content = "Tasnif mavjud emas"

                comp = div.find('div', class_="vacancy-serp-item__meta-info-company").find("a")
                if comp:
                    company = comp.text
                else:
                    company = "Kompaniya xaqida ma'lumot mavjud emas"
                jobs.append({'title': title, 'url': href, 'description': content, 'company': company})
            else:
                errors.append({'url': url, 'title': "Xatolik paydo bo'ldi, belgilash o'zgartirilgan"})
    else:
        errors.append({'url': url, 'title': "Sahifa topilmadi"})

    return jobs, errors


def superjob(url):
    resp = requests.get(url, headers=headers[randint(0, 2)])
    jobs = []
    errors = []
    domain = "https://www.superjob.ru"
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        main_div = soup.find("div", class_="_3VMkc")
        title = None
        href = None
        content = None
        company = None
        if main_div:
            div_lst = main_div.find_all('div', class_="f-test-search-result-item")
            for div in div_lst:
                tit = div.find('div', class_='qs65P')
                if tit:
                    title = tit.find("a").text
                    href = tit.find("a").get("href")
                con = div.find('span', class_="RRZVI _3UZoC _3zdq9 _3iH_l _3u9kN")
                if con:
                    content = con.text
                comp = div.find('span',
                                "_3nMqD f-test-text-vacancy-item-company-name _2Ut4L _3UZoC _3zdq9 _3iH_l _3u9kN")
                if comp:
                    company_link = comp.find("a")
                    if company_link:
                        company = company_link.text

                jobs.append({'title': title, 'url': domain + href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': "Xatolik paydo bo'ldi, belgilash o'zgartirilgan"})
    else:
        errors.append({'url': url, 'title': "Sahifa topilmadi"})

    return jobs, errors


if __name__ == '__main__':
    jobs, errors = superjob(url)
    h = open("work.json", "w", encoding='utf-8')
    h.write(str(jobs))
    h.close()
