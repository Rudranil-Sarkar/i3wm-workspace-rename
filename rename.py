import i3ipc
import subprocess

i3 = i3ipc.Connection()

def Rename_WorkSpace(name):
    workspace = i3.get_tree().find_focused().workspace()
    num = workspace.name.split(':')[0] # Keeping the number because without it the workspace became unswitchable
    workspace.command('rename workspace "{}" to "{}"'.format(workspace.name, '{}: {}'.format(num, name)))

def main():
    out = subprocess.Popen(['echo'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    dmenu_out = subprocess.Popen(["dmenu", "-p", "Enter New Name"], stdin=out.stdout,
                                 stdout = subprocess.PIPE)
    name = dmenu_out.communicate()[0]
    Rename_WorkSpace(name.decode('utf-8').capitalize())

if __name__ == '__main__':
    main()
