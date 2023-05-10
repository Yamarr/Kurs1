start = 0
elapsed = 0

def on_button_pressed_a():
    global start
    start = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)

# wenn B gedrückt wird ...

def on_button_pressed_b():
    global elapsed
    elapsed = input.running_time() - start
    basic.show_number(elapsed)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
