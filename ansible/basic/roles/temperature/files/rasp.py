import RPi.GPIO as GPIO
import time
import logging
import logging.handlers
from systemd.journal import JournalHandler

log = logging.getLogger('temperature')
log.addHandler(logging.handlers.SysLogHandler(address = '/dev/log'))

log.setLevel(logging.INFO)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 100)
p.start(0)
time.sleep(5)
p.ChangeDutyCycle(100)
time.sleep(15)

tFile = open('/sys/class/thermal/thermal_zone0/temp')
temp = float(tFile.read())/1000
tFile.close()
log.info("Temp check started, temperature at start %f", temp)
changeCycle = False
prevCycle = 100
newCycle = 0
while True:
  try:
    tFile = open('/sys/class/thermal/thermal_zone0/temp')
    temp = float(tFile.read())/1000
    tFile.close()
    if temp > 59:
       newCycle = 100
    elif temp > 55:
       newCycle = 75
    elif temp > 49:
       newCycle = 54
    elif temp > 40:
       newCycle = 49
    else:
       newCycle = 47
    if newCycle != prevCycle:
        log.info("Change cycle to %d, temp %f", newCycle, temp)
        prevCycle = newCycle
        p.ChangeDutyCycle(newCycle)
        time.sleep(60)
    if newCycle > 74:
       time.sleep(60)
    time.sleep(5)
  except Exception as err:
    log.error("unknown error occured", err)
    GPIO.cleanup()
    exit