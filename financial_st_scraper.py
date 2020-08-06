## Use this for scaraping a single symbol

import os
import numpy as np
import pandas as pd
import requests
from lxml import html
from fake_headers import Headers

symbol = 'RELIANCE'

def scrape():
    # Scraping Cash Flow
    def cash_flow():
        url_cf = f'https://in.finance.yahoo.com/quote/{symbol}.NS/cash-flow?p={symbol}.NS'
        # Fetch the page that we're going to parse, using the request headers
        # defined above
        page = requests.get(url_cf, headers=sp_headers())

        # Parse the page with LXML, so that we can start doing some XPATH queries
        # to extract the data that we want
        tree = html.fromstring(page.content)

        # Smoke test that we fetched the page by fetching and displaying the H1 element
        y_axis = tree.xpath("//h1/text()")
        print(y_axis)

        table_rows = tree.xpath("//div[contains(@class, 'D(tbr)')]")

        # Ensure that some table rows are found; if none are found, then it's possible
        # that Yahoo Finance has changed their page layout, or have detected
        # that you're scraping the page.
        assert len(table_rows) > 0

        parsed_rows = []

        for table_row in table_rows:
            parsed_row = []
            el = table_row.xpath("./div")

            none_count = 0

            for rs in el:
                try:
                    (text,) = rs.xpath('.//span/text()[1]')
                    parsed_row.append(text)
                except ValueError:
                    parsed_row.append(np.NaN)
                    none_count += 1

            if (none_count < 4):
                parsed_rows.append(parsed_row)

        df = pd.DataFrame(parsed_rows)
        df

        path = f'/Users/mohitsingh/Desktop/GSheetConnect/Companies/{symbol}'
        sheet_name = str(f'cash_flow_{symbol}.xlsx')
        writer = pd.ExcelWriter(sheet_name)
        writer = os.path.join(path, writer)
        df.to_excel(writer)

    cash_flow()

    def income_statement():
        url_is = f'https://in.finance.yahoo.com/quote/{symbol}.NS/financials?p={symbol}.NS'
        # Fetch the page that we're going to parse, using the request headers
        # defined above
        page = requests.get(url_is, headers=sp_headers())

        # Parse the page with LXML, so that we can start doing some XPATH queries
        # to extract the data that we want
        tree = html.fromstring(page.content)

        # Smoke test that we fetched the page by fetching and displaying the H1 element
        y_axis = tree.xpath("//h1/text()")
        print(y_axis)

        table_rows = tree.xpath("//div[contains(@class, 'D(tbr)')]")

        # Ensure that some table rows are found; if none are found, then it's possible
        # that Yahoo Finance has changed their page layout, or have detected
        # that you're scraping the page.
        assert len(table_rows) > 0

        parsed_rows = []

        for table_row in table_rows:
            parsed_row = []
            el = table_row.xpath("./div")

            none_count = 0

            for rs in el:
                try:
                    (text,) = rs.xpath('.//span/text()[1]')
                    parsed_row.append(text)
                except ValueError:
                    parsed_row.append(np.NaN)
                    none_count += 1

            if (none_count < 4):
                parsed_rows.append(parsed_row)

        df = pd.DataFrame(parsed_rows)
        df

        path = f'/Users/mohitsingh/Desktop/GSheetConnect/Companies/{symbol}'
        sheet_name = str(f'income_statement_{symbol}.xlsx')
        writer = pd.ExcelWriter(sheet_name)
        writer = os.path.join(path, writer)
        df.to_excel(writer)

    income_statement()

    def balance_sheet():
        url_bs = f'https://in.finance.yahoo.com/quote/{symbol}.NS/balance-sheet?p={symbol}.NS'
        # Fetch the page that we're going to parse, using the request headers
        # defined above
        page = requests.get(url_bs, headers=sp_headers())

        # Parse the page with LXML, so that we can start doing some XPATH queries
        # to extract the data that we want
        tree = html.fromstring(page.content)

        # Smoke test that we fetched the page by fetching and displaying the H1 element
        y_axis = tree.xpath("//h1/text()")
        print(y_axis)

        table_rows = tree.xpath("//div[contains(@class, 'D(tbr)')]")

        # Ensure that some table rows are found; if none are found, then it's possible
        # that Yahoo Finance has changed their page layout, or have detected
        # that you're scraping the page.
        assert len(table_rows) > 0

        parsed_rows = []

        for table_row in table_rows:
            parsed_row = []
            el = table_row.xpath("./div")

            none_count = 0

            for rs in el:
                try:
                    (text,) = rs.xpath('.//span/text()[1]')
                    parsed_row.append(text)
                except ValueError:
                    parsed_row.append(np.NaN)
                    none_count += 1

            if (none_count < 4):
                parsed_rows.append(parsed_row)

        df = pd.DataFrame(parsed_rows)
        df

        path = f'/Users/mohitsingh/Desktop/GSheetConnect/Companies/{symbol}'
        sheet_name = str(f'balance_sheet_{symbol}.xlsx')
        writer = pd.ExcelWriter(sheet_name)
        writer = os.path.join(path, writer)
        df.to_excel(writer)

    balance_sheet()

scrape()
