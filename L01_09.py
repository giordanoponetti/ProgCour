# enter input
import PySimpleGUI as sg

text = sg.PopupGetText('enter a command: ')
print(text)
print(eval(text))