# enter input and compute the result
import PySimpleGUI as sg

text = sg.PopupGetText('enter a command: ')
print(text, '=', eval(text))