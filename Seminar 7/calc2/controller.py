from statistics import mode
import  model as model
import view
import logger as log

def button_click():
    #result = model.do_it()
    value_a = view.get_value(1)
    value_b = view.get_value(2)
    operation = view.get_operation()
    if operation == '+':
        result = model.sum_num(value_a, value_b)
    if operation == '-':
        result = model.sub_num(value_a, value_b)
    if operation == '/':
        result = model.div_num(value_a, value_b)
    if operation == '*':
        result = model.mult_num(value_a, value_b)
    op = f'{value_a} {operation} {value_b}'
    view.view_data(op, result)
    log. operation_logger(op, result)