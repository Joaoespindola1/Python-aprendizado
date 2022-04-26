from time import sleep
import pyautogui
import pyperclip
import pandas as pd
import openpyxl
import numpy
# Baixar a planilha de vendas
'''pyautogui.press('win')
pyautogui.write('Opera')
pyautogui.press('enter')
sleep(1)
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)
pyautogui.click(x=356, y=267, clicks=2)
sleep(3)
pyautogui.click(x=439, y=375)
sleep(1)
pyautogui.click(x=1704, y=162)
sleep(1)
pyautogui.click(x=1510, y=564)'''
# Analisar a planilha de vendas
tabela = pd.read_excel(r'C:\Users\Pichau\Downloads\Vendas - Dez.xlsx')

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
#Enviar o relatório de vendas
pyautogui.press('win')
pyautogui.write('Opera')
pyautogui.press('enter')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)
pyautogui.click(x=156, y=161)
sleep(3)
pyautogui.write('belledinizc@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
texto = f'''
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
João Pedro Espindola'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')