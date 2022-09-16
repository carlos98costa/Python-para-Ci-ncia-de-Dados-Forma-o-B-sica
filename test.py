import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg

caminho = 'QUESTIONÁRIO SOCIOECONÔMICO 1 (1).csv'

arquivoCSV = pd.read_csv(caminho)
arquivoCSV.columns = [arquivoCSV]

print(arquivoCSV.columns)

listCSV = arquivoCSV.columns

use_custom_titlebar = False

def make_window(theme=None):
    NAME_SIZE = 23

    def name(name):
        dots = 23 - 4 - 2
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    sg.theme(theme)

    treedata = sg.TreeData()

    treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
    treedata.Insert("", '_B_', 'B', [])
    treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )

    layout_l = [[name('Text'), sg.Text('Nossa interface')],
                [name('Input'), sg.Input(s=50), sg.FileBrowse()],
                [name('Listbox'), sg.Listbox(listCSV[1:85], no_scrollbar=True,  s=(80,10))],
                [name('Image'), sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
                [name('Graph'), sg.Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]  ]


    layout = [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)] if use_custom_titlebar else [sg.Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [sg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-')],
              [sg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 18', justification='c', expand_x=True)],
              [sg.Col(layout_l)]]

    window = sg.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)
                                                  # Show 30% complete on ProgressBar
    window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

    return window

# Start of the program...
window = make_window()

while True:
    event, values = window.read()
    sg.popup(event, values)                     # show the results of the read in a popup Window
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if values['-COMBO-'] != sg.theme():
        sg.theme(values['-COMBO-'])
        window.close()
        window = make_window()
    if event == '-USE CUSTOM TITLEBAR-':
        use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
        window.close()
        window = make_window()
window.close()