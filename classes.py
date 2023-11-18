import pygame
import time
import random

pygame.init()


class Objects:
    def __init__(self, hit_box, image, velocity=0, brake=0):
        self.hit_box = hit_box
        self.image = image
        self.velocity = velocity
        self.brake = brake


class Timers:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.elapsed_time = 0
        self.spawn_timer = 0
        self.level_timer = 0
        self.bg_timer = 0


class Images:
    def __init__(self):
        self.backdrops = [
            "backdrop1.png",
            "backdrop2.png",
            "backdrop3.png",
            "backdrop4.png",
            "backdrop5.png",
            "backdrop6.png",
        ]
        self.roads = ["road4.png", "road5.png", "road6.png", "road7.png"]
        self.TRANSPARENT = (0, 255, 0)
        self.ambulance = pygame.image.load("ambulance.png")
        self.yellow_car = pygame.image.load("yellow_car.png")
        self.blue_car = pygame.image.load("blue_car.png")
        self.green_car = pygame.image.load("green_car.png")
        self.level = pygame.image.load("level.png")
        self.time = pygame.image.load("time.png")
        self.pause = pygame.image.load("pause.png")
        self.game_over = pygame.image.load("gameover.png")
        self.background1 = pygame.image.load(random.choice(self.roads))
        self.background2 = pygame.image.load(random.choice(self.roads))
        self.backdrop1 = pygame.image.load(random.choice(self.backdrops))
        self.backdrop2 = pygame.image.load(random.choice(self.backdrops))
        self.title = pygame.image.load("title.png")

        self.ambulance.set_colorkey(self.TRANSPARENT)
        self.yellow_car.set_colorkey(self.TRANSPARENT)
        self.blue_car.set_colorkey(self.TRANSPARENT)
        self.green_car.set_colorkey(self.TRANSPARENT)
        self.level.set_colorkey(self.TRANSPARENT)


class Settings:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 700
        self.ROADSIDE = 250
        self.game_over = False
        self.pause = True
        self.velocity = 5
        self.brake = 6
        self.level = 1
        self.cars = list()
        self.running = True
        self.bg1 = pygame.Rect(self.ROADSIDE, 0, 1, 1)
        self.bg2 = pygame.Rect(self.ROADSIDE, 0 - self.HEIGHT, 1, 1)
        self.bd1 = pygame.Rect(0, 0, 1, 1)
        self.bd2 = pygame.Rect(0, 0 - self.HEIGHT, 1, 1)
        self.score = 0
        self.highscore = 0
