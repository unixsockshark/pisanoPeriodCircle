
import pygame
import funcs

import pygame
import funcs
import pygame
import funcs

pygame.init()

fibNumbers = []
def calculateFibonacciNumbers():
    fn = 0
    fibNumbers.append(fn)
    fn2 = 1
    for i in range(500):
        fibNumbers.append(fn2)
        fn_next = fn + fn2
        fn = fn2
        fn2 = fn_next
calculateFibonacciNumbers()

display_width = 1280
display_height = 720
cycles = 1
display_size = (display_width, display_height)

screen = pygame.display.set_mode(display_size)

running = True
pygame.display.set_caption("Pisano Circle")

num_nodes = 15

drawn_lines = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cycles += 1

    screen.fill((255, 255, 255))

    circleRadius = 250
    circle_center = (display_width // 2, display_height // 2)  # Center of the screen
    circle = pygame.draw.circle(screen, (0, 0, 0), circle_center, circleRadius, 7)
    funcs.calculateNodes(num_nodes, screen)

    start_pos = funcs.nodes[fibNumbers[cycles] % num_nodes].get('pos')
    end_pos = funcs.nodes[fibNumbers[(cycles + 1) % len(fibNumbers)] % num_nodes].get('pos')
    drawn_lines.append((start_pos, end_pos))

    for line in drawn_lines:
        pygame.draw.line(screen, (0, 0, 0), line[0], line[1])

    pygame.display.flip()

pygame.quit()
