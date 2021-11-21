from web_search import *
import pygame


# Couleurs de base
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#Setup de la fenetre pygame
pygame.init()
screen = pygame.display.set_mode([700, 500])
screen.fill(BLACK)
pygame.display.set_caption("Projet")
RUN = True
logged_in = False




##----------------------------------------------------------------------##
##Calculs et fonctionnement de notre ordinateur (si on garde cette idée)##
##----------------------------------------------------------------------##


class OperatingSystem:
  def __init__(self):
    user = input('User: ')
    password = input('Password: ')
    if password == '0000' and user == 'User1':
      print('Welcome back ' + user + '!')
      return
    else:
      print('Wrong !')
      return



##------------------------------##
##---Boucle Principale du Jeu---##
##------------------------------##

while RUN:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      RUN= False
    if event.type == pygame.KEYDOWN:
      if not(logged_in):
        os = OperatingSystem()
        logged_in = True
  
      action = input('Command:')
      if action == '-randompage':
        load_page(random_page())
        action = ''
      if action == '-search':
        page = input('Search:')
        load_page(page)
        action = ''


pygame.quit()
