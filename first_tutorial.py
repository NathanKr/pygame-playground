# https://www.pygame.org/docs/tut/PygameIntro.html
import sys, pygame

pygame.init()
size = width, height = 640, 480
pos_ofset = [1, 1]
black = 0, 0, 0

# set_mode Initialize a window or screen for display. return Surface 
screen = pygame.display.set_mode(size)
#  ball is type Surface : https://www.pygame.org/docs/ref/surface.html
ball = pygame.image.load("intro_ball.gif") 
# ballreact is type Rect : Rect(left, top, width, height)
# https://www.pygame.org/docs/ref/rect.html
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    # move return new Rect , https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move
    ballrect = ballrect.move(pos_ofset)
    if ballrect.left < 0 or ballrect.right > width:
        pos_ofset[0] = -pos_ofset[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        pos_ofset[1] = -pos_ofset[1]

    # fill Surface with a solid color , fill(color, rect=None, special_flags=0) -> Rect
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
    screen.fill(black)

    # draw one image onto another blit(source, dest, area=None, special_flags=0) -> Rect
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    screen.blit(ball, ballrect)

    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    # Update the full display Surface to the screen . flip() -> None
    pygame.display.flip()