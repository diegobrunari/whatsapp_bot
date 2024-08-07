from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")

time.sleep(20) # Para Logar no WhatsApp pelo QR CODE

####### A partir daqui, o web whats está conectado ######
mensagem = '''
Teste de AUTOMAÇÃO
WhatsApp Web
'''

lista_contatos = ["jonas", "jotape", "kiko", "teste", "eu mais", "mais um eu"]

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys("aluguel atrasado")
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)
# Enviar a msg. Caso tenha emoji, é necessário usar o PyperClip. Em mensagens simples, não há necessidade
pyperclip.copy(mensagem)
time.sleep(2)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + 'V')
time.sleep(2)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)

# Tamanho da lista de contatos para lógica de envio de 5 em 5
qtd_contatos = len(lista_contatos)
if qtd_contatos % 5 == 0:
    qtd_blocos = int(qtd_contatos / 5)
else:
    qtd_blocos = int(qtd_contatos / 5) + 1

for i in range(qtd_blocos):
    # Lógica de encaminhamento
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    # Seleciona a msg enviada 
    lista_elementos = nav.find_elements('class name', '_amk4')
    for item in lista_elementos:
        mensagem = mensagem.replace("\n", "")
        texto = item.text.replace("\n", "")
        if mensagem in texto:
            elemento = item

    # Colocar o cursos em cima da msg para ser possívle abrir o "Encaminhar"
    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', '_ahkm').click()
    time.sleep(2)
    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    time.sleep(2)

    # Começa a selecionar os 5 contatos a serem enviados
    for nome in lista_enviar:
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(nome)
        time.sleep(1.3)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(1.5)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        time.sleep(1.1)
    
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(5)