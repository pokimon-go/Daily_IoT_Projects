16/05/2026
# Project Name
LCD SENSOR TEST(A SIMPLE TEST)
## Description
Okay this is just a simple run test it mainly show you have a geneunie LCD not reapoff, and just to see it work for the first time too. it's not much but just a plug and play simply put
## Hardware
So the hardware you need a few(atleast the ones i used), they are already listed in the hardware.md file.
## Software
So for this one you will need only Thonny IDE, simple yet effective for rapid testing and it uses micropython, incase you didn't know
## Setup
It's simple actually:
 1. Go download Thonny IDE from thier website, it's small, and install it
 2. open your installed IDE and also plugin your esp32 via the USB too
 3. click TOOLS -> Options -> Interpriter -> then choose micropython(esp32) & for the port select the option with @/dev/tty/USB0(it's the one for your plugged in usb')
 4. click "install or update micropython"
 5. then the target port is the same(USB0) -> micropython family choose your esp32 type -> variant choose ESP/WROOM, the rest will auto fill
 6. click ok, it will install after close everything and your done
then you can head back to the main window.
IMPORTANT: hopefully your done connecting your esp32 to the lcd appropriaty, otherwise, that's now your homework :)
## Usage
Okay, once done with the setup, now you a ready to test things out, so lets go;
so open three new files and put the code from the 
1. lcd_api.py
2. i2c_lcd.py
3. main.py
into their own tabs and save each one into the micro device with their respective names too and your done 
## Development / How I built it
So once your here, your basically done, just hope onto the main.py and run the code 
## Notes
here, am gonna accept it, for connection of the LCD to the esp32, you have to lookup the respective connection for your esp32 type though, and the different parts of Thonny IDE, but all of that , you learn as you go. 


THANKS, HOPE THE SOFTWARE HELP, SHOUTOUT TO CLAUDE AND RANDOM NERD TUTORIALS FOR ALL THE HELP TOO. NOW YOU CAN GO :) 
