from PySimpleGUI import PySimpleGUI as sg


def janela_login():
    sg.theme('LightGray1')
    layout = [
        [sg.Text('Login:', font=('Arial', 12), size=(5, 1)), sg.Input(key='login', size=(30, 1))],
        [sg.Text('Senha:', font=('Arial', 12), size=(5, 1)), sg.Input(key='senha', password_char='×', size=(30, 1))],
        [sg.Text('\n')],
        [sg.Button('Entrar', size=(8, 2)), sg.Button('Novo Cadastro', size=(8, 2)), sg.Button('Sair', size=(8, 2))],
    ]
    return sg.Window('Tela de Login', layout=layout, size=(400, 300), finalize=True,
                     element_justification='center', resizable=True)
    # element_justification server para centralizar o layout
    # resizable serve para permitir que a janela seja redimensionada após a axecursão




if __name__ == '__main__':
    janela1, janela2 = janela_login(), None
    while True:
        windwos, eventos, valores = sg.read_all_windows()


