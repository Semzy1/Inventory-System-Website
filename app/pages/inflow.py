import reflex as rx
from app.state import InventoryState, InflowTransaction


def transaction_row(transaction: InflowTransaction) -> rx.Component:
    """A single row in the inflow transactions table."""
    return rx.el.tr(
        rx.el.td(transaction["id"], class_name="px-6 py-4"),
        rx.el.td(transaction["item_name"], class_name="px-6 py-4 font-medium"),
        rx.el.td(transaction["quantity"], class_name="px-6 py-4"),
        rx.el.td(transaction["supplier"], class_name="px-6 py-4"),
        rx.el.td(transaction["date"], class_name="px-6 py-4"),
        rx.el.td(transaction["notes"], class_name="px-6 py-4"),
        class_name="border-b bg-white hover:bg-gray-50",
    )


def summary_card(title: str, value: rx.Var, icon: str) -> rx.Component:
    """A card for displaying a summary statistic."""
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-gray-500"),
            class_name="p-3 bg-gray-100 rounded-lg",
        ),
        rx.el.div(
            rx.el.p(value, class_name="text-2xl font-bold text-gray-800"),
            rx.el.p(title, class_name="text-sm text-gray-500"),
        ),
        class_name="flex items-center gap-4 p-4 bg-white border rounded-xl shadow-sm",
    )


def inflow_page() -> rx.Component:
    """The inflow page displaying all incoming transactions."""
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Inflow Transactions",
                class_name="text-3xl font-bold text-gray-800 tracking-tight",
            ),
            rx.el.p(
                "Tracking all incoming stock and shipments.",
                class_name="text-gray-600 mt-1",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            summary_card(
                "Total Transactions",
                InventoryState.inflow_transactions.length(),
                "list-ordered",
            ),
            summary_card(
                "Total Quantity In",
                InventoryState.total_inflow_quantity,
                "package-plus",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-500",
                ),
                rx.el.input(
                    placeholder="Search transactions...",
                    on_change=InventoryState.set_inflow_search,
                    class_name="w-full max-w-sm pl-10 pr-4 py-2 rounded-lg border bg-white focus:border-emerald-500 focus:ring-emerald-500",
                ),
                class_name="relative",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th("ID", class_name="px-6 py-3"),
                        rx.el.th("Item Name", class_name="px-6 py-3"),
                        rx.el.th("Quantity", class_name="px-6 py-3"),
                        rx.el.th("Supplier", class_name="px-6 py-3"),
                        rx.el.th("Date", class_name="px-6 py-3"),
                        rx.el.th("Notes", class_name="px-6 py-3"),
                        class_name="text-xs text-gray-700 uppercase bg-gray-100 text-left",
                    )
                ),
                rx.el.tbody(
                    rx.foreach(InventoryState.filtered_inflow, transaction_row)
                ),
                class_name="w-full text-sm text-left text-gray-600 table-auto",
            ),
            class_name="relative overflow-x-auto rounded-xl border",
        ),
        class_name="p-8 w-full",
    )