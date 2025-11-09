import reflex as rx
from app.state import InventoryState, Item
from app.components.item_card import item_card


def portfolio_page() -> rx.Component:
    """The portfolio page displaying all inventory items."""
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Item Portfolio",
                class_name="text-3xl font-bold text-gray-800 tracking-tight",
            ),
            rx.el.p(
                "A complete overview of all items in your inventory.",
                class_name="text-gray-600 mt-1",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-500",
                ),
                rx.el.input(
                    placeholder="Search items by name or category...",
                    on_change=InventoryState.set_portfolio_search,
                    class_name="w-full max-w-sm pl-10 pr-4 py-2 rounded-lg border bg-white focus:border-emerald-500 focus:ring-emerald-500",
                ),
                class_name="relative",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.foreach(InventoryState.filtered_items, item_card),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
        ),
        class_name="p-8 w-full",
    )