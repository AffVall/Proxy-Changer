import functions as f
from proxy import randomize_proxy

if __name__ == '__main__': 
    window_proxy = f.open_workspace()
    if window_proxy == True:
        randomize_proxy()
        f.proxy_login()
        f.change_proxy()
    else:
        print('ERRO: ops, algo deu errado')
