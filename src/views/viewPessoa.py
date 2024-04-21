import flet as ft
import src.views.cadastroPessoa as cp
from pessoaRepositorie import PessoaRepositorie as pr

def main(page: ft.Page):

    dt = ft.DataTable(
        width=700,
        column_spacing=200,
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Idade")),
            ft.DataColumn(ft.Text("Documento"))
        ],
        rows=[]
    )

    def btn_cadastrar_onclick(e):
        ft.app(target=cp.main)
        popular_datatable()
        page.update()

    def btn_alterar_onclick(e):
        pass

    def btn_excluir_onclick(e):
        pass

    btn_cadastrar = ft.ElevatedButton(text='Cadastrar',width=300, on_click=btn_cadastrar_onclick)
    btn_alterar = ft.ElevatedButton(text='Alterar',width=300, on_click=btn_alterar_onclick)
    btn_excluir = ft.ElevatedButton(text='Excluir',width=300, on_click=btn_excluir_onclick)

    def popular_datatable():
        dt.rows.clear()
        query = pr.search()

        for i in range(len(query)):
            dt.rows.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(query[i].get('NOME'))),
                    ft.DataCell(ft.Text(query[i].get('IDADE'))),
                    ft.DataCell(ft.Text(query[i].get('DOCUMENTO')))
                ]
            ))

    popular_datatable()
    page.add(ft.ElevatedButton(content=ft.Row([btn_cadastrar,  
            btn_alterar, 
            btn_excluir])),
            dt   
        )
    page.update()

if __name__ == "__main__":
    main()