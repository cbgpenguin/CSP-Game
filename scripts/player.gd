extends CharacterBody2D

const SPEED = 250.0 * 60 # Pixles/s
@onready var animatedSprite2d: AnimatedSprite2D = $AnimatedSprite2D
var colidedLastFrame = true

func _physics_process(delta: float) -> void:
	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var direction := Input.get_axis("move_left", "move_right")
	# Direction is -1, 1, or 0
	if direction: # If direction is not = to zero (I think)
		velocity.x = direction * SPEED * delta
	else:
		velocity.x = move_toward(velocity.x, 0, (1000 * delta)) #Slows it down by taking x velocity and incrementing it towards 0 
	# Animation
	if !colidedLastFrame:
		if direction == 0:
			setDefaltAnimation()
		elif direction == 1:
			animatedSprite2d.flip_h = false
			animatedSprite2d.play("walking (self explanatory but I felt like giving a description)")
		elif direction == -1:
			animatedSprite2d.flip_h = true
			animatedSprite2d.play("walking (self explanatory but I felt like giving a description)")
	else:
		setDefaltAnimation()
	
	colidedLastFrame = move_and_slide()

func setDefaltAnimation():
	animatedSprite2d.flip_h = false
	animatedSprite2d.play("default (front face short idel)")
