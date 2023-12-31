# Clock with alarm for device PicoPad Wi-Fi
This is my example CircuitPython application for device PicoPad with Wi-Fi.
The example shows the current time and date synchronized with NTP.

One alarm can be set. The alarm clock melody is the title theme
from Nintendo's The Legend of Zelda, composed by composer Kōji Kondō
and stored in the melody.py file.

- **Usage:**

First, install CircuitPython on your PicoPad from
https://circuitpython.org/board/pajenicko_picopad/

After installing CircuitPython, copy the entire contents to
the flash memory of PicoPad named CIRCUITPY.
Warning: **Do not use _BOOTSEL_!!!**
For the NTP synchronization feature, you must edit the settings.toml file.
Enter your Wi-Fi SSID and password.

- **Control by buttons:**
```
Up	increase alarm hour
Down	decrease alarm hour
Right	increase alarm minute
Left	decrease alarm minute
A	Day mode	| Green color
B	Night mode	| Red color
X	Switching off display
Y	Maximize the brightness of display.
```
## For more information see:

- https://picopad.eu
- https://circuitpython.org/board/pajenicko_picopad/
- https://circuitpython.org/libraries
- https://pajenicko.cz


## Contact
In case of questions, don't hesitate to contact me via mail damianvcechov@gmail.com.

Damian Čechov [Damien Chekhov]
