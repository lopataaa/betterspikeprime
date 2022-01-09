


from spike import Button, ColorSensor, Motor, MotorPair, PrimeHub
from spike.control import Timer, wait_until
from math import *
import uasyncio
import sys
import utime as time
from spike.operator import * 

defaultTreshold = 40
defaultSpeed = 40

hub = PrimeHub()

m = MotorPair('A', 'B')
mL = Motor('A')
mR = Motor('B')
mLe = Motor('E')
mRe = Motor('F')
sL = ColorSensor('C')
sR = ColorSensor('D')
sR.defaultTreshold = defaultTreshold
sL.defaultTreshold = defaultTreshold

defaultMeasuringMotor = mL

#set the default speed
motors = [mL, mR, mLe, mRe]
for motor in motors:
    motor.set_default_speed(defaultSpeed)

#helper functions
#monkey-patching functions, its bad but it works
#https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance

#with open('/_api/control.py', 'r') as f:
#    print(f.read())


def uwu():
    print('uwu <3')
    print('- lopatka')


def wait(ms):
    return time.sleep(ms/1000)

#motorPair

#motors
def waitForDegreesR(degrees, reset=False):
    self = mR
    if reset:
        self.set_degrees_counted(0)
    while abs(degrees) >= abs(self.get_degrees_counted()):
        pass
    return
mR.wait_for_degrees = waitForDegreesR
del globals()['waitForDegreesR']
def waitForDegreesRe(degrees, reset=False):
    self = mRe
    if reset:
        self.set_degrees_counted(0)
    while abs(degrees) >= abs(self.get_degrees_counted()):
        pass
    return
mRe.wait_for_degrees = waitForDegreesRe
del globals()['waitForDegreesRe']

def waitForDegreesL(degrees, reset=False):
    self = mL
    if reset:
        self.set_degrees_counted(0)
    while abs(degrees) >= abs(self.get_degrees_counted()):
        pass
    return
mL.wait_for_degrees = waitForDegreesL
del globals()['waitForDegreesL']
def waitForDegreesLe(degrees, reset=False):
    self = mLe
    if reset:
        self.set_degrees_counted(0)
    while abs(degrees) >= abs(self.get_degrees_counted()):
        pass
    return
mLe.wait_for_degrees = waitForDegreesLe
del globals()['waitForDegreesLe']

def runForDegrees(degrees, speed=None, stop=True):
    speed = speed or defaultSpeed
    mL.set_degrees_counted(0)
    m.start_tank(speed, speed)
    while abs(degrees) >= abs(mL.get_degrees_counted()):
        pass
    if stop:
        m.stop()
    return
m.run_for_degrees = runForDegrees
del globals()['runForDegrees']

def runForDegreesL(degrees, speed=None, stop=True):
    speed = speed or defaultSpeed
    self = mL
    self.set_degrees_counted(0)
    self.start(-speed)
    while abs(degrees) >= abs(self.get_degrees_counted()):
        pass
    if stop:
        self.stop()
    return
mL.run_for_degrees = runForDegreesL
del globals()['runForDegreesL']
def runForDegreesLe(degrees, speed=None, stop=True):
    speed = speed or defaultSpeed
    self = mLe
    self.set_degrees_counted(0)
    self.start(speed)
    while abs(degrees) >= abs(self.get_degrees_counted()):
        pass
    if stop:
        self.stop()
    return
mLe.run_for_degrees = runForDegreesLe
del globals()['runForDegreesLe']


def runForDegreesR(degrees, speed=None, stop=True):
    speed = speed or defaultSpeed
    self = mR
    self.set_degrees_counted(0)
    self.start(speed)
    while abs(degrees) >= abs(self.get_degrees_counted()):
        pass
    if stop:
        self.stop()
    return
mR.run_for_degrees = runForDegreesR
del globals()['runForDegreesR']
def runForDegreesRe(degrees, speed=None, stop=True):
    speed = speed or defaultSpeed
    self = mRe
    self.set_degrees_counted(0)
    self.start(speed)
    while abs(degrees) >= abs(self.get_degrees_counted()):
        pass
    if stop:
        self.stop()
    return
mRe.run_for_degrees = runForDegreesRe
del globals()['runForDegreesRe']

def moveForDegrees(steering, degrees, speed=None, stop=True):
    speed = speed or defaultSpeed
    mL.set_degrees_counted(0)
    m.start(steering, speed)
    while abs(degrees) >= abs(mL.get_degrees_counted()):
        pass
    if stop:
        m.stop()
    return
m.move_for_degrees = moveForDegrees
del globals()['moveForDegrees']

def turnL(angle, speed=None):
    speed = speed or defaultSpeed
    self = mL
    self.run_for_degrees((360*((70.3*angle)/360))/27.6, speed=speed) ## <== tohle dìlal dan kdyžtak to je na nìj
    return
mL.turn = turnL
del globals()['turnL']
def turnR(angle, speed=None):
    speed = speed or defaultSpeed
    self = mR
    self.run_for_degrees((360*((70.3*angle)/360))/27.6, speed=speed) ## <== tohle dìlal dan kdyžtak to je na nìj
    return
mR.turn = turnR
del globals()['turnR']

def lineAlignment(speed=15, duration=6, treshold=None):
    '''self = m
    t = Timer()
    while t.now() < duration:
        if sL.get_reflected_light() > defaultTreshold and sR.get_reflected_light() > defaultTreshold:
            self.start_tank(speed, speed)
        elif sL.get_reflected_light() < defaultTreshold and sR.get_reflected_light() > defaultTreshold:
            self.start_tank(-speed, speed)
        elif sL.get_reflected_light() > defaultTreshold and sR.get_reflected_light() < defaultTreshold:
            self.start_tank(speed, -speed)
        elif sL.get_reflected_light() < defaultTreshold and sR.get_reflected_light() < defaultTreshold:
            self.start_tank(-speed, -speed)
    m.stop()'''
    '''\
    ### Ta vìc èórnutá z youtube
    b=sL
    f=sR
    m.start_tank(speed, speed)
    def a():
        return b.get_reflected_light() < defaultTreshold or f.get_reflected_light() < defaultTreshold
    wait_until(a)
    m.stop()
    if b.get_reflected_light() < defaultTreshold:
        m.start_tank(0, speed)
        wait_until(f.get_reflected_light, less_than, 50)
        m.start_tank(-speed, 0)
        wait_until(b.get_reflected_light, greater_than, 50)
        m.start_tank(0, -speed)
        wait_until(f.get_reflected_light, less_than, 50)
        m.start_tank(speed, 0)
        wait_until(b.get_reflected_light, greater_than, 50)
        m.start_tank(0, speed)
        wait_until(f.get_reflected_light, less_than, 50)
    else:
        m.start_tank(speed, 0)
        wait_until(b.get_reflected_light, less_than, 50)
        m.start_tank(0, -speed)
        wait_until(f.get_reflected_light, greater_than, 50)
        m.start_tank(-speed, 0)
        wait_until(b.get_reflected_light, greater_than, 50)
        m.start_tank(0, speed)
        wait_until(f.get_reflected_light, less_than, 50)
        m.start_tank(speed, 0)
        wait_until(b.get_reflected_light, less_than, 50)
    def a():
        return b.get_reflected_light() < 50 or f.get_reflected_light() < 50
    wait_until(a)
    m.stop()
    if b.get_reflected_light() < 50:
        m.start_tank(0, speed)
        wait_until(f.get_reflected_light, less_than, 50)
        m.start_tank(-speed, 0)
        wait_until(b.get_reflected_light, greater_than, 50)
        m.start_tank(0, -speed)
        wait_until(f.get_reflected_light, greater_than, 50)
        m.start_tank(speed, 0)
        wait_until(b.get_reflected_light, less_than, 50)
        m.start_tank(0, speed)
        wait_until(f.get_reflected_light, less_than, 50)
    else:
        m.start_tank(speed, 0)
        wait_until(b.get_reflected_light, less_than, 50)
        m.start_tank(0, -speed)
        wait_until(f.get_reflected_light, greater_than, 50)
        m.start_tank(-speed, 0)
        wait_until(b.get_reflected_light, greater_than, 50)
        m.start_tank(0, speed)
        wait_until(f.get_reflected_light, less_than, 50)
        m.start_tank(speed, 0)
        wait_until(b.get_reflected_light, less_than, 50)
    m.stop()'''
    '''
    # vìc èórnutá od marèka
    treshold = treshold or defaultTreshold
    
    for i in range(duration):
        m.start_tank(speed,speed)
        def temp():
            return sL.get_reflected_light() < treshold or sR.get_reflected_light() < treshold
        wait_until(temp)
        if sL.get_reflected_light() < treshold:
            mL.stop()
            mR.start(speed)
            wait_until(sR.get_reflected_light, less_than, treshold)
            mR.stop()
        elif sR.get_reflected_light() < treshold:
            mL.start(-speed)
            wait_until(sL.get_reflected_light, less_than, treshold)
            mL.stop()
        wait(1000)
        m.start_tank(-speed,-speed)
        def temp():
            return sL.get_reflected_light() > treshold or sR.get_reflected_light() > treshold
        wait_until(temp)
        if sL.get_reflected_light() > treshold:
            mR.start(-speed)
            wait_until(sR.get_reflected_light, greater_than, treshold)
            mR.stop()
        elif sR.get_reflected_light() > treshold:
            mL.start(-speed)
            wait_until(sL.get_reflected_light, greater_than, treshold)
            mL.stop()
    m.stop()
    return
    treshold = treshold or defaultTreshold
    for i in range(10):

        m.start_tank(speed, speed)
        while sL.get_reflected_light() > treshold or sR.get_reflected_light() > treshold:

            if(sL.get_reflected_light() < treshold):
                mL.start(-speed)
            if(sR.get_reflected_light() < treshold):
                mR.start(speed)
        m.start_tank(-speed, -speed)
        while sL.get_reflected_light() < treshold or sR.get_reflected_light() < treshold:

            if(sL.get_reflected_light() > treshold):
                mL.start(speed)
            if(sR.get_reflected_light() > treshold):
                mR.start(-speed)'''
    '''
    treshold = treshold or defaultTreshold
    t = Timer()
    while t.now() < duration:
        if sR.get_reflected_light() > treshold:
            mR.start(speed)
        else:
            mR.start(0)
        if sL.get_reflected_light() > treshold:
            mL.start(-speed)
        else:
            mL.start(0)
    m.stop()'''
    '''
    #pjavlobva veruze
    m.start_tank(speed, speed);
    wait_until(lambda: sL.get_reflected_light() < 50 or sR.get_reflected_light() < 50)
    m.stop()
    for i in range(1, 5):
        m.rfd(50, speed=-speed);
        if sL.get_reflected_light() > 50:
            m.start_tank(int(speed / i), int(-speed / i))
            wait_until(sR.get_reflected_light, greater_than, 50)
            m.stop()
        elif sR.get_reflected_light() > 50:
            m.start_tank(int(-speed / i), int(speed / i))
            wait_until(sL.get_reflected_light, greater_than, 50)
            m.stop()
        m.rfd(50, speed=speed);
'''

m.line_alignment = lineAlignment
del globals()['lineAlignment']


def followLineWithBothSensors(degrees, speedOnBlack=0, speedOnWhite=20):
    self = m
    mL.set_degrees_counted(0)
    while(-mL.get_degrees_counted() < degrees):
        if sL.get_reflected_light() > defaultTreshold and sR.get_reflected_light() > defaultTreshold:
            self.start_tank(speedOnWhite, speedOnWhite)
        elif sL.get_reflected_light() < defaultTreshold and sR.get_reflected_light() > defaultTreshold:
            self.start_tank(speedOnBlack, speedOnWhite)
        elif sL.get_reflected_light() > defaultTreshold and sR.get_reflected_light() < defaultTreshold:
            self.start_tank(speedOnWhite, speedOnBlack)
        elif sL.get_reflected_light() < defaultTreshold and sR.get_reflected_light() < defaultTreshold:
            self.start_tank(speedOnBlack, speedOnBlack)
        self.stop()
m.follow_line = followLineWithBothSensors
del globals()['followLineWithBothSensors']

def followLineLeftSensorRightSideOfLine(speed, stopConditionHelperFunction, *args, treshold=None):
    treshold = treshold or defaultTreshold
    self = sL
    defaultMeasuringMotor.set_degrees_counted(0)
    while not stopConditionHelperFunction(*args, treshold=treshold):
        if sL.get_reflected_light() < treshold: #is blek
            m.start_tank(speed, 0)
        elif sL.get_reflected_light() > treshold: #is wajt
            m.start_tank(0, speed)
    return
mL.follow_line_right = followLineLeftSensorRightSideOfLine
del globals()['followLineLeftSensorRightSideOfLine']

#colorsensors
def addSensorsObject(sensorL, sensorR, motorObject):
    motorObject.sL = sensorL
    motorObject.sR = sensorR
    return

def waitForBlackR():
    self = sR
    while sR.get_reflected_light() > self.defaultTreshold:
        pass
    return
sR.wait_for_black = waitForBlackR
del globals()['waitForBlackR']
def waitForBlackL():
    self = sL
    while sR.get_reflected_light() > self.defaultTreshold:
        pass
    return
sL.wait_for_black = waitForBlackL
del globals()['waitForBlackL']


def waitForWhiteR():
    self = sR
    while sR.get_reflected_light() < self.defaultTreshold:
        pass
    return
sR.wait_for_white = waitForWhiteR
del globals()['waitForWhiteR']
def waitForWhiteL():
    self = sL
    while sR.get_reflected_light() < self.defaultTreshold:
        pass
    return
sL.wait_for_white = waitForWhiteL
del globals()['waitForWhiteL']
#pass colorsensor objects to motors and motorpair objects
addSensorsObject(sL, sR, m)
addSensorsObject(sL, sR, mL)
addSensorsObject(sL, sR, mR)
del globals()['addSensorsObject']



### Condition Helper Functions

def TrueOnSensorBlackAndDegrees(sensor, degrees, treshold=None):
    # Don't forget to reset degrees before first calling this function or else its gonna be useless
    # Call this -> defaultMeasuringMotor.set_degrees_counted(0)
    treshold = treshold or defaultTreshold
    return sensor.get_reflected_light < defaultTreshold and defaultMeasuringMotor.get_degrees_counted() >= degrees



# Launcher

class launcher:
    def __init__(self):
        pass
    color_running = 'green'
    color_idle = 'azure'
    color_onpress = 'blue'
    missions = []
    def defineMission(self, *args):
        for i in args:
            self.missions.append(i)
    def launch(self):
        #prvotni hodnota
        currentval = 1
        hub.light_matrix.write(currentval)
        hub.status_light.on(self.color_idle)
        while True:
            if hub.left_button.is_pressed():
                hub.status_light.on(self.color_onpress)
                if currentval == len(self.missions):
                    #pokud je to posledni vec v arrayi zacit od 1
                    currentval = 1
                    hub.light_matrix.write(currentval)
                else:
                    #pricteni 1
                    currentval += 1
                    hub.light_matrix.write(currentval)
                #cekani na tu nez se to tlacitko pusti
                while hub.left_button.is_pressed():
                    pass
            #spusteni mise
            if hub.right_button.is_pressed():
                hub.status_light.on(self.color_onpress)
                while hub.right_button.is_pressed():
                    pass
                hub.status_light.on(self.color_running)
                self.missions[currentval-1]()
                #spusteni funkce
                if currentval == len(self.missions):
                    currentval = 1
                    hub.light_matrix.write(currentval)
                else:
                    currentval += 1
                    hub.light_matrix.write(currentval)
                while hub.right_button.is_pressed():
                    hub.status_light.on(self.color_onpress)
                    pass
            hub.status_light.on(self.color_idle)

def defineAlias(original, alias):
    alias = original

### Predefined Aliases / Function name abbreviations
m.rfd = m.run_for_degrees
mL.rfd = mL.run_for_degrees
mR.rfd = mR.run_for_degrees
mLe.rfd = mLe.run_for_degrees
mRe.rfd = mRe.run_for_degrees

m.mfd = m.move_for_degrees

speed = defaultSpeed
m.rfdan = m.run_for_degrees
mL.rfdan = mL.run_for_degrees
mR.rfdan = mR.run_for_degrees
mLe.rfdan = mLe.run_for_degrees
mRe.rfdan = mRe.run_for_degrees


