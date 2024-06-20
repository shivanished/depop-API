import os
from dotenv import load_dotenv
load_dotenv()
import requests
from rich import print
import http.client
import json


def get_search_results(load_number=None):
    # API URL
    url = "https://depop-thrift.p.rapidapi.com/getSearch"

    params = {
        "page":1,
        "keyword":"vintage hoodie",
        # "categoryId":str,
        # "countryCode":str,
        "sortBy":"priceAscending",
        "colors":"black,gray,green",
        "conditions":"brand_new,used_like_new,used_excellent",
        # "brands":str,
        # "sizes":str,
        # "priceMin":int,
        "priceMax":"100"
    }

    headers = {
        "x-rapidapi-key": "b55582bacemsh0b6a447b36192a9p150c55jsn2512ee1c5436",
        "x-rapidapi-host": "depop-thrift.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()


if __name__ == '__main__':
    response = get_search_results()
    print(response)