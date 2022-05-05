import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2
        self.thinkInterval = 1000
        self.direction = "Up"
        self.counter = 0
        self.clock = pygame.time.Clock()
        self.widthBound = screen.get_width()
        self.heightBound = screen.get_height()

    def think(self):
      """"
      This function sets the enemies current direction (randomly) to one of the four directions on the screen
      args: self is enemy
      returns: none
      """
      num = random.randrange(0,4)
      if num == 0:
        self.direction = "Up"
      if num == 1:
        self.direction = "Right"
      if num == 2:
        self.direction = "Down"
      if num == 3:
        self.direction = "Left"

    def move(self):
      """
      This function moves the enemy according to the randomly selected direction from above function
      args: self is enemy
      returns: none
      """
      if self.direction == "Up":
        if self.rect.y > 0:
          self.rect.y -= self.speed
      if self.direction == "Right":
        if self.rect.x < self.widthBound:
          self.rect.x += self.speed
      if self.direction == "Down":
        if self.rect.y < self.heightBound:
          self.rect.y += self.speed
      if self.direction == "Left":
        if self.rect.x > 0:
          self.rect -= self.speed

    def update(self):
        """
      This function calls think function over an interval of time
      args: self is enemy
      returns: none
      """
       self.counter = self.counter + self.clock.tick()
      if self.counter > self.thinkInterval:
        self.counter = 0
        self.think()

      self.move()
        #print("'Update me,' says " + self.name)
