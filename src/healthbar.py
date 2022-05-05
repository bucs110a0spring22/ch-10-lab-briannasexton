import pygame

class HealthBar:
  def __init__(self, screen):
    """
    Creates the health bar feature at the top of user screen
    args: self is health bar
    returns: none
    """
    print("Healthbar Initiated")
    self.COLOR = (0,255,0)
    self.screen = screen
    self.width = (self.screen.get_width()-20)
    self.healthFactor = 1

  def UpdateHealth(self):
    """
    Updates the health bar size according to health of the hero
    args: self is health bar
    returns: none
    """
    self.bar = pygame.draw.rect(self.screen, self.COLOR, pygame.Rect(10, 10, (self.width * self.healthFactor), 10))