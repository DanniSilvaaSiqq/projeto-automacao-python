import pyautogui
import time

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=720, y=476)
pyautogui.write("asdasdasda23@gmail.com")
pyautogui.press("tab")
pyautogui.write("asdsadas123435")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=695, y=326)

    #Código do Produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #Marca do Produto
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #Tipo do Produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #Categoria do Produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #Preço Unitário do Produto
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    #Custo do Produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)