import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# Actors are sprites — loaded from the images/ folder
player = Actor('happy')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('alien')
alien.pos = (100, 100)
alien.dx = 3
alien.dy = 2

cookie = Actor('cookie')
cookie.pos = (300, 300)

score = 0
game_over = False


def update():
    global score, game_over

    if game_over:
        return

    # Move player with arrow keys (held down = keeps moving)
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # Keep player inside the screen
    if player.x < 20:
        player.x = 20
    if player.x > WIDTH - 20:
        player.x = WIDTH - 20
    if player.y < 20:
        player.y = 20
    if player.y > HEIGHT - 20:
        player.y = HEIGHT - 20

    # Alien bounces around the screen
    alien.x += alien.dx
    alien.y += alien.dy
    if alien.x < 20 or alien.x > WIDTH - 20:
        alien.dx = -alien.dx
    if alien.y < 20 or alien.y > HEIGHT - 20:
        alien.dy = -alien.dy

    # Collect the cookie — it respawns in a new spot
    if player.colliderect(cookie):
        score += 1
        cookie.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    # Game over if alien catches player
    if player.colliderect(alien):
        game_over = True


def draw():
    screen.fill((30, 30, 30))

    player.draw()
    alien.draw()
    cookie.draw()

    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2),
                         fontsize=60, color="red")
        screen.draw.text(f"Final Score: {score}",
                         center=(WIDTH // 2, HEIGHT // 2 + 60),
                         fontsize=30, color="white")


pgzrun.go()
