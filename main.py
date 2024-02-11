import flet as ft
import viewPessoa as vp
import database as db

db.Database.initialize()

ft.app(target=vp.main)