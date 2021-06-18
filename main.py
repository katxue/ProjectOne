import pygame
import sys

pygame.init()
width = int(pygame.display.Info().current_w / 1.5)
height = int(pygame.display.Info().current_h / 1.5)
screen = pygame.display.set_mode((width, height), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
FPS = 60


def draw_base(surface, start, base_height, base_width):
    start = (start[0], start[1] - base_height)
    rect = (start, (base_width, base_height))
    pygame.draw.rect(surface, (255, 255, 255), rect)


def draw_top(surface, start, num_segments, seg_wt, seg_wb, seg_height, seg_scale):
    pass


def draw_tree(surface, start, base_height, base_width, num_segments, seg_wt, seg_wb, seg_height, seg_scale):
    draw_base(surface, start, base_height, base_width)
    draw_top(surface, start, num_segments, seg_wt, seg_wb, seg_height, seg_scale)


while True:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            width = event.w
            height = event.h
            screen = pygame.display.set_mode((width, height), flags=pygame.RESIZABLE)

    draw_tree(screen, (int(width/2), int(height/2)), 100, 30, 0, 0, 0, 0, 0)
    pygame.display.flip()

