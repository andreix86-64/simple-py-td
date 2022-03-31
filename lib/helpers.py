def h_rect_collides_with_point(rx, ry, w, h, px, py):
    return rx <= px <= rx + w and ry <= py <= ry + h

