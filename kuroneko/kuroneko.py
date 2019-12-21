# coding: utf-8
from __future__ import print_function

import argparse
import re

import requests
import terminaltables
from bs4 import BeautifulSoup


def fetch_data(tracking_codes):
    cleanup = lambda s: "-".join(re.findall(".{1,4}", re.sub("[^0-9]", "", s)))
    codes = [cleanup(code) for code in tracking_codes]
    form_data = {"number{:02d}".format(i + 1): code for i, code in enumerate(codes)}
    form_data["number00"] = 1
    r = requests.post("https://toi.kuronekoyamato.co.jp/cgi-bin/tneko", form_data)
    soup = BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all("table", class_="meisai")
    return codes, tables


def parse_table(table):
    headers = [th.get_text() for th in table.find_all("tr")[0].find_all("th")]
    headers[0] = "#"
    lines = []
    for i, row in enumerate(table.find_all("tr")[1:]):
        line = [cell.get_text() for cell in row.find_all("td")]
        line[0] = i
        lines.append(line)
    return headers, lines


def main():
    parser = argparse.ArgumentParser(description="Get delivery status of takyubin package")
    parser.add_argument("tracking_codes", nargs="+", action="store", type=str,
                        help="Tracking codes")
    parser.add_argument("--ascii", action="store_true",
                        help="Print using ASCII characters only")
    args = parser.parse_args()

    codes, tables = fetch_data(args.tracking_codes)
    for i, (code, table) in enumerate(zip(codes, tables)):
        headers, lines = parse_table(table)
        print("{:d}件目 {}".format(i + 1, code))
        if args.ascii:
            print(terminaltables.AsciiTable([headers] + lines).table, end="\n\n")
        else:
            print(terminaltables.SingleTable([headers] + lines).table, end="\n\n")