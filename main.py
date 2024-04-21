import flet as ft
import src.views.viewPessoa as vp
import database as db

db.Database.initialize()

ft.app(target=vp.main)