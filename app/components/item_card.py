import reflex as rx
from app.state import Item


def item_card(item: Item) -> rx.Component:
    """A card component to display a single inventory item."""
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=item["image_url"],
                alt=item["name"],
                class_name="h-48 w-full object-cover",
            ),
            class_name="overflow-hidden rounded-t-xl border-b",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    item["category"],
                    class_name="text-xs font-semibold uppercase tracking-wider text-emerald-600",
                ),
                class_name="mb-2",
            ),
            rx.el.h3(
                item["name"], class_name="text-lg font-bold text-gray-800 truncate"
            ),
            rx.el.p(f"SKU: {item['sku']}", class_name="text-sm text-gray-500"),
            class_name="p-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    f"{item['quantity']}", class_name="text-2xl font-bold text-gray-800"
                ),
                rx.el.p("In Stock", class_name="text-sm text-gray-500"),
                class_name="text-center",
            ),
            rx.el.div(
                rx.cond(
                    item["unit_price_naira"].to(bool),
                    rx.el.p(
                        "₦" + item["unit_price_naira"].to_string(),
                        class_name="text-lg font-bold text-emerald-600",
                    ),
                ),
                rx.cond(
                    item["unit_price_dollar"].to(bool),
                    rx.el.p(
                        "$" + item["unit_price_dollar"].to_string(),
                        class_name="text-lg font-bold text-emerald-600",
                    ),
                ),
                rx.cond(
                    item["unit_price_euro"].to(bool),
                    rx.el.p(
                        "€" + item["unit_price_euro"].to_string(),
                        class_name="text-lg font-bold text-emerald-600",
                    ),
                ),
                rx.el.p("Unit Cost", class_name="text-sm text-gray-500"),
                class_name="text-center",
            ),
            class_name="flex justify-around items-center p-4 border-t",
        ),
        class_name="bg-white rounded-xl border border-gray-200 shadow-md transition-all duration-300 hover:shadow-2xl hover:-translate-y-1",
    )