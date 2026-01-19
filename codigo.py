import pyautogui
import time
import pandas as pd
import paperclip

# Define um intervalo curto entre comandos simples
pyautogui.PAUSE = 0.5

# Passo 1 - Abrir o navegador
pyautogui.press('win')
pyautogui.write('firefox')
pyautogui.press('enter')

# --- PAUSA CRÍTICA ---
# Precisamos esperar o Firefox abrir de fato antes de digitar o link
time.sleep(5) 

# Passo 2 - Entrar no site da empresa
pyautogui.hotkey('ctrl', 'l') # Seleciona a barra de URL (atalho universal)
time.sleep(0.5)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Espera o site carregar completamente
time.sleep(3)

# Passo 3 - Fazer login
# Clicar no campo de email
pyautogui.click(x=982, y=371)  # Coordenadas do campo de email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")  # Passa para o campo de senha
pyautogui.write("1234456")  # Digita a senha
pyautogui.click(x=1001, y=549)  # Clica no botão de login
time.sleep(4)  # Espera a página carregar

# Passo 4 - Baixar a base de dados
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    # Passo 5 - Cadastrar os produtos - no formulário
    pyautogui.click(x=970, y=253)  # Coordenadas do campo do código do produto

    

    codigo = str(tabela.loc[linha, "codigo"])   
    pyautogui.write(codigo)  # Digita o código do produto
    pyautogui.press("tab")  # Passa para o próximo campo

    #campo marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")  # Passa para o próximo campo

    #campo tipo
    tipo= str(tabela.loc[linha, "tipo"])    
    pyautogui.write(tipo)
    pyautogui.press("tab")  # Passa para o próximo campo

    #campo categoria do produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")  # Passa para o próximo campo

    #campo preço
    preco =  str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")  # Passa para o próximo campo

    #campo custo do produto
    custo = str(tabela.loc[linha, "custo"]) 
    pyautogui.write("50.00")
    pyautogui.press("tab")  # Passa para o próximo campo

    #campo observação
    observacao = str(tabela.loc[linha, "obs"])          
    pyautogui.write(observacao)
    pyautogui.press("tab")  # Passa para o botão enviar

    pyautogui.press("enter")  # Envia o formulário


    pyautogui.scroll(5000)  # Rola para cima (para o topo da página)

