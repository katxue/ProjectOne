import pygame
import sys

pygame.init()
width = int(pygame.display.Info().current_w / 1.5)
height = int(pygame.display.Info().current_h / 1.5)
screen = pygame.display.set_mode((width, height), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
FPS = 60


def to_ints(coords):
    return [(int(c[0]), int(c[1])) for c in coords]


def calc_base(start, base_width, base_height, color):
    top_left = (start[0], start[1] - base_height)
    rect = (top_left, (base_width, base_height))
    return color, rect


def calc_trapezoid(start, seg_wt, seg_wb, seg_height, base_width, base_height):
    x = start[0] + ((base_width - seg_wb)/2)
    y = start[1] - base_height
    trapezoid = ((x, y),  # Bottom left
                 (seg_wb + x, y),  # Bottom right
                 (x + ((seg_wb + seg_wt) / 2), y - seg_height),  # Top right
                 (x + ((seg_wb - seg_wt) / 2), y - seg_height))  # Top left

    return trapezoid


def draw_base(surface, start, base_width, base_height):
    color, rect = calc_base(start, base_width, base_height, (255, 255, 255))
    pygame.draw.rect(surface, color, rect)


def draw_top(surface, start, num_segments, seg_wt, seg_wb, seg_height, seg_scale, base_width, base_height):
    trapezoid = calc_trapezoid(start, seg_wt, seg_wb, seg_height, base_width, base_height)
    pygame.draw.polygon(surface, (255, 255, 255), trapezoid, 3)


def draw_tree(surface: pygame.Surface, start: (int, int), base_width: int, base_height: int, num_segments: int,
              seg_wt: int, seg_wb: int, seg_height: int, seg_scale: float):
    """
    :param surface: pygame.Surface
    :param start: Bottom left (x, y) coordinate of the tree base
    :param base_height: Height (y) of the tree base
    :param base_width: Width (x) of the tree base
    :param num_segments: Number of top trapezoid segments (last one is triangle)
    :param seg_wt: Top width of first (largest) trapezoid
    :param seg_wb: Bottom width of first trapezoid
    :param seg_height: Height of first trapezoid
    :param seg_scale: Percentage that next (higher, smaller) trapezoid is from previous float (0, 1)
    :return: None
    """

    draw_base(surface, start, base_width, base_height)
    draw_top(surface, start, num_segments, seg_wt, seg_wb, seg_height, seg_scale, base_width, base_height)


def main(screen, width, height):
    while True:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.VIDEORESIZE:
                width = event.w
                height = event.h
                screen = pygame.display.set_mode((width, height), flags=pygame.RESIZABLE)

        draw_tree(screen, (int(width/2), int(height/2)), 30, 100, 0, 80, 220, 50, 0)
        pygame.display.flip()


if __name__ == '__main__':
    main(screen, width, height)
