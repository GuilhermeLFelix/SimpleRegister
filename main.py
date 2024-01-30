import flet as ft
import viewPessoa as vp
import database as db

db.initialize()

ft.app(target=vp.main)