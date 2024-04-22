import flet as ft
import src.views.cadastroPessoa as cp
from src.models.repository.person_repository import PersonRepository as pr

def main(page: ft.Page):

    def popular_datatable():
        pass
        #dt.rows.clear()
        #query = pr.get_all_person()

        #for i in range(len(query)):
        #    dt.rows.append(ft.DataRow(
        #        cells=[
        #            ft.DataCell(ft.Text(query[i].get('NOME'))),
        #            ft.DataCell(ft.Text(query[i].get('IDADE'))),
        #            ft.DataCell(ft.Text(query[i].get('DOCUMENTO')))
        #        ]
        #   ))

    def cadastrar_onclick(e):
        popular_datatable()
        page.update()

    
    def btn_excluir_onclick(e):
        pass

    def btn_alterar_onclick(e):
        pass

    dt = ft.DataTable(
        width=700,
        column_spacing=200,
        show_checkbox_column=True,
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Idade")),
            ft.DataColumn(ft.Text("Documento"))
        ],
        rows=[]
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=cadastrar_onclick, bgcolor=ft.colors.LIME_500
    )

    btn_alterar = ft.ElevatedButton(text='Alterar',width=300, on_click=btn_alterar_onclick)
    btn_excluir = ft.ElevatedButton(text='Excluir',width=300, on_click=btn_excluir_onclick)

    popular_datatable()

    page.add(ft.ElevatedButton(content=ft.Row([  
            btn_alterar, 
            btn_excluir])),
            dt   
        )
    page.update()

if __name__ == "__main__":
    main()