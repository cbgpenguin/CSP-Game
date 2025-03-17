
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.CharacterBody2D.CharacterBody2D import CharacterBody2D

@gdclass
class Player(CharacterBody2D):

	# define properties like this
	
	SPEED = 130.0
	JUMP_VELOCITY = -300.0
	
	# Get the gravity from the project settings to be synced with RigidBody nodes.
	gravity = ProjectSettings.get_setting("physics/2d/default_gravity")


	# define signals like this
	#test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		animatedSprite = $AnimatedSprite2D

	def _process(self, delta:float) -> None:
		direction = Input.get_axis("move_left", "move_right")
		#flip sprite
		if direction > 0:
			animatedSprite.flip_h = false
		elif direction < 0:
			animatedSprite.flip_h = true
		#Play animation
		if direction == 0:
			animatedSprite.play("Idle")
		else:
			animatedSprite.play("run")
		#apply momvement
		if direction:
			velocity.x = direction * SPEED
		else:
			velocity.x = move_toward(velocity.x, 0, SPEED)
		move_and_slide()

		
	
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
