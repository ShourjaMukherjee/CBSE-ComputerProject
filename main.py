# Project setup

import pygame
import pickle
import random
from settings import *
from PlayersAndStuff import *
from os import path
import time

class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
		self.clock=pygame.time.Clock()
		self.running=True
		pygame.display.set_caption(TITLE)
		self.font_name=pygame.font.match_font(FONT_NAME)
		self.load_data()
	
	def shrink_image(self,image,factor):
		rect=image.get_rect()
		width=rect.width
		height=rect.height
		return pygame.transform.scale(image, (int(width *factor), int(height*factor)))
		
	def load_data(self):
		#this loads the high score
		self.dir=path.dirname(__file__)
		with open(path.join(self.dir,HS_FILE),'r') as f:
			try:
				self.highscore=int(f.read())
			except:
				self.highscore=0
		self.image_dir=path.join(self.dir,'img')
		# load sounds
		self.snd_dir = path.join(self.dir, 'snd')
		self.jump_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'Jump33.wav'))
		self.cloud_images=[pygame.image.load(path.join(self.image_dir, 'cloud1.png')),
						pygame.image.load(path.join(self.image_dir, 'cloud2.png')),
						pygame.image.load(path.join(self.image_dir, 'cloud3.png'))]
		
		#CHANGE NO.1
		with open(path.join(self.dir,'LoggedInAccount.dat'),'rb') as file:
			try:	
				x=pickle.load(file)
				self.current_user=x.FirstName
				self.current_user_HS=x.Highscore
			except:
				self.current_user='X'
		# try:
			# file=open(path.join(self.dir,'LoggedInAccount.dat'),'rb')
			# x=pickle.load(file)
			# self.current_user=x.FirstName
			# self.current_user_HS=x.Highscore
		# except:
			# self.current_user='X'
		# file.close()
		
	
	def new(self):
		# start a new game
		self.score=0
		self.all_sprites = pygame.sprite.LayeredUpdates()
		self.platforms=pygame.sprite.Group()
		self.powerups=pygame.sprite.Group()
		self.mobs=pygame.sprite.Group()
		self.clouds=pygame.sprite.Group()
		self.player = Player(self)
		#making all the platforms
		for platform in platform_list:
			Platform(self,platform[0],platform[1])
		self.mob_timer=0
		pygame.mixer.music.load(path.join(self.snd_dir, 'Happy Tune.ogg'))
		for i in range(8): #spawn clouds at start
			c = Cloud(self)
			c.rect.y += 500
		self.run()
	
	def run(self):
		# Game Loop
		pygame.mixer.music.play(loops=-1)
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
		pygame.mixer.music.fadeout(500)
	
	def update(self):
		#Game Loop-Update
		self.all_sprites.update()
		
		#SPAWNING MOBS
		now=pygame.time.get_ticks()
		if now-self.mob_timer>mob_freq-random.choice([1000,500,0,-500,1000]):		#varying spawn time
			self.mob_timer=now
			Mob(self)
		#collision with enemies
		mob_hits = pygame.sprite.spritecollide(self.player, self.mobs, False, pygame.sprite.collide_mask)
		if mob_hits:
			if  self.player.rect.right<WIDTH-5 and  self.player.rect.left>5 :
				self.playing = False
		
		#this collison is only valid if falling
		if self.player.vel.y>0:
			hits=pygame.sprite.spritecollide(self.player,self.platforms,False)
			if hits:
				lowest=hits[0]
				for hit in hits:
					if hit.rect.bottom>lowest.rect.bottom:
						lowest = hit
				if self.player.pos.x<lowest.rect.right+10 and self.player.pos.x>lowest.rect.left-10:		
					if self.player.pos.y<lowest.rect.centery+2: #so that player doesnt snap up even when it is lower than platform
						self.player.pos.y=lowest.rect.top 
						self.player.vel.y=0
						self.player.jumping=False
			
		#if player dies
		if self.player.rect.bottom>HEIGHT:
			for sprite in self.all_sprites:
				sprite.rect.y -=self.player.vel.y #this gives effect that sprites are moving up when we die
				if sprite.rect.bottom < 0:
					sprite.kill()
		if len(self.platforms)==0:
			self.playing=False
		
		#powerups collision
		pow_hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
		for pow in pow_hits:
			if pow.type == 'boost':
				self.player.vel.y = -boost_power
				self.player.jumping = False
		
		
		
		#scrolling upwards
		if self.player.rect.top <= HEIGHT/4:
			if random.randrange(100) < 15:
				Cloud(self)
			self.player.pos.y+=max(abs(self.player.vel.y),3) #scrolling upwards if player goes up but screen fails to scroll
			for cloud in self.clouds:
				cloud.rect.y += max(abs(self.player.vel.y / 2), 2)
			for mob in self.mobs:
				mob.rect.y+=max(abs(self.player.vel.y),3)
			for plat in self.platforms:
				plat.rect.y+=max(abs(self.player.vel.y),3)
				if plat.rect.top>=HEIGHT+20:
					plat.kill()
					self.score+=10
		
		#making of new platforms
		while len(self.platforms) < 6: #keeping about 6 platforms at any instant
			width = random.randrange(50, 100)
			p = Platform(self,random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30))
			
	
	def events(self):
		# GameLoop-events
		for event in pygame.event.get():
			#closing
			if event.type==pygame.QUIT:
				self.playing=False
				self.running=False
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_SPACE:
					
					self.player.jump()
					
			if event.type==pygame.KEYUP:  #if we release key fast then full jump does not happen
				if event.key==pygame.K_SPACE:
					self.player.low_jump()
	
				
	def draw(self):
		#gameloop draw
		self.screen.fill(BLUISH)
		self.all_sprites.draw(self.screen)
		self.draw_text(str(self.score),30,WHITE,WIDTH/2,10)
		
		#updating the screen
		pygame.display.flip()
		
	def wait(self):
		waiting=True
		while waiting:
			self.clock.tick(FPS)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					self.running=False
					waiting=False
				if event.type==pygame.KEYUP:
					if event.key==pygame.K_x:
						waiting=False
					if event.key==pygame.K_q:
						waiting=False
						self.running=False
	
	def show_start_screen(self):
		pygame.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
		pygame.mixer.music.play(loops=-1)
		self.screen.fill(BLUISH)
		self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 5)
		#change No.2
		self.draw_text("Welcome "+self.current_user+"!", 20, WHITE, WIDTH / 3+ 100, HEIGHT / 3)
		self.draw_text("Arrows to move, Space to jump", 20, WHITE, WIDTH / 2, HEIGHT / 2)
		self.draw_text("Press 'X' to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
		pygame.display.flip()
		
		self.wait()
		pygame.mixer.music.fadeout(500)
	
	def show_end_screen(self):
		pygame.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
		pygame.mixer.music.play(loops=-1)
		if  self.running:     #to aviod going to this screen if user tries to close window during playing game
			self.screen.fill(BLUISH)
			self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 6)
			self.draw_text("YOUR SCORE IS " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 3)
			self.draw_text("Press 'X' to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
			self.draw_text("Press 'Q' to Quit", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4 +40)
			#OVERALL HIGHSCORE HANDLING
			if self.score>self.highscore:
				self.highscore=self.score
				self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
				with open(path.join(self.dir, HS_FILE), 'w') as f:
					f.write(str(self.score))
			else:
				self.draw_text("Overall High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
			#PERSONAL HIGHSCORE HANDLING
			if self.score>self.current_user_HS:
				self.draw_text("NEW PERSONAL BEST!", 22, WHITE, WIDTH / 2, HEIGHT / 2  )
				
			else:
				self.draw_text("Your High Score: " + str(self.current_user_HS), 22, WHITE, WIDTH / 2, HEIGHT / 2 )
			
			pygame.display.flip()
			
			self.wait()
			pygame.mixer.music.fadeout(500)
				
	
	def draw_text(self, text, size, color, x, y):
		font = pygame.font.Font(self.font_name, size)     #giving font to the text
		text_surface = font.render(text, True, color) 
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)                     #position of the mid of the top of the text
		self.screen.blit(text_surface, text_rect)
		

class Account():                                                                                #every user will have an object of this class
	def __init__(self, FirstName, LastName, DOB, Password, Username ):
		self.FirstName = FirstName
		self.LastName = LastName
		self.DOB = DOB
		self.Password= Password
		self.Username =  Username
		self.Highscore = 0	
		
def LoggedInAccountHS_update(g):
	with open(path.join(g.dir,'LoggedInAccount.dat'),'rb+') as file:
		try:
			S=g.score
				
			while True:
				try:
					pos=file.tell()
					x=pickle.load(file)
					if str(x.FirstName)==str(g.current_user) and S>x.Highscore:
					
						x.Highscore=S
						file.seek(pos,0)
						pickle.dump(x,file)
						
						break
				except EOFError:
					break

		except IOError:
			pass

def AccountsHS_update(g):
	with open(path.join(g.dir,'Accounts.dat'),'rb+') as file:
		try:
			S=g.score
				
			while True:
				try:
					pos=file.tell()
					x=pickle.load(file)
					if str(x.FirstName)==str(g.current_user) and S>x.Highscore:
					
						x.Highscore=S
						file.seek(pos,0)
						pickle.dump(x,file)
						
						break
				except EOFError:
					break

		except IOError:
			pass
	
g=Game()
g.show_start_screen()

while g.running:
	g.new()
	LoggedInAccountHS_update(g)
	AccountsHS_update(g)
	g.show_end_screen()
	g.load_data()
	

  

	
	

pygame.quit()
