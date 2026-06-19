class Alien:
    total_aliens_created = 0 #class
    health = 3
    
    def __init__(self, location_x, location_y):
        Alien.total_aliens_created += 1
        self.x_coordinate = location_x
        self.y_coordinate = location_y

    def hit(self):
        self.health -= 1
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def teleport(self, location_x, location_y):
        self.x_coordinate = location_x
        self.y_coordinate = location_y
        return self

    def collision_detection(location_x, location_y):
        pass

def new_aliens_collection(positions):
    return [Alien(x, y) for x, y in positions]
