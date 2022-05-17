from logging import error
from os import environ
from dotenv import load_dotenv
from requests import get

CONFIG_FILE_URL = environ.get('CONFIG_FILE_URL')
try:
    if len(CONFIG_FILE_URL) == 0:
        raise TypeError
    try:
        res = get(CONFIG_FILE_URL)
        if res.status_code == 200:
            with open('confi.env', 'wb+') as f:
                f.write(res.content)
        else:
            error(f'Failed to download config.env {res.status_code}')
    except Exception as err:
        error(f'CONFIG_FILE_URL: {err}')
except:
    pass
load_dotenv('config.env', override=True)
