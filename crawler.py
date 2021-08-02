import bs4 as bs
import grequests
from collections import defaultdict
import logging

LINK_PATTERN = 'https://'
json_file = defaultdict(list)


def get_all_urls(url_to_get):
    response = []
    try:
        page = grequests.get(url_to_get)
        response = grequests.map([page], size=20)
    except AttributeError:
        logging.info("Can't collect `recipes_links")

    soup = [bs.BeautifulSoup(res.text, 'html.parser') for res in response]

    all_links = [link.get('href') for link in soup[0].find_all('a') if
                 str(link.get('href')).startswith(LINK_PATTERN)]
    return set(all_links)


if __name__ == '__main__':
    url_link = input("Enter url to scrape: ")
    result = get_all_urls(url_link)

    for r in result:
        print(r)
