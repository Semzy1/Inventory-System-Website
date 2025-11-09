import reflex as rx
from app.pages.base_layout import base_layout
from app.pages.portfolio import portfolio_page
from app.pages.inflow import inflow_page
from app.pages.outflow import outflow_page


def index() -> rx.Component:
    return base_layout(portfolio_page())


def inflow() -> rx.Component:
    return base_layout(inflow_page())


def outflow() -> rx.Component:
    return base_layout(outflow_page())


from app.pages.admin import admin_page


def admin() -> rx.Component:
    return base_layout(admin_page())


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
from app.state import InventoryState
from app.state import InventoryState

app.add_page(
    index, route="/", title="Portfolio | InvManager", on_load=InventoryState.on_load
)
app.add_page(inflow, route="/inflow", title="Inflow | InvManager")
app.add_page(outflow, route="/outflow", title="Outflow | InvManager")
app.add_page(admin, route="/admin", title="Admin | InvManager")