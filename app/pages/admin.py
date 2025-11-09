import reflex as rx
from app.state import InventoryState, Item


def admin_item_row(item: Item) -> rx.Component:
    """A single row in the admin items table."""
    return rx.el.tr(
        rx.el.td(item["name"], class_name="px-6 py-4 font-medium"),
        rx.el.td(item["sku"], class_name="px-6 py-4"),
        rx.el.td(item["category"], class_name="px-6 py-4"),
        rx.el.td(item["quantity"], class_name="px-6 py-4"),
        rx.el.td(
            rx.el.div(
                rx.cond(
                    item["unit_price_naira"].to(bool),
                    rx.el.span("₦" + item["unit_price_naira"].to_string()),
                ),
                rx.cond(
                    item["unit_price_dollar"].to(bool),
                    rx.el.span("$" + item["unit_price_dollar"].to_string()),
                ),
                rx.cond(
                    item["unit_price_euro"].to(bool),
                    rx.el.span("€" + item["unit_price_euro"].to_string()),
                ),
                class_name="flex flex-col",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon(tag="copy", class_name="h-4 w-4"),
                    class_name="p-1 text-blue-600 hover:text-blue-800",
                ),
                rx.el.button(
                    rx.icon(tag="trash-2", class_name="h-4 w-4"),
                    on_click=lambda: InventoryState.delete_item(item["id"]),
                    class_name="p-1 text-red-600 hover:text-red-800",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="px-6 py-4",
        ),
        class_name="border-b bg-white hover:bg-gray-50",
    )


def admin_page() -> rx.Component:
    """The admin page for managing inventory.
    This is a placeholder and will be built out in a future step.
    """
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Admin Panel",
                class_name="text-3xl font-bold text-gray-800 tracking-tight",
            ),
            rx.el.p(
                "Manage your inventory items and settings.",
                class_name="text-gray-600 mt-1",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.h2(
                "Add New Item", class_name="text-xl font-semibold text-gray-700 mb-4"
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.input(
                        placeholder="Name",
                        name="name",
                        type="text",
                        required=True,
                        class_name="w-full px-3 py-2 border rounded-lg",
                    ),
                    rx.el.input(
                        placeholder="SKU",
                        name="sku",
                        type="text",
                        required=True,
                        class_name="w-full px-3 py-2 border rounded-lg",
                    ),
                    rx.el.input(
                        placeholder="Category",
                        name="category",
                        type="text",
                        required=True,
                        class_name="w-full px-3 py-2 border rounded-lg",
                    ),
                    rx.el.input(
                        placeholder="Quantity",
                        name="quantity",
                        type="number",
                        required=True,
                        class_name="w-full px-3 py-2 border rounded-lg",
                    ),
                    rx.el.input(
                        placeholder="Unit Price (Naira)",
                        name="unit_price_naira",
                        type="number",
                        step="0.01",
                        class_name="w-full px-3 py-2 border rounded-lg",
                    ),
                    rx.el.input(
                        placeholder="Unit Price (Dollar)",
                        name="unit_price_dollar",
                        type="number",
                        step="0.01",
                        class_name="w-full px-3 py-2 border rounded-lg",
                    ),
                    rx.el.input(
                        placeholder="Unit Price (Euro)",
                        name="unit_price_euro",
                        type="number",
                        step="0.01",
                        class_name="w-full px-3 py-2 border rounded-lg",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4",
                ),
                rx.el.button(
                    "Add Item",
                    type="submit",
                    class_name="px-4 py-2 bg-emerald-600 text-white font-semibold rounded-lg hover:bg-emerald-700 transition-colors",
                ),
                on_submit=InventoryState.add_item,
                reset_on_submit=True,
            ),
            class_name="p-6 bg-white border rounded-xl shadow-sm mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Record Inflow",
                        class_name="text-xl font-semibold text-gray-700 mb-4",
                    ),
                    rx.el.form(
                        rx.el.select(
                            rx.foreach(
                                InventoryState.items,
                                lambda item: rx.el.option(
                                    item["name"], value=item["name"]
                                ),
                            ),
                            name="item_name",
                            placeholder="Select Item",
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.input(
                            placeholder="Quantity",
                            name="quantity",
                            type="number",
                            required=True,
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.input(
                            placeholder="Supplier",
                            name="supplier",
                            type="text",
                            required=True,
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.input(
                            name="date",
                            type="date",
                            required=True,
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.input(
                            placeholder="Notes",
                            name="notes",
                            type="text",
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.button(
                            "Add Inflow",
                            type="submit",
                            class_name="w-full px-4 py-2 bg-emerald-600 text-white font-semibold rounded-lg hover:bg-emerald-700 transition-colors",
                        ),
                        on_submit=InventoryState.add_inflow_transaction,
                        reset_on_submit=True,
                        class_name="space-y-4",
                    ),
                    class_name="p-6 bg-white border rounded-xl shadow-sm",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Record Outflow",
                        class_name="text-xl font-semibold text-gray-700 mb-4",
                    ),
                    rx.el.form(
                        rx.el.select(
                            rx.foreach(
                                InventoryState.items,
                                lambda item: rx.el.option(
                                    item["name"], value=item["name"]
                                ),
                            ),
                            name="item_name",
                            placeholder="Select Item",
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.input(
                            placeholder="Quantity",
                            name="quantity",
                            type="number",
                            required=True,
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.input(
                            placeholder="Destination",
                            name="destination",
                            type="text",
                            required=True,
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.input(
                            name="date",
                            type="date",
                            required=True,
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.input(
                            placeholder="Notes",
                            name="notes",
                            type="text",
                            class_name="w-full px-3 py-2 border rounded-lg",
                        ),
                        rx.el.button(
                            "Add Outflow",
                            type="submit",
                            class_name="w-full px-4 py-2 bg-red-500 text-white font-semibold rounded-lg hover:bg-red-600 transition-colors",
                        ),
                        on_submit=InventoryState.add_outflow_transaction,
                        reset_on_submit=True,
                        class_name="space-y-4",
                    ),
                    class_name="p-6 bg-white border rounded-xl shadow-sm",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8",
            )
        ),
        rx.el.div(
            rx.el.h2(
                "Item List", class_name="text-xl font-semibold text-gray-700 mb-4"
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th("Name", class_name="px-6 py-3"),
                            rx.el.th("SKU", class_name="px-6 py-3"),
                            rx.el.th("Category", class_name="px-6 py-3"),
                            rx.el.th("Quantity", class_name="px-6 py-3"),
                            rx.el.th("Unit Price", class_name="px-6 py-3"),
                            rx.el.th("Actions", class_name="px-6 py-3"),
                            class_name="text-xs text-gray-700 uppercase bg-gray-100 text-left",
                        )
                    ),
                    rx.el.tbody(rx.foreach(InventoryState.items, admin_item_row)),
                    class_name="w-full text-sm text-left text-gray-600 table-auto",
                ),
                class_name="relative overflow-x-auto rounded-xl border",
            ),
        ),
        class_name="p-8 w-full",
    )