from app.src import GUI
from app.src.updates import updater

if __name__ == '__main__':
    if updater.do_update():
        print("Client updated, please restart.")
    gui = GUI.Gui()
