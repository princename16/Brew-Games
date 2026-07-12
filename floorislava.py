#!/usr/bin/env python3
"""Floor is Lava - Jump on platforms to avoid the lava below."""

import curses
import random
import sys

WIDTH = 80
HEIGHT = 24
GROUND_Y = 20
DINO_X = 6
GRAVITY = 0.6

JUMP_VELOCITY = -7.0


def draw_lava(stdscr):
    for x in range(WIDTH):
        if x < WIDTH - 1:
            try:
                stdscr.addstr(GROUND_Y, x, "~")
            except curses.error:
                pass
def draw_player(stdscr, player_y):
    """Draw the player character."""
    body = [
        " _____",
        "| ˚¬˚|",
        "|    |",
        "______",
        "||  ||",
    ]
    for index, line in enumerate(body):
        y = int(player_y) - len(body) + index + 1
        if 0 <= y < HEIGHT:
            try:
                stdscr.addstr(y, DINO_X, line)
            except curses.error:
                pass


def draw_platforms(stdscr, platforms):
    """Draw platforms."""
    for platform in platforms:
        x = platform["x"]
        y = platform["y"]
        width = platform["width"]
        if 0 <= y < HEIGHT:
            for i in range(width):
                if 0 <= x + i < WIDTH - 1:
                    try:
                        stdscr.addstr(y, x + i, "=")
                    except curses.error:
                        pass


def run_game(stdscr):
    """Main game loop with gravity."""
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    stdscr.keypad(True)

    player_x = 6
    player_y = GROUND_Y
    velocity = 0.0
    jumping = False
    score = 0
    platforms = [
        {"x": 10, "y": 15, "width": 8},
        {"x": 30, "y": 12, "width": 8},
        {"x": 50, "y": 15, "width": 8},
        {"x": 70, "y": 10, "width": 8},
    ]
    spawn_timer = 0

    while True:
        key = stdscr.getch()
        if key in (ord("q"), 27):
            return False
        if key in (ord(" "), ord("w"), curses.KEY_UP):
            if not jumping:
                jumping = True
                velocity = JUMP_VELOCITY
        if key in (curses.KEY_LEFT, ord("a"), ord("A")):
            player_x = max(0, player_x - 2)
        if key in (curses.KEY_RIGHT, ord("d"), ord("D")):
            player_x = min(WIDTH - 6, player_x + 2)

        # Apply gravity
        if jumping or player_y < GROUND_Y:
            velocity += GRAVITY
            player_y += velocity

            # Check collision with platforms
            on_platform = False
            player_bottom = int(player_y)
            player_top = int(player_y) - 5
            for platform in platforms:
                if (player_x < platform["x"] + platform["width"] and 
                    player_x + 6 > platform["x"] and
                    player_bottom >= platform["y"] and 
                    player_top <= platform["y"] and
                    velocity >= 0):
                    player_y = float(platform["y"])
                    velocity = 0.0
                    jumping = False
                    on_platform = True
                    break

            # Fall into lava
            if player_y >= GROUND_Y + 1:
                break

        # Spawn new platforms
        spawn_timer += 1
        if spawn_timer > 25:
            new_y = random.randint(5, 18)
            new_x = WIDTH - random.randint(5, 15)
            platforms.append({"x": new_x, "y": new_y, "width": 8})
            spawn_timer = 0

        # Move platforms left
        for platform in platforms:
            platform["x"] -= 1
        platforms = [p for p in platforms if p["x"] + p["width"] > 0]

        score += 1

        stdscr.erase()
        draw_lava(stdscr)
        draw_platforms(stdscr, platforms)
        draw_player(stdscr, player_y)
        stdscr.addstr(1, 2, f"Score: {score}")
        stdscr.addstr(2, 2, "Jump: space / w / up  Quit: q")
        stdscr.refresh()

    stdscr.erase()
    stdscr.addstr(HEIGHT // 2 - 1, WIDTH // 2 - 10, f"Game Over! Score: {score}")
    stdscr.addstr(HEIGHT // 2 + 1, WIDTH // 2 - 14, "Press r to retry or q to quit")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key in (ord("r"), ord("R")):
            return True
        if key in (ord("q"), 27):
            return False


def main():
    """Main entry point."""
    print("Welcome to Floor is Lava!")
    print("Jump on platforms to avoid the lava!")
    print("Press Enter to start...")
    input()

    while True:
        try:
            replay = curses.wrapper(run_game)
        except KeyboardInterrupt:
            break
        if not replay:
            break

    print("Thanks for playing Floor is Lava!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)