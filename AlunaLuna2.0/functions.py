from time import sleep
import pygetwindow
import pyautogui as pag
from proxy import proxy
import keyboard

def image_search(img, click=True, time=5):
    try:
        img_location = pag.locateOnScreen(img, minSearchTime=time , confidence=0.8)
        print(f'IMAGE FOUND: {img}, {img_location}')
        x,y = pag.center(img_location)
        if click: pag.click(x,y)
        return True

    except pag.ImageNotFoundException:
        print(f'IMAGE NOT FOUND: {img}')
        return False

def open_workspace():
    print('\nSTART: Inicializando OPEN_PROXY.\n')
    try:
        janela = pygetwindow.getWindowsWithTitle("ProxyCap Configuration")[0]
        if janela:
            janela.activate()

    except IndexError:
        print('LOG: Janela não estava aberta.')
        Enable = image_search('resources/proxyEnable.png',False,1)
        if Enable == False:
            showMore()
        img = pag.locateOnScreen('resources/proxyEnable.png',1,confidence=0.8)
        for x in range(10):
            x,y = pag.center(img)
            pag.click(x,y,button='RIGHT')
            sleep(0.1)
            if image_search('resources/proxyDesable.png',False,0.1):
                pag.press('up',1,0.3)
                pag.press('enter')
                continue
            pag.press('up',2,0.3)
            if image_search('resources/configProxyOpen.png',False,0.1):
                break
        pag.press('enter')

    if image_search('resources/headler.png',False) == False:
        return False
    print('LOG: Janela aberta com sucesso.')
    return True

def proxy_login():
    print('\nSTART: Inicializando PROXY_LOGIN.\n')

    image_search('resources/NewProxy.png')
    sleep(0.1)
    image_search('resources/proxyAuthenticationOn.png')
    image_search('resources/Hostname.png')
    pag.write(proxy['host'])
    image_search('resources/Port.png')
    pag.write(proxy['port'])
    image_search('resources/username.png')
    pag.write(proxy['username'])
    image_search('resources/password.png')
    pag.write(proxy['password'])

    headler = image_search('resources/headler.png',False,0.3)
    if headler == False:
        pag.press('enter')

def change_proxy():
    print('\nSTART: Inicializando CHANGE_PROXY.\n')

    image_search('resources/userDefautGray.png',time=0.8)
    if image_search('resources/userDefautBlue.png',False):
        print('LOG: Defaut selecionado.')
        image_search('resources/deleteProxy.png')

    else:
        print('WARNING: Não foi possivel encontrar Defaut')
    pag.press('enter')

def showMore():
    keyboard.press_and_release('windows+b') 
    for x in range(20):
        if image_search('resources/showMore.png',False):
            break
        pag.press('left', 1, 0.3)
    pag.press('enter')
