import pyautogui
import pandas as pd
import time
# importar a base de produtos 
tabela = pd.read_csv("produtos.csv")
print (tabela)
pyautogui.FAILSAFE = True

#entrar no site da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 1.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# Entrar no site da empresa
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


#fazer login no site
# selecionar o botão email
pyautogui.click(x=632, y=467)
#escrever seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua_senha_aqui")
# Apertou tab , escreveu a senha 
pyautogui.click(x=951, y=661)
time.sleep(3)



#cadastrar primeiro produto
# Primeiro vamos clicar na linha código
# usaremos o for e iremos percorrer cada espaço para preencher com as informações
# utilizaremos o Tab para pular entre as linhas do site e ir preenchendo

for linha in tabela.index:
    pyautogui.click(x=652, y=328)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):  
        pyautogui.write(str(tabela.loc[linha, "obs"]))
# Clicar no botão enter
    pyautogui.click(x=818, y=636)
    time.sleep(2)
    pyautogui.scroll(50000)

    


#enviar as informações do produto
#repetir o passo 1
