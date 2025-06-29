
from random import randint
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

proxy = {
    'host' : config['proxy']['host'],
    'port' : config['proxy']['port'],
    'username' : config['proxy']['username'],
    'password' : config['proxy']['password'],
}


def proxy_sort():
    counter=0
    with open('proxys.txt', 'r', ) as text:
        for line in text:
            counter += 1
        return randint(1,counter)

def search_proxy(random_proxy):
    counter=0
    with open('proxys.txt', '+rt') as text:
        for line in text:
            counter +=1
            if counter == random_proxy:
                proxy_list = line.split(':')
                break
    counter=0
    for lib in proxy:
        proxy[lib] = proxy_list[counter]
        counter += 1

def randomize_proxy():
    if config['geral']['Randomize_Proxy'] == 'True':
        random_proxy = proxy_sort()
        search_proxy(random_proxy)
        print('\nProxy em uso:')
        for x in proxy.values():
            print(x)
