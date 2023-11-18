import pygame
import random
import time
import classes

pygame.init()
pygame.font.init()

settings = classes.Settings()
images = classes.Images()
timers = classes.Timers()
player = classes.Objects(
    pygame.Rect(settings.ROADSIDE + 180, 360, 36, 76),
    images.ambulance,
    settings.velocity,
    settings.brake,
)

SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Highway Cruise")
FONT = pygame.font.SysFont("drugsther", 48)

cars = list()
level = 1


def main():
    while settings.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings.running = False
                break

        run_game()


def display():
    global cars
    global level
    SCREEN.blit(images.backdrop1, settings.bd1)
    SCREEN.blit(images.backdrop2, settings.bd2)
    SCREEN.blit(images.background1, settings.bg1)
    SCREEN.blit(images.background2, settings.bg2)

    if len(cars) > 0:
        for car in cars:
            SCREEN.blit(car.image, car.hit_box)

    player_display = [player.hit_box.x - 2, player.hit_box.y - 2]
    SCREEN.blit(player.image, player_display)
    time_text = FONT.render(f"{round(timers.elapsed_time): 05d}", 1, "black")
    level_text = FONT.render(f"{level: 03d}", 1, "black")
    SCREEN.blit(images.level, (0, settings.HEIGHT - 210))
    SCREEN.blit(images.time, (settings.WIDTH - 180, settings.HEIGHT - 210))
    SCREEN.blit(level_text, (60, settings.HEIGHT - 125))
    SCREEN.blit(time_text, (settings.WIDTH - 140, settings.HEIGHT - 125))

    if settings.pause:
        SCREEN.blit(images.title, (0, 10))
        SCREEN.blit(images.pause, (0, 50))

    if settings.game_over:
        SCREEN.blit(images.game_over, (settings.WIDTH / 2 - 150, 150))

    pygame.display.flip()


def run_game():
    global cars
    global level

    keys = pygame.key.get_pressed()

    if settings.pause:
        if keys[pygame.K_RETURN]:
            settings.pause = False
            timers.start_time = time.time()

    if not settings.pause and not settings.game_over:
        timers.bg_timer += timers.clock.tick(60)
        timers.spawn_timer += timers.clock.tick(60)
        timers.level_timer += timers.clock.tick(60)
        timers.elapsed_time = time.time() - timers.start_time
        handle_bg()

        if len(cars) > 0:
            collision = handle_cars(player, cars)
            if collision:
                settings.game_over = True

        if (
            keys[pygame.K_RIGHT]
            and player.hit_box.x < settings.WIDTH - settings.ROADSIDE - 40
        ):
            player.hit_box.x += player.velocity
        if keys[pygame.K_LEFT] and player.hit_box.x > settings.ROADSIDE:
            player.hit_box.x -= player.velocity
        if keys[pygame.K_UP] and player.hit_box.y > 0:
            player.hit_box.y -= player.velocity
        if keys[pygame.K_SPACE] and player.hit_box.y < settings.HEIGHT - 80:
            player.hit_box.y += player.brake

        if timers.spawn_timer > (3000 - min(level, 3) * 500):
            cars += spawn_cars(level)
            timers.spawn_timer = 0

        if timers.level_timer > 4000 and level < 10:
            level += 1
            timers.level_timer = 0

    display()


def spawn_cars(lvl):
    new_cars = list()
    lanes_avail = [1, 2, 3, 4, 5]

    if lvl == 1:
        r = random.choices([1, 2], weights=[5, 5])[0]
    elif lvl == 2:
        r = random.choices([1, 2], weights=[2, 8])[0]
    elif lvl == 3:
        r = random.choices([1, 2, 3], weights=[2, 6, 2])[0]
    elif lvl == 4:
        r = random.choices([1, 2, 3], weights=[1, 4, 5])[0]
    elif lvl == 5:
        r = random.choices([2, 3, 4], weights=[4, 5, 1])[0]
    elif lvl == 6:
        r = random.choices([2, 3, 4], weights=[2, 5, 3])[0]
    elif lvl == 7:
        r = random.choices([2, 3, 4], weights=[1, 4, 5])[0]
    elif lvl == 8:
        r = random.choices([3, 4], weights=[5, 5])[0]
    elif lvl == 9:
        r = random.choices([3, 4], weights=[3, 7])[0]
    else:
        r = random.choices([3, 4], weights=[1, 9])[0]

    for _ in range(r):
        lane = random.choice(lanes_avail)
        if lane == 1:
            new_cars.append(
                classes.Objects(
                    *generate_car(settings.ROADSIDE + 5, settings.ROADSIDE + 35)
                )
            )
            lanes_avail.remove(1)

        elif lane == 2:
            new_cars.append(
                classes.Objects(
                    *generate_car(settings.ROADSIDE + 85, settings.ROADSIDE + 115)
                )
            )
            lanes_avail.remove(2)

        elif lane == 3:
            new_cars.append(
                classes.Objects(
                    *generate_car(settings.ROADSIDE + 163, settings.ROADSIDE + 195)
                )
            )
            lanes_avail.remove(3)

        elif lane == 4:
            new_cars.append(
                classes.Objects(
                    *generate_car(settings.ROADSIDE + 244, settings.ROADSIDE + 274)
                )
            )
            lanes_avail.remove(4)

        else:
            new_cars.append(
                classes.Objects(
                    *generate_car(settings.ROADSIDE + 319, settings.ROADSIDE + 355)
                )
            )
            lanes_avail.remove(5)

    return new_cars


def generate_car(x1, x2):
    car = pygame.Rect(random.randint(x1, x2), -80, 40, 80)
    car_colour = random.choice(["green", "blue", "yellow"])

    if car_colour == "green":
        image = images.green_car
    elif car_colour == "blue":
        image = images.blue_car
    else:
        image = images.yellow_car

    car_v = random.randint(5, 10)
    return [car, image, car_v]


def handle_bg():
    if timers.bg_timer >= 1:
        settings.bg1.y += 15
        settings.bg2.y += 15
        settings.bd1.y += 15
        settings.bd2.y += 15

    if settings.bg1.y > settings.HEIGHT:
        settings.bg1.y = 0 - settings.HEIGHT + 15
        settings.bd1.y = 0 - settings.HEIGHT + 15
        images.background1 = pygame.image.load(random.choice(images.roads))
        images.backdrop1 = pygame.image.load(random.choice(images.backdrops))
    if settings.bg2.y > settings.HEIGHT:
        settings.bg2.y = 0 - settings.HEIGHT + 15
        settings.bd2.y = 0 - settings.HEIGHT + 15
        images.background2 = pygame.image.load(random.choice(images.roads))
        images.backdrop2 = pygame.image.load(random.choice(images.backdrops))


def handle_cars(p, c):
    for car in c:
        if p.hit_box.colliderect(car.hit_box):
            return car
        car.hit_box.y += car.velocity
        if car.hit_box.y > settings.HEIGHT:
            cars.remove(car)


if __name__ == "__main__":
    main()
