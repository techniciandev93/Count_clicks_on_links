import requests
from dotenv.main import load_dotenv
from urllib.parse import urlparse
import os


def shorten_link(long_url, headers):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    body = {"long_url": long_url}
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(bitlink, headers):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{strip_scheme(bitlink)}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(bitlink, headers):
    schemaless_url = strip_scheme(bitlink)
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    response = requests.get(url.format(schemaless_url), headers=headers)
    if response.ok:
        return True
    return False


def strip_scheme(url):
    parser_url = urlparse(url)
    schemaless = parser_url.netloc + parser_url.path
    return schemaless


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLY_TOKEN']

    bitlink_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    entered_url = input('Введите ссылку: ')
    if is_bitlink(entered_url, bitlink_headers):
        print(f'По вашей ссылке прошли: {count_clicks(entered_url, bitlink_headers)} раз(а)')
    else:
        print(f'Битлинк: {shorten_link(entered_url, bitlink_headers)}')
