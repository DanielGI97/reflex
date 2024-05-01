import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="Miticus",size="6"),
        rx.text("@miticus"),
        rx.text("HOLA QUE TAL ESTA ES MI PRIMERA PÁGINA"),
        align="center"
    )