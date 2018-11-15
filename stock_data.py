# pylint: disable=E1101
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

base_url = "https://finviz.com/quote.ashx?t="
finviz_table_class =  "snapshot-table2"

class Stock_Data:
    def __init__(self, symbol):
        self.symbol = symbol
        self.finviz_url = base_url + symbol
        self.finviz_stock_html = BeautifulSoup(self.get_finviz_data(), 'html.parser')
        self.finviz_table_data = self.get_tab_data(finviz_table_class)

    def get_finviz_data(self):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(self.finviz_url, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content #pylint places warning error E1101 on this line, states resp has no member resp
                else:
                    return None

        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(self.finviz_url, str(e)))
            return None


    def is_good_response(self, resp):
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

    def get_tab_data(self, tab_class):
        tab = self.finviz_stock_html.find("table",{"class":tab_class})
        tab_dict = {}
        for row in tab.findAll('tr'):
            td_keys = row.findAll('td', {"class":"snapshot-td2-cp"})
            td_vals = row.findAll('td', {"class":"snapshot-td2"})                  
            if(len(td_keys) == len(td_vals)):
                for i in range(len(td_keys)):
                    tab_dict[td_keys[i].get_text()] = td_vals[i].get_text()
        return tab_dict

    