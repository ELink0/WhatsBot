from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
from selenium.common.exceptions import ElementNotVisibleException
import os
import sys
import sched
import threading

import time
import banco

# Configurações Globais
nomeBot = u"\U0001F47B"
destino = 'Luan'
controle = 0

incoming_scheduler = sched.scheduler(time.time, time.sleep)

ultima_msg_enviada = None
ultimo_contato_nome = None

mensagem = 'Teste'

driver = webdriver.Firefox(executable_path="./src/geckodriver", log_path="./src/geckodriver_log.log") 
driver.set_page_load_timeout(60 * 5)
tempoEspera = WebDriverWait(driver, 1000)


def chatConfig():
    print("\n\n\n\t\tIniciando...")
    limpaTerminal = os.system('cls' if os.name == 'nt' else 'clear')
    
    driver.get('https://web.whatsapp.com/')
    print("\t\tEscaneie o QR Code com o app do WhatsApp!")
    time.sleep(10)
    scan_ok = input("Após escanear, aperte enter para continuar")
    print("Continuando...")
    seleciona_chat(destino)
    
    incoming_thread = threading.Thread(target=iniciaChecagemMsgs)
    incoming_thread.start()
    
def iniciaChecagemMsgs():
       # implementar aqui uma função para verificar se tem mensagens novas
       print("Implementar")
        
def seleciona_chat(destino):
    listachats_xpath = '//input[@type="text"]'
    # Vai localizar no HTML a parte que tem o <input type="text">
    # listachats = tempoEspera.until(EC.presence_of_element_located((By.XPATH, listachats_xpath)))
    listachats = driver.find_element_by_class_name('_2S1VP')
    time.sleep(5)
    listachats.send_keys('{}'.format(destino))
    listachats.send_keys(Keys.ENTER)
    print('Contato {} selecionado'.format(destino))
    time.sleep(5)
    enviar_mensagem(mensagem, '')
    
def enviar_mensagem(mensagem, msg=''):
    inputbox = driver.find_element(By.XPATH, '//*[@id="main"]//footer//div[contains(@contenteditable, "true")]')
    inputbox.click()
    time.sleep(2)
    if msg:
    	# Caso seja passado por parãmetro alguma mensagem a mais
    	# Por exemplo:
    	# Bot: Olá
    	# (pula linha)
    	# Msg adicional passada por parâmetro
        inputbox.send_keys(nomeBot + ' : ' + mensagem + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + msg)

    elif mensagem:
    	# Aqui caso não tenha passado nada no parâmetro msg
    	# Vai sair = Bot : Mensagem
        inputbox.send_keys(nomeBot + ' : ' + mensagem)
    else:
        print('falha ao enviar a mensagem')
        return
    inputbox.send_keys(Keys.ENTER)
    print('mensagem enviada')

    tmpmsg_xpath = '//span[@data-icon="msg-time"]'
    tempoEspera.until(EC.invisibility_of_element_located((By.XPATH, tmpmsg_xpath)))
    print('mensagem entregue')
    time.sleep(2)
    


def ContatoAtual():
        global ultimo_contato_nome
        contato_atual = driver.find_element(By.XPATH, '//*[@id="main"]/header//span[contains(@dir, "auto")]').text
        if contato_atual != ultimo_contato_nome:
            ultimo_contato_nome = contato_atual
            print("\n\tContato atual:", contato_atual)
        return contato_atual

def inicio():
    chatConfig()

while controle == 0:
    print("1 - Iniciar bot\n2 - Configurações do bot\n3 - Sair")
    opcao = int(input(" > "))
    
    if opcao == 1:
        limpaTerminal = os.system('cls' if os.name == 'nt' else 'clear')
        inicio()
    elif opcao == 2:
        print("Implementar!!!")
    else:
        break
