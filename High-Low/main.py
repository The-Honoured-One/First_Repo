import flet as ft
import random


def main(page: ft.Page):
    page.window_width = 300
    page.window_height = 300
    page.window_resizable = False
    page.update()
    page.title = "High-Low Game"
    display_bar = ft.Text("Welcome to high-low")
    page.add(ft.Row([display_bar], alignment = ft.MainAxisAlignment.CENTER))
    def add(e):
        main_display.value = str(int(main_display.value) + 1)
        page.update()
    def subtract(e):
        main_display.value = str(int(main_display.value) - 1)
        page.update()
    def check (e):
        if int(main_display.value) == target:
            display_bar.value = "CORRECT GUESS !!"
            page.update()
        elif int(main_display.value) > target:
            display_bar.value = "Go Lower, " + str(count) + " more tries"
            page.update()        
        else:
            display_bar.value = "Go Higher, " + str(count) + " more tries"
            page.update()
    def press_play(e):
        display_bar.value = "Select a number"
        page.remove_at(1)
        page.update()
        target = random.randint(1,9)
        page.add(ft.Row([
            ft.IconButton(icon = ft.icons.ADD, on_click = add),
            main_display,
            ft.IconButton(icon = ft.icons.REMOVE, on_click = subtract)
        ], alignment = ft.MainAxisAlignment.CENTER))
        page.add(ft.Row([ft.CupertinoButton(
            content=ft.Text("GUESS", color=ft.cupertino_colors.DESTRUCTIVE_RED),
            opacity_on_click=0.3,
            on_click= check)], alignment = ft.MainAxisAlignment.CENTER))
        page.update()
    play_text = ft.CupertinoFilledButton(
        content = ft.Text("Play"),
        on_click = press_play
    )
    page.add(ft.Row([play_text], alignment = ft.MainAxisAlignment.CENTER))
    page.update()
    main_display = ft.Text("0")
    count = 2

    target = random.randint(1,9)


ft.app(main)
