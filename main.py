import pygame
pygame.init()

environment = pygame.image.load('track6.png')
car = pygame.image.load('car.png')
car = pygame.transform.scale(car, (30, 70))
display = pygame.display.set_mode((1200,400))
clock = pygame.time.Clock()

drive = True
car_x = 155
car_y = 270
view_dist = 30
direction = 'Up'
cam_up_offset = 0
cam_right_offset = 0
speed = 2
view = 255

while drive:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            drive = False

    cam_x = car_x + 15 + cam_right_offset
    cam_y = car_y + 15 + cam_up_offset
    view_up = display.get_at((cam_x, cam_y - view_dist))[0]
    view_down = display.get_at((cam_x, cam_y + view_dist))[0]
    view_right = display.get_at((cam_x + view_dist, cam_y))[0]
    view_left = display.get_at((cam_x - view_dist, cam_y))[0]
    print(view_up, view_right, view_down, view_left)

    if direction == 'Up' and view_up != view and view_left != view and view_right == view:
        direction = 'Right'
        car = pygame.transform.rotate(car, -90)
        cam_right_offset = 35
    elif direction == 'Right' and view_right != view and view_down == view:
        direction = 'Down'
        car = pygame.transform.rotate(car, -90)
        cam_up_offset = 35
        car_x += 35
        cam_right_offset = 0
    elif direction == 'Down' and view_down != view and view_right == view:
        direction = 'Right'
        car = pygame.transform.rotate(car, 90)
        car_y += 35
        cam_up_offset = 0
        cam_right_offset = 35
    elif direction == 'Right' and view_right != view and view_up == view:
        direction = "Up"
        car = pygame.transform.rotate(car, 90)
        car_x += 35
        cam_right_offset = 0
    elif direction == 'Down' and view_down != view and view_left == view:
        direction = 'Left'
        car = pygame.transform.rotate(car, -90)
        car_x -= 35
        car_y += 35
        cam_up_offset = 0
    elif direction == 'Left' and view_left != view and view_up == view:
        direction = 'Up'
        car = pygame.transform.rotate(car, -90)



    if direction == 'Up' and view_up == view:
        car_y -= speed
    elif direction == 'Right' and view_right == view:
        car_x += speed
    elif direction == 'Down' and view_down == view:
        car_y += speed
    elif direction == 'Left' and view_left == view:
        car_x -= speed

    display.blit(environment, (0,0))
    display.blit(car, (car_x, car_y))
    sensor = pygame.draw.circle(display, (0, 0, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
    clock.tick(60)