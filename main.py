from zillowbot import ZillowBot

zillow_url = "https://www.zillow.com/bellevue-wa/apartments/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.24806196887002%2C%22east%22%3A-122.1872366192234%2C%22south%22%3A47.599669722699915%2C%22north%22%3A47.634046533916134%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3619%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A15%7D"
output_fname = "listings.xlsx"


def export_to_excel(df):
    df.to_excel(output_fname, encoding="utf-8", sheet_name="listings",
                index=False)
    print(f"Excel file created: {output_fname}")


def main():
    zbot = ZillowBot(zillow_url)
    df = zbot.scrape_all_pages()
    export_to_excel(df)
    zbot.quit()


if __name__ == "__main__":
    main()
