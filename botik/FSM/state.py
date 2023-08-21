from aiogram.fsm.state import State, StatesGroup

class Order(StatesGroup):
    admin_panel = State()
    choosing_type = State()
    choosing_brand = State()
    choosing_taste = State()

class AdminPanelAddRow(StatesGroup):
    brand = State()
    liquid_mg = State()
    number_of_pulls = State()
    flavor = State()
    quantity = State()
    price = State()
    