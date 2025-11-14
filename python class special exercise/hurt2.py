for y in range(15, -15, -1):
    line = ""
    for x in range(-30, 30):

        scaled_x = x * 0.04
        scaled_y = y * 0.1

        if ((scaled_x**2 + scaled_y**2 - 1) ** 3 - scaled_x**2 * scaled_y**3) <= 0:
            line += "♥"
        else:
            line += " "
    print(line)
