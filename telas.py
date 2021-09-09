from PySimpleGUI import PySimpleGUI as sg


def janela_login():
    sg.theme('LightGray1')
    layout = [
        [sg.Text('Login:', font=('Arial', 12), size=(5, 1)), sg.Input(key='login', size=(30, 1))],
        [sg.Text('Senha:', font=('Arial', 12), size=(5, 1)), sg.Input(key='senha', password_char='*',
                                                                      size=(30, 1), text_color='red')],
        [sg.Text('\n')],
        [sg.Button('Entrar', size=(8, 2)), sg.Button('Novo Cadastro', size=(8, 2)), sg.Button('Sair', size=(8, 2))],
    ]
    return sg.Window('Tela de Login', layout=layout, size=(400, 300), finalize=True,
                     element_justification='center', resizable=True)
    # element_justification server para centralizar o layout
    # resizable serve para permitir que a janela seja redimensionada após a axecursão

def janela_cadastro():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text(f'{"Nome":<10}'), sg.Input(key='nome', size=(100, 1))],
        [sg.Text(f'{"Sobre Nome":<10}'), sg.Input(key='sobre_nome', size=(100, 1))],
        [sg.Text(f'{"Email":<10}'), sg.Input(key='email', size=(100, 1))],
        [sg.Text(f'{"Telefone":<10}'), sg.Input(key='telefone', size=(100, 1))],
        [sg.Text(f'{"Login":<10}'), sg.Input(key='login', size=(100, 1))],
        [sg.Text(f'{"Senha":<10}'), sg.Input(password_char='*', key='nova_senha', size=(100, 1))],
        [sg.Text(' ')],
        [sg.Button('Salvar', size=(10, 3)), sg.Button('Cancelar', size=(10, 3))],
    ]
    return sg.Window('Tela de Cadastro', layout=layout, resizable=True, finalize=True,
                     size=(400, 300), element_justification='left')


if __name__ == '__main__':
    janela1, janela2 = janela_login(), None
    while True:
        windwos, eventos, valores = sg.read_all_windows()
        if windwos == janela1 and eventos == sg.WIN_CLOSED or eventos == 'Sair':
            break

        elif windwos == janela1 and eventos == 'Novo Cadastro':
            janela1.close()
            janela2 = janela_cadastro()
        elif windwos == janela2 and eventos == 'Cancelar' or eventos == sg.WIN_CLOSED:
            janela2.close()
            janela1 = janela_login()

