import requests
import pysftp

def get_from_api(method, url):
    return requests.request(method, url, timeout=5).json()

def get_from_sftp(hostname, username, pwd, port, filename):
    with pysftp.Connection(host=hostname, username=username, password=pwd, port=port) as sftp:
        sftp.get(filename)

def put_into_server(hostname, username, pwd, port, filename):
    with pysftp.Connection(host=hostname, username=username, password=pwd, port=port) as sftp:
        sftp.put(filename)