import PySimpleGUI as gui
import ctypes
import platform

global usersearch


def make_dpi_aware():
    if int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)


def main(search_line):
    try:
        ourfile = open(usersearch)
    except:
        print("No such file found!!!")
        return

    counter = 0
    found = False  # so far nothing found
    for x in ourfile:
        counter += 1
        if str(search_line.lower()) in x.strip().lower():
            print(search_line + ' found in line_' + str(counter))
            found = True
    ourfile.close()

    if found:
        return True
    else:
        return False


# print(gui.theme_list())

make_dpi_aware()
gui.theme('DarkBrown5')
layout = [
    [gui.Text('Select file: '), gui.Input(key='-FILE-'), gui.FileBrowse()],
    [gui.Text(size=(0, 1))],
    [gui.Text('Search for: '), gui.InputText(key='-USERDATA-')],
    [gui.Button('Start searching')],
    [gui.Output(size=(100, 10))],
    [gui.Cancel()]]

window = gui.Window('Python Searcher', layout)

while True:
    event, values = window.read()
    try:
        usersearch = values["-FILE-"]
    except:
        break

    if event == 'Start searching':
        if main(values["-USERDATA-"]) is False:
            print("Not found in file")

    if event == gui.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks Exit
        break

window.close()
