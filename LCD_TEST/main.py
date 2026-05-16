
#THIS TOO GOT AN ASSIST FROM CLAUDE, MOSTLY TO HELP UNDERSTAND IT WELL


from machine import I2C, Pin
from i2c_lcd import I2cLcd
import time

# ESP32 Pin assignment (for 38-pin NodeMCU)
I2C_SCL = Pin(22)  # SCL pin
I2C_SDA = Pin(21)  # SDA pin
I2C_FREQ = 400000  # 400kHz

# LCD size
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# I2C address (usually 0x27 or 0x3F)
DEFAULT_I2C_ADDR = 0x27

print("Scanning I2C bus...")
i2c = I2C(0, scl=I2C_SCL, sda=I2C_SDA, freq=I2C_FREQ)

# Scan for I2C devices
devices = i2c.scan()
if devices:
    print(f"I2C devices found: {[hex(device) for device in devices]}")
    I2C_ADDR = devices[0]  # Use first device found
else:
    print("No I2C devices found!")
    print("Check your wiring:")
    print("  VCC → 5V (or 3.3V)")
    print("  GND → GND")
    print("  SDA → GPIO21")
    print("  SCL → GPIO22")
    I2C_ADDR = DEFAULT_I2C_ADDR  # Try default anyway

print(f"Using I2C address: {hex(I2C_ADDR)}")

# Initialize LCD
try:
    lcd = I2cLcd(i2c, I2C_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)
    
    # Test 1: Clear and display text
    lcd.clear()
    lcd.putstr("ESP32 LCD Test")
    print("✓ Line 1 displayed")
    
    time.sleep(2)
    
    # Test 2: Second line
    lcd.move_to(0, 1)
    lcd.putstr("MicroPython!")
    print("✓ Line 2 displayed")
    
    time.sleep(3)
    
    # Test 3: Scrolling counter
    lcd.clear()
    lcd.putstr("Counter:")
    
    for i in range(10):
        lcd.move_to(0, 1)
        lcd.putstr(f"Count: {i}      ")  # Extra spaces to clear previous
        print(f"Count: {i}")
        time.sleep(1)
    
    lcd.clear()
    lcd.putstr("Test Complete!")
    print("✓ LCD test finished!")
    
except Exception as e:
    print(f"Error: {e}")
    print("\nTroubleshooting:")
    print("1. Check wiring")
    print("2. Adjust contrast potentiometer on LCD")
    print("3. Try different I2C address (0x27 or 0x3F)")
