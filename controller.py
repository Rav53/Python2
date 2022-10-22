from unittest import result
import main
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    main.init(value_a, value_b)
    result = main.sum()
    view.view_data(result)
    