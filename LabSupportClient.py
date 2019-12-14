import sys

from app.src.updates import updater

if __name__ == '__main__':
    updates_disabled = False
    if len(sys.argv) > 1:
        updates_disabled = sys.argv[1] == "--no-updates"
    if not updates_disabled and updater.do_update():
        print("Client updated!")
    from app.src import GUI
    gui = GUI.Gui()
