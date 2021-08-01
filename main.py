import PySimpleGUI as psg
from manipula_dados import inserir_dados, recupera_senha_usuario
# Defina o conteúdo das janelas
def tela_inicial():
    layout= [
        [psg.Image('ifome_red.png')],
        [psg.Button('Cadastrar'), psg.Button('Acessar')]
    ]
    return psg.Window('Ifome', layout=layout, finalize=True)

def tela_cadastro():
    layout = [
    [psg.Text('', key='notification', size=(22,1))],
    [psg.Text('Nome: '), psg.Input(key='input_nome', size=(15, 1))],
    [psg.Text('Senha: '), psg.Input(key='input_senha', size=(15, 1))],
    [psg.Button('Salvar'), psg.Button('Cancelar')]
    ] 
    return psg.Window('Cadastro', layout=layout, finalize=True)

def tela_login():
    layout = [
    [psg.Text('', key='notification', size=(22,1))],
    [psg.Text('Nome: '), psg.Input(key='input_nome', size=(15, 1))],
    [psg.Text('Senha: '), psg.Input(key='input_senha', size=(15, 1))],
    [psg.Button('Acessar'), psg.Button('Voltar')]
    ]
    return psg.Window('Login', layout=layout, finalize=True)

# Crie as janelas
janela1, janela2, janela3 = tela_inicial(), None, None

while True:
    window, event, values = psg.read_all_windows()

    # funções com janela1
    if window == janela1 and event == psg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Cadastrar':
        janela2 = tela_cadastro()
        janela1.hide()
    if window == janela1 and event == 'Acessar':
        janela3 = tela_login()
        janela1.hide()

    # funções com janela 2
    if window == janela2 and (event == 'Cancelar' or event == psg.WIN_CLOSED):
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Salvar':
        if values['input_nome']!= '' and values['input_senha']!='':
            inserir_dados(values['input_nome'], values['input_senha'])
            janela2.hide()
            janela1.un_hide()
        else:
            janela2['notification'].update('O nome e senha são invalidos.')
    
    # funções com janela 3
    if window == janela3 and (event == 'Voltar' or event == psg.WIN_CLOSED):
        janela3.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Acessar':
        if values['input_nome']!= '' and values['input_senha']!='':
            if values['input_senha'] == recupera_senha_usuario(values['input_nome']):
                janela3['notification'].update(f'Bem Vindo {values["input_nome"]}.')
            else:
                janela3['notification'].update('Acesso negado.')
        else:
            janela3['notification'].update('Insira seu nome e senha.')