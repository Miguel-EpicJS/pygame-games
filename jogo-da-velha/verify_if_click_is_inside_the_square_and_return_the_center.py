def verify_if_click_is_inside_the_square_and_return_the_center(click):
    if click[0] > 300 and click[0] < 450 and click[1] > 100 and click[1] < 220:
        center = [(300 + 450) / 2, (100 + 220) / 2]
        return center, 0
    elif click[0] > 450 and click[0] < 650 and click[1] > 100 and click[1] < 220:
        center = [(450 + 650) / 2, (100 + 220) / 2]
        return center, 1
    elif click[0] > 650 and click[0] < 800 and click[1] > 100 and click[1] < 220:#
        center = [(650 + 800) / 2, (100 + 220) / 2]
        return center, 2
    elif click[0] > 300 and click[0] < 450 and click[1] > 220 and click[1] < 380:
        center = [(300 + 450) / 2, (220 + 380) / 2]
        return center, 3
    elif click[0] > 450 and click[0] < 650 and click[1] > 220 and click[1] < 380:
        center = [(450 + 650) / 2, (220 + 380) / 2]
        return center, 4
    elif click[0] > 650 and click[0] < 800 and click[1] > 220 and click[1] < 380:#
        center = [(650 + 800) / 2, (220 + 380) / 2]
        return center, 5
    elif click[0] > 300 and click[0] < 450 and click[1] > 380 and click[1] < 500:
        center = [(300 + 450) / 2, (380 + 500) / 2]
        return center, 6
    elif click[0] > 450 and click[0] < 650 and click[1] > 380 and click[1] < 500:
        center = [(450 + 650) / 2, (380 + 500) / 2]
        return center, 7
    elif click[0] > 650 and click[0] < 800 and click[1] > 380 and click[1] < 500:#
        center = [(650 + 800) / 2, (380 + 500) / 2]
        return center, 8

    return False