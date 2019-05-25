import socket
from contextlib import closing


def test_text_is_show(driver):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex(('localhost', 5000)) == 0:
            driver.get('http://localhost:5000/views/sample')
            assert 'Welcome to Your Vue.js App' in driver.page_source
