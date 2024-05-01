import reflex as rx
from pyreflex.components.navbar import navbar
from pyreflex.components.footer import footer
from pyreflex.views.header.header import header
from pyreflex.links.links import links
import pyreflex.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                align="center",
                margin_y=styles.Spacer.BIG.value 
            )
        ),
        rx.center(
            footer()
        )
    )
    
    
app = rx.App()
app.add_page(index)
app.compile()