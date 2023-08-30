import json
import requests
from dotenv.main import load_dotenv
from urllib.parse import urlparse
import os


def send_request(url, method, headers=None, body=None):
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, headers=headers, data=json.dumps(body))
    else:
        raise ValueError("Неподдерживаемый метод запроса. Поддерживаются только 'GET' и 'POST'.")
    response.raise_for_status()
    return response


def shorten_link(long_url, headers):
    send_request(long_url, method='GET')
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    body = {"long_url": long_url}
    response = send_request(url, 'POST', headers=headers, body=body)
    return response.json()['id']


def count_clicks(bitlink, headers):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{strip_scheme(bitlink)}/clicks/summary'
    response = send_request(url, method='GET', headers=headers)
    return response.json()['total_clicks']


def is_bitlink(bitlink, headers):
    try:
        schemaless_url = strip_scheme(bitlink)
        url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
        send_request(url.format(schemaless_url), method='GET', headers=headers)
        return True
    except requests.HTTPError:
        return False


def strip_scheme(url):
    schemaless = urlparse(url)._replace(scheme='').geturl()
    return schemaless[2:] if schemaless.startswith("//") else schemaless


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.environ['TOKEN']

    bitlink_headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    entered_url = input('Введите ссылку: ')
    if is_bitlink(entered_url, bitlink_headers):
        print(f'По вашей ссылке прошли: {count_clicks(entered_url, bitlink_headers)} раз(а)')
    else:
        print(f'Битлинк: {shorten_link(entered_url, bitlink_headers)}')
