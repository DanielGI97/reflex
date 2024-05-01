import reflex as rx

def link_button(text: str, url: str = None) -> rx.Component:

    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_right",
                ),
                rx.text(text)
            ),
            width="100%"
        ),
        href=url,
        is_external=True,
        width="100%"
    )
