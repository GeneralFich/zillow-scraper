import pandas as pd
import time

from pandas.core.frame import DataFrame
from bot import Bot


class ZillowBot(Bot):

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.driver.get(url)

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url
        print("URL set to ZillowBot successfully.")

    @url.deleter
    def url(self):
        del self._url

    def get_url_elements(self) -> list:
        """Returns a list of WebElements with a href attribute that represents 
        the URL of a property listing."""
        return self.driver.find_elements_by_xpath(
            "//div[contains(@class,'list-card-info')]"
            "/a[contains(@class,'list-card-link')]")

    def get_price_elements(self) -> list:
        return self.driver.find_elements_by_xpath(
            "//div[contains(@class,'list-card-heading')]"
            "/div[contains(@class,'list-card-price')]")

    def get_address_elements(self) -> list:
        return self.driver.find_elements_by_class_name("list-card-addr")

    def get_pagenum_elements(self) -> list:
        return self.driver.find_elements_by_class_name("ekGcXR")

    def scroll_down(self) -> None:
        eles = self.get_url_elements()
        n_eles = len(eles)
        while True:
            eles[-1].location_once_scrolled_into_view
            time.sleep(1)
            eles = self.get_url_elements()
            if n_eles == len(eles):
                break
            else:
                n_eles = len(eles)

    def scrape_current_page(self) -> pd.DataFrame:
        self.scroll_down()

        # Extract the href links from the elements.
        time.sleep(0.5)
        urls = [e.get_attribute("href") for e in self.get_url_elements()]
        print(f"{len(urls)} urls found.")

        # Get the matching list of prices.
        eles = self.get_price_elements()
        prices = []
        for ele in eles:
            p_list = []
            for char in ele.text:
                p_list.append(char) if char.isnumeric() else ""
                if char not in "$,0123456789":
                    break
            price = "".join(p_list)
            prices.append(int(price))
        print(f"{len(prices)} prices found.")

        # Get the matching list of addresses.
        eles = self.get_address_elements()
        addresses = [e.text for e in eles]
        print(f"{len(addresses)} addresses found.")

        # Combine the data into a dataframe and return it.
        return pd.DataFrame({"Address": addresses, "Price": prices, "URL": urls})

    def scrape_all_pages(self):
        pagenum_eles = self.get_pagenum_elements()
        n_pages = len(pagenum_eles)
        print(f"There are {n_pages} pages.")

        dfs = []
        for pagenum in range(n_pages):
            df = self.scrape_current_page()
            dfs.append(df)
            if pagenum < n_pages-1:
                page_turner = self.get_pagenum_elements()[pagenum+1]
                page_turner.click()  # Go to the next page.

        return pd.concat(dfs)
