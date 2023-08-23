# SPDX-FileCopyrightText: 2022 Scott Shawcroft for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Print out time based on NTP."""

import board
import displayio
import terminalio
from adafruit_display_text import label
from digitalio import DigitalInOut, Direction, Pull
import simpleio

import time
import rtc

import socketpool
import wifi

import adafruit_ntp
import os

# Import melody from file melody.py
from melody import melody

# Define buttons
btn_down = DigitalInOut(board.SW_DOWN)
btn_down.pull = Pull.UP

btn_up = DigitalInOut(board.SW_UP)
btn_up.pull = Pull.UP

btn_left = DigitalInOut(board.SW_LEFT)
btn_left.pull = Pull.UP

btn_right = DigitalInOut(board.SW_RIGHT)
btn_right.pull = Pull.UP

btn_x = DigitalInOut(board.SW_X)
btn_x.pull = Pull.UP

btn_y = DigitalInOut(board.SW_Y)
btn_y.pull = Pull.UP

btn_a = DigitalInOut(board.SW_A)
btn_a.pull = Pull.UP

btn_b = DigitalInOut(board.SW_B)
btn_b.pull = Pull.UP

# Set Wi-fi in file settings.toml
wifi.radio.connect(
    os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD")
)

# Set current rtc time from NTP server
pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(pool, tz_offset=2)
rtc.RTC().datetime = ntp.datetime
cur_time = time.localtime()

# Set implicite brightness display
board.DISPLAY.brightness = 0.01

display = board.DISPLAY
group = displayio.Group()
font = terminalio.FONT

ctime = "{:02d}:{:02d}:{:02d}".format(cur_time.tm_hour, cur_time.tm_min, cur_time.tm_sec)
ctime_area = label.Label(font, text=ctime, color=0xADFF2F, scale=6)
ctime_area.x = 20
ctime_area.y = 60
group.append(ctime_area)

cdate = "{:02d}.{:02d}.{:04d}".format(cur_time.tm_mday, cur_time.tm_mon, cur_time.tm_year)
cdate_area = label.Label(font, text=cdate, color=0xADFF2F, scale=4)
cdate_area.x = 43
cdate_area.y = 120
group.append(cdate_area)

hour = 00
minute = 00
second = 00

alarm = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
alarm_area = label.Label(font, text=alarm, color=0xADFF2F, scale=3)
alarm_area.x = 95
alarm_area.y = 180
group.append(alarm_area)


while True:

    if (btn_up.value == False):
      hour += 1
      alarm = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
      alarm_area.scale = 3
      alarm_area.text = alarm

    if (btn_left.value == False):
      minute -= 1
      alarm = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
      alarm_area.scale = 3
      alarm_area.text = alarm

    if (btn_right.value == False):
      minute += 1
      alarm = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
      alarm_area.scale = 3
      alarm_area.text = alarm

    if (btn_down.value == False):
      hour -= 1
      alarm = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
      alarm_area.scale = 3
      alarm_area.text = alarm

    if (btn_a.value == False):
      ctime_area.color = 0xADFF2F
      cdate_area.color = 0xADFF2F
      alarm_area.color = 0xADFF2F

    if (btn_b.value == False):
      ctime_area.color = 0xFF0000
      cdate_area.color = 0xFF0000
      alarm_area.color = 0xFF0000

    if (btn_x.value == False):
      board.DISPLAY.brightness = 0

    if (btn_y.value == False):
      board.DISPLAY.brightness = 1

    cur_time = time.localtime()
    ctime = "{:02d}:{:02d}:{:02d}".format(cur_time.tm_hour, cur_time.tm_min, cur_time.tm_sec)
    cdate = "{:02d}.{:02d}.{:04d}".format(cur_time.tm_mday, cur_time.tm_mon, cur_time.tm_year)
    ctime_area.text = ctime
    cdate_area.text = cdate
    board.DISPLAY.show(group)

    if (alarm == ctime):
      ctime_area.text = "!ALARM!"
      cdate_area.text = ""
      alarm_area.text = "Ring Ring"
      board.DISPLAY.show(group)
      for note in melody:
         frequency, duration = note
         simpleio.tone(board.AUDIO, frequency, duration)
         time.sleep(0.05)