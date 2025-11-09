import reflex as rx
from app.components.sidebar import sidebar
from app.state import InventoryState


def base_layout(child: rx.Component, *args, **kwargs) -> rx.Component:
    """A base layout that includes the sidebar and main content area."""
    return rx.el.div(
        sidebar(),
        rx.el.div(
            rx.el.header(
                rx.el.button(
                    rx.icon("panel-left", class_name="h-5 w-5"),
                    on_click=InventoryState.toggle_sidebar,
                    variant="ghost",
                    size="icon",
                    class_name=rx.cond(
                        InventoryState.sidebar_collapsed,
                        "p-1 rounded-md hover:bg-gray-100",
                        "hidden",
                    ),
                ),
                class_name="flex h-16 items-center border-b bg-white px-6 md:hidden",
            ),
            rx.el.main(child, class_name="flex-1 overflow-y-auto"),
            class_name="flex flex-col flex-1",
        ),
        class_name="flex h-screen w-full bg-gray-50 font-['Raleway']",
    )