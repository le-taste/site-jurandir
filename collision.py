def point_over_rect(point_pos, rect, pos):
    left = pos[0]
    right = pos[0] + rect[0]

    top = pos[1]
    bottom = pos[1] + rect[1]

    if (left < point_pos[0]
        and right > point_pos[0]
        and top < point_pos[1]
        and bottom > point_pos[1]):
        return True

    return False

def point_over_circle(point_pos, radius, pos):
    dx = point_pos[0] - pos[0]
    dy = point_pos[1] - pos[1]

    dist_squared = dx * dx + dy * dy

    if (dist_squared < radius * radius): 
        return True

    return False


# type = 0 -> rect
# type = 1 -> circle

class collider:
    def __init__(self, type, pos, shape):
        self.type = type
        self.pos = pos
        self.shape = shape

    def collides_with_point(self, point_pos):
        if (self.type == 0):
            return point_over_rect(point_pos, self.shape, self.pos)
        else:
            return point_over_circle(point_pos, self.shape, self.pos)