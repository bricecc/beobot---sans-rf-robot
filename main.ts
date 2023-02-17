function recule () {
    pins.servoWritePin(AnalogPin.P0, 180)
    pins.servoWritePin(AnalogPin.P13, 0)
}
function stop () {
    pins.servoWritePin(AnalogPin.P0, 90)
    pins.servoWritePin(AnalogPin.P13, 90)
}
input.onButtonPressed(Button.A, function () {
    avance()
})
function demiTour () {
    stop()
    recule()
    basic.pause(500)
    pins.servoWritePin(AnalogPin.P0, 180)
    pins.servoWritePin(AnalogPin.P13, 180)
    basic.pause(500)
    stop()
}
input.onButtonPressed(Button.AB, function () {
    stop()
})
input.onButtonPressed(Button.B, function () {
    recule()
})
function avance () {
    pins.servoWritePin(AnalogPin.P0, 0)
    pins.servoWritePin(AnalogPin.P13, 180)
}
basic.forever(function () {
    avance()
    if (sonar.ping(
    DigitalPin.P8,
    DigitalPin.P12,
    PingUnit.Centimeters
    ) < 10) {
        demiTour()
    }
})
