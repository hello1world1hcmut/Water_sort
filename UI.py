# import pygame
# from Color import Color
# from Cups_UI import Cups, Cup, Rect_Cup


# class UI:
#     def __init__(self, Cups: Cups):
#         self.Cups = Cups
#         self.count = 0
#         self.path = Cups.path
#         self.active_solve = False
#         self.active_reset = False
#         self.button = pygame.image.load('./button/button.png')
#         pygame.init()
#         self.surface = pygame.display.set_mode((1500, 750))
#         self.surface.fill(Color[0])
#         pygame.display.set_caption('Water sort')
#         self.Cups.surface = self.surface
    
#     def init_display(self):
#         self.surface.fill(Color[0])
#         font_surface = pygame.font.Font(None, 50).render('STEP: ' + str(self.count), None, Color[1])
#         surface_button = pygame.transform.scale(self.button, (120, 120))
#         self.surface.blit(surface_button, (700, 600))
#         self.surface.blit(font_surface, (20, 20))
#         self.Cups.draw()

#     def run(self):
#         self.init_display()
#         pygame.display.update()
#         pygame.time.delay(500)
#         while True:            
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     exit()
#             pos = pygame.mouse.get_pos()
#             if (pos[0] >= 700 and pos[0] <= 820) and (pos[1] >= 600 and pos[1] <= 720):
#                 if pygame.mouse.get_pressed()[0] == 1 and self.active_solve == False:
#                     clone_path = self.path
#                     while len(clone_path) != 0:
#                         self.Cups.move(clone_path[0])
#                         self.count += 1
#                         clone_path = clone_path[1:]
#                         self.init_display()
#                         pygame.display.update()
#                         self.active_solve = True

