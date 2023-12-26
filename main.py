def on_button_pressed_a():
    global num
    num = num + 1
    kitronik_VIEW128x64.show("Raiz Quadrada de " + str(num), 1)
    kitronik_VIEW128x64.show(Math.sqrt(num), 2)
    serial.write_number(Math.sqrt(num))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global num
    num = num - 1
    kitronik_VIEW128x64.show("Raiz Quadrada de " + str(num), 1)
    kitronik_VIEW128x64.show(Math.sqrt(num), 2)
    serial.write_number(Math.sqrt(num))
input.on_button_pressed(Button.B, on_button_pressed_b)

num = 0
kitronik_VIEW128x64.control_display_on_off(kitronik_VIEW128x64.on_off(True))
kitronik_VIEW128x64.set_font_size(kitronik_VIEW128x64.FontSelection.NORMAL)
serial.write_line("ON")
kitronik_VIEW128x64.show("Raiz Quadrada de " + str(num), 1)

def on_forever():
    pass
basic.forever(on_forever)
