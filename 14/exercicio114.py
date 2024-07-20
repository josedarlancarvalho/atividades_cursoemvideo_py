import urllib.request

try:
    site = urllib.request.urlopen('http://www.youtube.com')
except urllib.error.URLError:
    print(f'Deu erro:')
else:
    print('Tudo certo.')
