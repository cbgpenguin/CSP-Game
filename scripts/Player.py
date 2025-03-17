from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.Input import Input
from py4godot.classes.core import Vector3
from py4godot.classes.core import Vector2, NodePath
from py4godot.classes.CharacterBody2D.CharacterBody2D import CharacterBody2D

@gdclass
class Player(CharacterBody2D):

	speed = 100.0
	velocity = 0
	screen_size = None

	def _ready(self):
		print("hello")
		self.animatedSprite = self.get_node("AnimatedSprite2D")
		self.screen_size = self.get_viewport_rect().size
		_input = Input.instance()

	def _process(self, delta: float):
		print("hello")
		if self._input.is_action_pressed("move_right"):
			self.velocity.x += 1
		if self._input.is_action_pressed("move_left"):
			self.velocity.x -= 1
		if self.velocity.length() > 0:
			self.velocity = self.velocity.normalized() * self.speed
			self.animatedSprite.play("walk")
			if self.velocity.x < 0:
				self.animatedSprite.flip_h = True
			else:
				self.animatedSprite.flip_h = False
		else:
			self.animatedSprite.play("stand_front")
	
		self.velocity = self.move_and_slide(self.velocity)
