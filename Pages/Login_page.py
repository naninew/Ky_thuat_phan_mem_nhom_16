from nicegui import app as nicegui_app, ui


def Login_page():
    dark_mode = ui.dark_mode()
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
    with ui.tabs().classes("w-full") as tabs:
        Login = ui.tab("Login")
        Register = ui.tab("Register")
    with ui.tab_panels(tabs, value=Login).classes("w-full"):
        with ui.tab_panel(Login):
            with ui.row().classes("w-full items-center"):
                ui.space()
                with ui.card().classes("w-1/2 items-center"):
                    ui.label("Login")
                    ui.input(
                        label="Email",
                        placeholder="your email",
                        on_change=lambda e: result_email.set_text(
                            "you typed: " + e.value
                        ),
                        validation={"Input too long": lambda value: len(value) < 20},
                    ).classes("w-1/2 items-center")
                    result_email = ui.label()

                    ui.input(
                        label="Password",
                        placeholder="your password",
                        on_change=lambda e: result_password.set_text(
                            "you typed: " + e.value
                        ),
                        validation={"Input too long": lambda value: len(value) < 20},
                    ).classes("w-1/2 items-center")
                    result_password = ui.label()
                    ui.button(
                        "Login", on_click=lambda: ui.label("Login success")
                    ).classes("w-1/2 items-center")
                    ui.timer(1.0, lambda: ui.label("Tick!"), once=True)
                ui.space()
        with ui.tab_panel(Register):
            with ui.row().classes("w-full"):
                ui.space()
                with ui.card().classes("w-1/2 items-center"):
                    ui.label("Register")
                    ui.input(
                        label="Email",
                        placeholder="your email",
                        on_change=lambda e: result_email.set_text(
                            "you typed: " + e.value
                        ),
                        validation={"Input too long": lambda value: len(value) < 20},
                    ).classes("w-1/2 items-center")
                    result_email = ui.label()

                    ui.input(
                        label="Password",
                        placeholder="your password",
                        on_change=lambda e: result_password.set_text(
                            "you typed: " + e.value
                        ),
                        validation={"Input too long": lambda value: len(value) < 20},
                    ).classes("w-1/2 items-center")
                    result_password = ui.label()

                    ui.input(
                        label="Confirm password",
                        placeholder="your password",
                        on_change=lambda e: result_confirm_password.set_text(
                            "you typed: " + e.value
                        ),
                        validation={"Input too long": lambda value: len(value) < 20},
                    ).classes("w-1/2 items-center")
                    result_confirm_password = ui.label()

                    ui.button(
                        "Register", on_click=lambda: ui.label("Register Success!")
                    ).classes("w-1/2 items-center")
                    ui.timer(1.0, lambda: ui.label("Tick!"), once=True)
                ui.space()
