import pygame, time

pygame.init()

BASE_COLOR = (32,194,14)
BLACK = (0, 0, 0)
GREY = (211,211,211)
BLUE_GREY = (102, 153, 204)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173,216,230)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


resolution = (600,400)
screen = pygame.display.set_mode(resolution)

def render_text(text: str,pos: tuple,color: tuple = WHITE,size: int = 30):
  '''
  Fonction qui permet d\'afficher du texte.
  Prend en argument le texte (str) et sa position (tuple)
  '''
  pygame.font.init()
  font = pygame.font.SysFont('Comic Sans MS', size)
  text = font.render(text, True, color)
  screen.blit(text,pos)


def render_image(image_name: str,pos: tuple,size: tuple):
  '''
  Fonction qui permet d\'afficher une image.
  Prend en argument le nom de l'image (str), sa position (tuple), et sa taille (tuple)'''
  loaded_img= pygame.image.load(image_name)
  loaded_img = pygame.transform.scale(loaded_img, size)
  screen.blit(loaded_img, pos + size)


def render_rectangle(color: tuple,size: tuple,pos: tuple):
  '''
  Fonction qui permet d\'afficher un rectangle.
  Prend en argument la couleur (un tuple), sa taille (tuple), et sa position (tuple)'''
  pygame.draw.rect(screen, color, pygame.Rect(pos + size))


def render_circle(color: tuple,radius: int,pos: tuple):
  '''
  Fonction qui permet d\'afficher un cercle.
  Prend en argument la couleur (un tuple), son rayon (int), et sa position (tuple)
  '''
  pygame.draw.circle(screen, color, pos, radius)

def check_interaction(clickpos: tuple, wanted_area: tuple, wanted_pages: list, page: str):
  '''
  Fonction qui prend en parametre la position de la souris au moment du click que l'on check et qui la compare avec la zone que l'on veut sous forme de tuple - (x1, x2,y1,y2)
  Compare aussi la page du jeu et la page dans lesquelles le bouton marche. 
  La fonction renvoi True ou False selon si la souris est bien a l'endroit voulu
  '''
  if page in wanted_pages:
    if wanted_area[0]<=clickpos[0]<=wanted_area[1] and wanted_area[2]<=clickpos[1]<=wanted_area[3]:
      return True
    else:
      return False
  else:
    return False

def render_time():
  '''
  Affiche l'heure
  '''
  render_text(time.strftime("%Y-%m-%d"),(522,385),BLACK,20)
  render_text(time.strftime("%H:%M"),(520,355),BLACK,40)