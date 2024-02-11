import flet as ft
from pessoaRepositorie import PessoaRepositorie as pr

def main(page: ft.Page):
    def btn_cadastrar_click(e):
        if all([nome_input.value, idade_input.value]):
            pr.insert(nome_input.value, idade_input.value, documento_input.value, telefone_input.value, email_input.value)
            dlg = ft.AlertDialog(title=ft.Text('Sucesso'))
            page.dialog = dlg
            dlg.open = True
            page.update()
    page.title = 'Simple Register'
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.padding = 100
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.appbar = ft.AppBar(title=ft.Text('Register'), center_title=True)
    nome_input = ft.TextField(label='Nome', autofocus=True, hint_text='Digite seu nome')
    idade_input = ft.TextField(label='Idade', autofocus=True, hint_text='Informe a idade')
    documento_input = ft.TextField(label='Documento', autofocus=True, hint_text='Informe a sua identificação')
    telefone_input = ft.TextField(label='Telefone', autofocus=True, hint_text='Informe o seu telefone')
    email_input = ft.TextField(label='E-mail', autofocus=True, hint_text='Informe o seu e-mail')
    btn_cadastrar = ft.ElevatedButton(text='Cadastrar',width=600, on_click=btn_cadastrar_click)
    page.update()
    page.add(nome_input, idade_input, documento_input, telefone_input, email_input, btn_cadastrar)