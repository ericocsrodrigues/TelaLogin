from PySimpleGUI import PySimpleGUI  as sg


def janela_login():
    sg.theme('LightGray1')
    layout = [
        [sg.Text('Login:'), sg.Input(key='login', size=(31, 1))],
        [sg.Text('Senha:'), sg.Input(key='senha', password_char='×', size=(30, 1))],
        [sg.Text('')],
        [sg.Button('Entrar'), sg.Button('Novo Cadastro'), sg.Button('Sair')],
    ]
    return sg.Window('Tela de Login', layout=layout, finalize=True)


if __name__ == '__main__':
    janela_login()
    while True:
        events, values = sg.read_all_windows()

