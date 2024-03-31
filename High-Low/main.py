import flet as ft


def main(page: ft.Page):
    page.title = "High-Low Game"
    display_bar = ft.Text("Welcome to high-low")
    page.add(display_bar)
    def press_play(e):
        display_bar.value = "Select a number"
        page.remove_at(1)
        page.update()
    play_text = ft.CupertinoFilledButton(
        content = ft.Text("Play"),
        on_click = press_play
    )
    page.add(play_text)
    page.update()

    print(page.controls)

ft.app(main)
