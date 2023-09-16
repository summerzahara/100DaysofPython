import colorgram

def create_color_list():
    colors = colorgram.extract('image.jpg',25)

    my_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_tuple = (r, g, b)
        my_colors.append(rgb_tuple)

    print(my_colors)

color_list = [(58, 105, 148), (222, 234, 229), (225, 202, 110), (133, 85, 57), (220, 147, 74), (231, 224, 203), (143, 178, 201), (195, 145, 171), (235, 221, 231), (141, 78, 102), (212, 90, 65), (135, 181, 137), (64, 109, 91), (188, 82, 119), (151, 134, 66), (64, 157, 95), (43, 156, 190), (183, 191, 202), (216, 176, 191), (108, 121, 157), (7, 58, 104), (13, 68, 123), (156, 28, 38), (231, 174, 163)]