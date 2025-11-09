import reflex as rx
from app.state import InventoryState, NavItem


def nav_link(item: NavItem) -> rx.Component:
    """A navigation link component for the sidebar."""
    return rx.el.a(
        rx.icon(item["icon"], class_name="h-5 w-5 shrink-0"),
        rx.el.span(item["name"]),
        href=item["href"],
        on_click=lambda: InventoryState.set_page(item["name"]),
        class_name=rx.cond(
            InventoryState.current_page == item["name"],
            "flex items-center gap-3 rounded-lg bg-emerald-100 px-3 py-2 text-emerald-700 transition-all hover:text-emerald-800 font-semibold",
            "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-600 transition-all hover:bg-gray-100 hover:text-gray-900",
        ),
    )


def sidebar() -> rx.Component:
    """The main sidebar navigation component."""
    return rx.el.aside(
        rx.el.div(
            rx.el.a(
                rx.icon("boxes", class_name="h-7 w-7 text-emerald-600"),
                rx.el.span(
                    "InvManager",
                    class_name="text-xl font-bold tracking-tight text-gray-800",
                ),
                href="/",
                class_name="flex items-center gap-2",
            ),
            class_name="flex h-16 items-center border-b px-6",
        ),
        rx.el.nav(
            rx.foreach(InventoryState.nav_items, nav_link),
            class_name="flex-1 flex flex-col gap-1 p-4",
        ),
        class_name="hidden md:flex flex-col h-screen w-64 border-r bg-white font-['Raleway']",
    )