#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedRPM, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Led
from flask import Flask, render_template, g
app = Flask(__name__)

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/open")
def open():
    tank_drive.on_for_rotations(-100, -100, 10)
    # g.door_open = True
    return "OK"

@app.route("/close")
def close():
    tank_drive.on_for_rotations(100, 100, 10)
    # g.door_open = False
    return "OK"

if __name__ == '__main__':
    # Runs the server, if you should play the game, remove debug option
    app.run(debug=True, host='0.0.0.0')
