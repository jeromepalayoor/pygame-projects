import pygame
import random
import math

pygame.init()
HEIGHT = 600
WIDTH = 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))

def get_angle(A, B, C):
    a2 = (B[0]-C[0])**2 + (B[1]-C[1])**2
    b2 = (A[0]-C[0])**2 + (A[1]-C[1])**2
    c2 = (A[0]-B[0])**2 + (A[1]-B[1])**2
    a = math.acos((b2+c2-a2)/(2*math.sqrt(b2)*math.sqrt(c2)))
    b = math.acos((a2+c2-b2)/(2*math.sqrt(a2)*math.sqrt(c2)))
    c = math.acos((a2+b2-c2)/(2*math.sqrt(a2)*math.sqrt(b2)))
    return math.degrees(a), math.degrees(b), math.degrees(c)

def get_tri():
    while 1:
        points = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)), (random.randint(0, WIDTH), random.randint(0, HEIGHT)), (random.randint(0, WIDTH), random.randint(0, HEIGHT))]
        angles = get_angle(points[0], points[1], points[2])
        if not (angles[0] < 40 or angles[1] < 40 or angles[2] < 40):
            break
    return points

curr = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
points = get_tri()

win.fill((255, 255, 255))
shade = 255
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shade = 255
                win.fill((255, 255, 255))
                curr = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
                points = get_tri()

    for _ in range(100):
        new = random.choice(points)
        curr = ((curr[0] + new[0]) // 2 , (curr[1] + new[1]) // 2)
        pygame.draw.circle(win, (shade, shade, shade), curr, 1)

    shade -= 1
    if shade < 0: shade = 0
    
    pygame.display.update()

pygame.quit()