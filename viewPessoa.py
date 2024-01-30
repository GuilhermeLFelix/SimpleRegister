import flet as ft
import cadastroPessoa as cp

def  main(page: ft.Page):
    def btn_cadastrar_onclick(e):
        ft.app(target=cp.main)

    def btn_alterar_onclick(e):
        pass

    def btn_excluir_onclick(e):
        pass

    btn_cadastrar = ft.ElevatedButton(text='Cadastrar',width=500, on_click=btn_cadastrar_onclick)
    btn_alterar = ft.ElevatedButton(text='Alterar',width=500, on_click=btn_alterar_onclick)
    btn_excluir = ft.ElevatedButton(text='Excluir',width=500, on_click=btn_excluir_onclick)

    page.add(ft.ElevatedButton(content=ft.Row([btn_cadastrar,  
            btn_alterar, 
            btn_excluir])),
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("Idade")),
                ft.DataColumn(ft.Text("Documento"))
            ]
        )
    )
    page.update()