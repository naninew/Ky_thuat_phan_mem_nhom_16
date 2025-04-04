from nicegui import app as nicegui_app, ui


def Login_page():
    dark_mode = ui.dark_mode()
    #
    #
    with ui.row().classes("w-full items-center"):
        result = ui.label().classes("mr-auto")
        with ui.button(icon="menu"):
            with ui.menu() as menu:
                ui.menu_item("Menu item 1", lambda: result.set_text("Selected item 1"))
                ui.menu_item("Menu item 2", lambda: result.set_text("Selected item 2"))
                ui.menu_item(
                    "Menu item 3 (keep open)",
                    lambda: result.set_text("Selected item 3"),
                    auto_close=False,
                )
                ui.separator()
                ui.menu_item("Light Mode", on_click=dark_mode.disable)
                ui.menu_item("Dark Mode", on_click=dark_mode.enable)
                ui.separator()
                ui.menu_item("Close", menu.close)
    ui.separator()
    with ui.row().classes("w-full"):
        ui.space()
        with ui.card().classes("items-center"):
            ui.label("Card content")
            ui.button("Add label", on_click=lambda: ui.label("Click!"))
            ui.timer(1.0, lambda: ui.label("Tick!"), once=True)
        ui.space()
