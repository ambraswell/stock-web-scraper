# pylint: disable=E1101
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content #pylint places warning error E1101 on this line, states resp has no member resp
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_tab_data(tab_class):
    tab = html.find("table",{"class":tab_class})
    tab_dict = {}
    for row in tab.findAll('tr'):
        td_keys = row.findAll('td', {"class":"snapshot-td2-cp"})
        td_vals = row.findAll('td', {"class":"snapshot-td2"})                  
        if(len(td_keys) == len(td_vals)):
            for i in range(len(td_keys)):
                tab_dict[td_keys[i].get_text()] = td_vals[i].get_text()
    return tab_dict

stocks = ["GE"]
base_url = "https://finviz.com/quote.ashx?t="

stocklist_data = []
for stock in stocks:
    print(stock)
    raw_html = simple_get(base_url + stock)
    html = BeautifulSoup(raw_html, 'html.parser')
    tab_class =  "snapshot-table2"    
    tab_dict = get_tab_data(tab_class)
    stocklist_data.append(tab_dict)
for stock in stocklist_data:
    for k,v in stock.items():
        print(k,v)
    


