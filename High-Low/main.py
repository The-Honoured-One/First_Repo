import flet as ft


def main(page: ft.Page):
    page.window_width = 300
    page.window_height = 300
    page.window_resizable = False
    page.update()
    page.title = "High-Low Game"
    display_bar = ft.Text("Welcome to high-low")
    page.add(ft.Row([display_bar], alignment = ft.MainAxisAlignment.CENTER))
    def press_play(e):
        display_bar.value = "Select a number"
        page.remove_at(1)
        page.update()
    play_text = ft.CupertinoFilledButton(
        content = ft.Text("Play"),
        on_click = press_play
    )
    page.add(ft.Row([play_text], alignment = ft.MainAxisAlignment.CENTER))
    page.update()

    print(page.controls)

ft.app(main)
