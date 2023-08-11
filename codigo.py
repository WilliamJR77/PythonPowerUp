# Passo a passo do projeto Python_PowerUp
# passo 1: entrar no sistema da empresa
# abrir o navegador 

import pyautogui
import time

# Comando do pyautogui permite com que voce automatize tarefas no python
# pyautogui.write("") -> escrever um texto
# pyautogui.press("") -> apertar um tecla
# pyautogui.click() -> clivar em algum lugat da tela
# pyautogui.hotkey("", "" ,"") -> combinacao de teclas
# time.sleep(number in seconds) -> depay em segundos em algum lugar do codigo         


# pyautogui.PAUSE -> coloca um delay entre os comandos
pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

# entrar no link da empresa:
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# passo 2: fazer o login
# selecionar o campo de email
pyautogui.click(x=408, y=421)
#escrever o seu email
pyautogui.write("emailtesteparaprojetos@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.click(x=674, y=584) # cick no botao de login
time.sleep(3)

# passo 3: importar a base de produtos para cadastrar
import pandas as pd
baseDados = pd.read_csv("produtos.csv")
print(baseDados)

# passo 4: cadastrar um produto
# passo 5: repetir o processo de cadastro ate o fim
for linha in baseDados.index:
    # clicar no campo de codigo
    pyautogui.click(x=398, y=306)
    # Pegar da base de dados o valor co campo que a gente quer preencher'
    codigo = baseDados.loc[linha, "codigo"]
    # preencher o campo 
    pyautogui.write(str(codigo))
    # passar para  o proximo campo 
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(baseDados.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(baseDados.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(baseDados.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(baseDados.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(baseDados.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = baseDados.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(baseDados.loc[linha, "obs"]))
    pyautogui.press("tab")

    #  Finalizar o cadastro do produto
    pyautogui.press("enter")
    # dar scroll de tudo pra cima 
    pyautogui.scroll(15000)