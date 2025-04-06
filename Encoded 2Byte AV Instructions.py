def encoded(angle, speed, previous_task):
    if not (0 <= angle <= 359) or not (0 <= speed <= 127):
        raise ValueError("Angle must be between 0 and 359, Speed must be between 0 and 127.")
    if previous_task not in (0, 1):
        raise ValueError("Previous task must be 0 (not available) or 1 (available)")
    # combines angle and speed into two bytes, and shifts the angle to the left to make room for speed
    shift_angle = (angle << 7) | speed
    # extracts the upper byte
    byte_1 = (shift_angle >> 8) & 0xFF
    # extracts the lower byte
    byte_2 = ((previous_task << 7) | (speed & 0x7F)) & 0xFF
    print(f"Byte 1: {byte_1} (0x{byte_1:X}), Byte 2: {byte_2} (0x{byte_2:X})")


encoded(45, 60, 1)
