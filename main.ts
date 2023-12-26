input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    num = 0
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("Raiz Quadrada de " + ("" + ("" + num)), 1, kitronik_VIEW128x64.ShowAlign.Centre)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    num = num + 1
    kitronik_VIEW128x64.show("Raiz Quadrada de " + ("" + ("" + num)), 1, kitronik_VIEW128x64.ShowAlign.Centre)
    kitronik_VIEW128x64.show(Math.sqrt(num), 2)
    serial.writeNumber(Math.sqrt(num))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    num = num - 1
    kitronik_VIEW128x64.show("Raiz Quadrada de " + ("" + ("" + num)), 1, kitronik_VIEW128x64.ShowAlign.Centre)
    kitronik_VIEW128x64.show(Math.sqrt(num), 2)
    serial.writeNumber(Math.sqrt(num))
})
let num = 0
kitronik_VIEW128x64.controlDisplayOnOff(kitronik_VIEW128x64.onOff(true))
kitronik_VIEW128x64.setFontSize(kitronik_VIEW128x64.FontSelection.Normal)
serial.writeLine("ON")
kitronik_VIEW128x64.show("Raiz Quadrada de " + ("" + ("" + num)), 1, kitronik_VIEW128x64.ShowAlign.Centre)
