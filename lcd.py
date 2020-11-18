import board
import time
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.color = [100, 0, 0]
lcd.message = "Hello\nFrom VS Code"
time.sleep(3)

lcd.color = [100, 0, 0]
lcd.blink = 1
lcd.clear()
lcd.message = "Thanks for\nreading"
time.sleep(3)

# Turn off LCD backlights and clear text
lcd.color = [0, 0, 0]
lcd.clear()
