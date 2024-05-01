import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.hstack(
        rx.text(f"¡Esto es el footer y te lleva a Youtube! Esto fué creado en el año {datetime.date.today().year}"),
        rx.image(src="favicon.ico")
    )