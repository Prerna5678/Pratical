"""
Simple, polished Snake game using Pygame.

Features:
- Start menu with Play / Quit
- Pause and Resume (P)
- Score and persistent high score (highscore.txt)
- Keyboard controls: arrows + WASD
- Smooth, grid-based movement with adjustable speed

Run: python snake-game.py
"""

import os
import random
import sys

# Helpful import check for pygame so we can show actionable instructions
try:
	import pygame
except Exception as e:
	print("\nError: Pygame is not installed or failed to import.")
	print("Install it into your project's virtual environment and try again.")
	print("If you're using the project's .venv on Windows PowerShell, run:")
	print("  . \"C:\\Users\\91812\\Desktop\\Project\\Game in Python\\.venv\\Scripts\\Activate.ps1\"")
	print("  python -m pip install --upgrade pip setuptools wheel")
	print("  python -m pip install pygame")
	print("Then run: python snake-game.py")
	print(f"\nFull import error: {e}\n")
	sys.exit(1)

# ===== CONFIG =====
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 60

# Speed measured in moves per second (snake steps)
DEFAULT_SPEED = 8
HIGH_SCORE_FILE = "highscore.txt"
# ensure data file is written next to the script
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
HIGH_SCORE_PATH = os.path.join(PROJECT_DIR, HIGH_SCORE_FILE)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 200, 0)
BLUE = (50, 150, 255)


def load_high_score(path=HIGH_SCORE_PATH):
	try:
		with open(path, "r") as f:
			return int(f.read().strip() or 0)
	except Exception:
		return 0


def save_high_score(score, path=HIGH_SCORE_PATH):
	try:
		cur = load_high_score(path)
		if score > cur:
			with open(path, "w") as f:
				f.write(str(score))
	except Exception:
		pass


class SnakeGame:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Snake")
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font(None, 36)
		self.large_font = pygame.font.Font(None, 72)

		self.running = True
		self.state = "menu"  # menu, playing, paused, gameover

		self.speed = DEFAULT_SPEED
		self.step_time = 1.0 / self.speed

		self.high_score = load_high_score()

		# load optional sounds if available
		self.sounds = {}
		try:
			pygame.mixer.init()
			self.sounds['eat'] = None
		except Exception:
			self.sounds = {}

		self.reset_game()

	def reset_game(self):
		mid_x = GRID_WIDTH // 2
		mid_y = GRID_HEIGHT // 2
		self.snake = [(mid_x, mid_y), (mid_x - 1, mid_y), (mid_x - 2, mid_y)]
		self.direction = (1, 0)
		self.next_direction = self.direction
		self.place_food()
		self.score = 0
		self.elapsed = 0.0
		self.state = 'playing'

	def place_food(self):
		choices = [(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT) if (x, y) not in self.snake]
		self.food = random.choice(choices) if choices else None

	def handle_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if self.state == 'menu':
					if event.key in (pygame.K_RETURN, pygame.K_SPACE):
						self.reset_game()
					elif event.key == pygame.K_ESCAPE:
						self.running = False
				elif self.state == 'playing':
					if event.key in (pygame.K_UP, pygame.K_w):
						self.set_direction((0, -1))
					elif event.key in (pygame.K_DOWN, pygame.K_s):
						self.set_direction((0, 1))
					elif event.key in (pygame.K_LEFT, pygame.K_a):
						self.set_direction((-1, 0))
					elif event.key in (pygame.K_RIGHT, pygame.K_d):
						self.set_direction((1, 0))
					elif event.key == pygame.K_p:
						self.state = 'paused'
					elif event.key == pygame.K_ESCAPE:
						self.state = 'menu'
				elif self.state == 'paused':
					if event.key == pygame.K_p:
						self.state = 'playing'
					elif event.key == pygame.K_ESCAPE:
						self.state = 'menu'
				elif self.state == 'gameover':
					if event.key in (pygame.K_RETURN, pygame.K_SPACE):
						self.reset_game()
					elif event.key == pygame.K_ESCAPE:
						self.state = 'menu'

	def set_direction(self, dir_tuple):
		# prevent reversing
		if (dir_tuple[0] * -1, dir_tuple[1] * -1) == self.direction and len(self.snake) > 1:
			return
		self.next_direction = dir_tuple

	def update(self, dt):
		if self.state != 'playing':
			return
		self.elapsed += dt
		if self.elapsed >= self.step_time:
			self.elapsed -= self.step_time
			self.direction = self.next_direction
			head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
			# wrap-around behavior
			head = (head[0] % GRID_WIDTH, head[1] % GRID_HEIGHT)
			if head in self.snake:
				self.state = 'gameover'
				save_high_score(self.score)
				self.high_score = load_high_score()
				return
			self.snake.insert(0, head)
			if head == self.food:
				self.score += 1
				# slightly increase speed every 5 points
				if self.score % 5 == 0:
					self.speed = min(self.speed + 1, 20)
					self.step_time = 1.0 / self.speed
				self.place_food()
			else:
				self.snake.pop()

	def draw_grid(self):
		for x in range(0, WINDOW_WIDTH, CELL_SIZE):
			pygame.draw.line(self.screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
		for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
			pygame.draw.line(self.screen, GRAY, (0, y), (WINDOW_WIDTH, y))

	def draw(self):
		self.screen.fill(BLACK)
		# draw food
		if self.food:
			fx, fy = self.food
			pygame.draw.rect(self.screen, RED, (fx * CELL_SIZE + 1, fy * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2), border_radius=4)
		# draw snake
		for i, (sx, sy) in enumerate(self.snake):
			rect = pygame.Rect(sx * CELL_SIZE + 1, sy * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2)
			color = GREEN if i == 0 else BLUE
			pygame.draw.rect(self.screen, color, rect, border_radius=6)

		# HUD
		score_surf = self.font.render(f"Score: {self.score}", True, WHITE)
		hs_surf = self.font.render(f"High: {self.high_score}", True, YELLOW)
		self.screen.blit(score_surf, (8, 8))
		self.screen.blit(hs_surf, (WINDOW_WIDTH - hs_surf.get_width() - 8, 8))

		if self.state == 'paused':
			self.draw_center_message("Paused", sub="Press P to resume")
		elif self.state == 'menu':
			self.draw_menu()
		elif self.state == 'gameover':
			self.draw_center_message("Game Over", sub=f"Score: {self.score}  High: {self.high_score}\nPress Enter to play again")

		pygame.display.flip()

	def draw_center_message(self, title, sub=None):
		title_surf = self.large_font.render(title, True, WHITE)
		tx = (WINDOW_WIDTH - title_surf.get_width()) // 2
		ty = (WINDOW_HEIGHT - title_surf.get_height()) // 2 - 30
		self.screen.blit(title_surf, (tx, ty))
		if sub:
			lines = str(sub).split("\n")
			for i, line in enumerate(lines):
				sub_surf = self.font.render(line, True, WHITE)
				sx = (WINDOW_WIDTH - sub_surf.get_width()) // 2
				self.screen.blit(sub_surf, (sx, ty + title_surf.get_height() + 8 + i * 30))

	def draw_menu(self):
		self.screen.fill(BLACK)
		title = self.large_font.render("Snake", True, GREEN)
		tx = (WINDOW_WIDTH - title.get_width()) // 2
		ty = WINDOW_HEIGHT // 4
		self.screen.blit(title, (tx, ty))

		option_surf = self.font.render("Press Enter or Space to Play", True, WHITE)
		optx = (WINDOW_WIDTH - option_surf.get_width()) // 2
		self.screen.blit(option_surf, (optx, ty + 120))

		info_surf = self.font.render("Arrows or WASD to move — P to pause — Esc to menu", True, GRAY)
		ix = (WINDOW_WIDTH - info_surf.get_width()) // 2
		self.screen.blit(info_surf, (ix, ty + 170))

		hs_surf = self.font.render(f"High Score: {self.high_score}", True, YELLOW)
		self.screen.blit(hs_surf, ((WINDOW_WIDTH - hs_surf.get_width()) // 2, ty + 210))

	def run(self):
		while self.running:
			dt = self.clock.tick(FPS) / 1000.0
			self.handle_input()
			if self.state == 'menu':
				# menu loop: draw and wait for input
				self.draw()
				continue
			self.update(dt)
			self.draw()
		pygame.quit()


def main():
	game = SnakeGame()
	game.run()


if __name__ == '__main__':
	main()