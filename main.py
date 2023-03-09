from smbus import SMBus
import time
address = 0x40
bus = SMBus(1)

# Put device in "normal mode"
bus.write_byte_data(address, 0x00, 0x01)

# Rotate through 3 channels
# bus.write_byte_data(address, 0x0C, 0x01)
# time.sleep(2)
# bus.write_byte_data(address, 0x0C, 0x04)
# time.sleep(2)
# bus.write_byte_data(address, 0x0C, 0x10)
# time.sleep(2)
# bus.write_byte_data(address, 0x0C, 0x15)
# time.sleep(2)
# 
# # Turn off

bus.write_byte_data(address, 0x0C, 0x00)


# Set drive strength
# bus.write_byte_data(address, 0x12, 0x00)
#bus.write_byte_data(address, 0x12, 0x3E)
#bus.write_byte_data(address, 0x0C, 0x55)


