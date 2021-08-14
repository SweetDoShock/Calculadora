# -*- coding: UTF-8 -*-

#==============> ↓↓↓
#==============> BIBLIOTECAS ↓↓↓
import os
try:
	import pyfiglet
except:
	os.system('pip install pyfiglet')

#==============> VARIAVEIS ↓↓↓
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'
NF="\033[0m"
C_GREY89="\033[38;5;254m"
CR="\033[48;5;196m"
ch = f'\n\n   {R}>>>{C} '
a = f'{C}[{R}'
b = f'{C}]{G}'
back = f'   {a}00{b} RETORNAR'
c = f'{C}> {G}'
T = False

#==============> FUNÇÕES ↓↓↓
def clear():
	os.system('clear')
#==============> FIGLET's ↓↓↓
f = pyfiglet.figlet_format('Sweet', font = 'cosmic')

#==============> MENU ↓↓↓
while True:
	clear()
	print(f'              {a}∆{b} CODED BY {a}∆{b}{G}\n{f}\n   {G}[ MEU NÚMERO: {C}wa.me/5551997773672 {G}]\n\n')
	n1 = int(input(f'   {a}+{b} 1° VALOR {C}>>> {NF}{CR}'))
	n2 = int(input(f'{NF}   {a}+{b} 2° VALOR {C}>>> {NF}{CR}'))

#==============> RESULTADOS ↓↓↓


	print(f'''{NF}

   {C}===> RESULTADOS:

   {a}+{b} SOMA{C}          >>> {n1 + n2}
   {a}+{b} SUBTRAÇÃO{C}     >>> {n1 - n2} 
   {a}+{b} SUBTRAÇÃO INV{C} >>> {n2 - n1}
   {a}+{b} MULTIPLICAÇÃO{C} >>> {n1 * n2}
   {a}+{b} DIVISÃO{C}       >>> {n1 / n2}
   {a}+{b} DIV INTEIRA{C}   >>> {n1 // n2}
   {a}+{b} MÓDULO{C}        >>> {n1 % n2}
   {a}+{b} EXPONENCIAÇÃO{C} >>> {n1 ** n2}

   {a}?{b} PRESSIONE ENTER PARA REALIZAR UM NOVO CALCULO''');v = input(ch)
   
