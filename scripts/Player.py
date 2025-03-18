from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.AnimatedSprite2D import AnimatedSprite2D
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
		print("ready")
		animatedSprite = self.get_node(NodePath.new2("AnimatedSprite2D"))
		self.screen_size = self.get_viewport_rect().size
		self._input_singleton = Input.instance()
	
	def _process(self, delta: float):
		print("processing")
		_input = self._input_singleton
		print("hi")
		if _input.is_action_pressed("move_right"):
			animatedSprite.play("walk")
			self.animatedSprite.flip_h = True
			self.position.x += self.speed * delta
		elif _input.is_action_pressed("move_left"):
			self.animatedSprite.play("walk")
			self.animatedSprite.flip_h = False
			self.position.x -= self.speed * delta
		else:
			self.animatedSprite.play("stand_front")
