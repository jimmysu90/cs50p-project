import pygame
import project
import classes

images = classes.Images()
settings = classes.Settings()
timers = classes.Timers()
pygame.init()


def test_generate_car():
    test = project.generate_car(255, 285)
    assert test[0].x <= 285
    assert test[0].x >= 255
    assert test[0].y == -80
    assert (
        (test[2] == 5)
        or (test[2] == 6)
        or (test[2] == 7)
        or (test[2] == 8)
        or (test[2] == 9)
        or (test[2] == 10)
    )


def test_spawn_cars():
    test = len(project.spawn_cars(1))
    assert test == 1 or test == 2
    test = len(project.spawn_cars(2))
    assert test == 1 or test == 2
    test = len(project.spawn_cars(3))
    assert test == 1 or test == 2 or test == 3
    test = len(project.spawn_cars(4))
    assert test == 1 or test == 2 or test == 3
    test = len(project.spawn_cars(5))
    assert test == 2 or test == 3 or test == 4
    test = len(project.spawn_cars(6))
    assert test == 2 or test == 3 or test == 4
    test = len(project.spawn_cars(7))
    assert test == 2 or test == 3 or test == 4
    test = len(project.spawn_cars(8))
    assert test == 3 or test == 4
    test = len(project.spawn_cars(9))
    assert test == 3 or test == 4
    test = len(project.spawn_cars(10))
    assert test == 3 or test == 4


def test_handle_cars():
    p = classes.Objects(pygame.Rect(430, 360, 36, 76), images.ambulance)
    non_colliding_car1 = classes.Objects(pygame.Rect(390, 294, 40, 80), images.blue_car)
    non_colliding_car2 = classes.Objects(pygame.Rect(466, 284, 40, 80), images.blue_car)
    colliding_top_left = classes.Objects(pygame.Rect(391, 285, 40, 80), images.blue_car)
    colliding_top_right = classes.Objects(
        pygame.Rect(465, 285, 40, 80), images.blue_car
    )
    colliding_bottom_right = classes.Objects(
        pygame.Rect(465, 361, 40, 80), images.blue_car
    )
    colliding_bottom_left = classes.Objects(
        pygame.Rect(391, 361, 40, 80), images.blue_car
    )

    c = [non_colliding_car1, non_colliding_car2]
    assert project.handle_cars(p, c) == None
    c.append(colliding_top_left)
    assert project.handle_cars(p, c) == colliding_top_left
    c.remove(colliding_top_left)
    c.append(colliding_top_right)
    assert project.handle_cars(p, c) == colliding_top_right
    c.remove(colliding_top_right)
    c.append(colliding_bottom_right)
    assert project.handle_cars(p, c) == colliding_bottom_right
    c.remove(colliding_bottom_right)
    c.append(colliding_bottom_left)
    assert project.handle_cars(p, c) == colliding_bottom_left
    c += [colliding_bottom_right, colliding_top_left, colliding_top_right]
    assert project.handle_cars(p, c) == colliding_bottom_left
