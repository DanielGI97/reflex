import reflex as rx
from pyreflex.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Mi instagram","https://www.instagram.com/daniel_g_i_25/"),
        link_button("Mi Linkedin","https://www.linkedin.com/in/daniel-gonz%C3%A1lez-ibarra-459a1313a/"),
        link_button("Mi Twitch","https://www.twitch.tv/miticus25"),
        align="center",
        width="100%"
    )