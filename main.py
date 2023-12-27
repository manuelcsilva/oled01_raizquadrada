def on_logo_pressed():
    global num
    num = 0
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("Raiz Quadrada de " + convert_to_text(num),
        1,
        kitronik_VIEW128x64.ShowAlign.CENTRE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    global num
    num = num + 1
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("Raiz Quadrada de " + convert_to_text(num),
        1,
        kitronik_VIEW128x64.ShowAlign.CENTRE)
    kitronik_VIEW128x64.show(Math.sqrt(num), 2)
    serial.write_number(Math.sqrt(num))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global num
    num = num - 1
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("Raiz Quadrada de " + convert_to_text(num),
        1,
        kitronik_VIEW128x64.ShowAlign.CENTRE)
    kitronik_VIEW128x64.show(Math.sqrt(num), 2)
    serial.write_number(Math.sqrt(num))
input.on_button_pressed(Button.B, on_button_pressed_b)

num = 0
kitronik_VIEW128x64.control_display_on_off(kitronik_VIEW128x64.on_off(True))
serial.write_line("ON")
kitronik_VIEW128x64.show("OLED01",
    1,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.BIG)
kitronik_VIEW128x64.show("Raiz",
    2,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.BIG)
kitronik_VIEW128x64.show("Quadrada",
    3,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.BIG)
basic.pause(2000)
kitronik_VIEW128x64.clear()
kitronik_VIEW128x64.show("Raiz Quadrada de " + convert_to_text(num),
    1,
    kitronik_VIEW128x64.ShowAlign.CENTRE)