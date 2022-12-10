"""Test Something"""
import pygame

pygame.init()

font = pygame.font.Font(None, 30)

def debug(info, y=10, x=10):
    display_surface = pygame.display.get_surface()
    text_surf = font.render(info, True, "Black")
    display_surface.blit(text_surf, (x,y))
    