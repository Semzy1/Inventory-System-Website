import reflex as rx
from app.components.sidebar import sidebar


def base_layout(child: rx.Component, *args, **kwargs) -> rx.Component:
    """A base layout that includes the sidebar and main content area."""
    return rx.el.div(
        sidebar(),
        rx.el.main(child, class_name="flex-1 overflow-y-auto"),
        class_name="flex h-screen w-full bg-gray-50 font-['Raleway']",
    )