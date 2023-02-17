def recule():
    pins.servo_write_pin(AnalogPin.P0, 180)
    pins.servo_write_pin(AnalogPin.P13, 0)
def stop():
    pins.servo_write_pin(AnalogPin.P0, 90)
    pins.servo_write_pin(AnalogPin.P13, 90)

def on_button_pressed_a():
    avance()
input.on_button_pressed(Button.A, on_button_pressed_a)

def demiTour():
    stop()
    recule()
    basic.pause(500)
    pins.servo_write_pin(AnalogPin.P0, 180)
    pins.servo_write_pin(AnalogPin.P13, 180)
    basic.pause(500)
    stop()

def on_button_pressed_ab():
    stop()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    recule()
input.on_button_pressed(Button.B, on_button_pressed_b)

def avance():
    pins.servo_write_pin(AnalogPin.P0, 0)
    pins.servo_write_pin(AnalogPin.P13, 180)

def on_forever():
    avance()
    if sonar.ping(DigitalPin.P8, DigitalPin.P12, PingUnit.CENTIMETERS) < 10:
        demiTour()
basic.forever(on_forever)
