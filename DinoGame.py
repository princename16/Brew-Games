#!/usr/bin/env python3
"""A simple terminal-based dinosaur runner game."""

import curses
import random
import sys

WIDTH = 80
HEIGHT = 24
GROUND_Y = 20
DINO_X = 6
GRAVITY = 0.55
JUMP_VELOCITY = -7.0


def draw_ground(stdscr):
    for x in range(WIDTH):
        stdscr.addstr(GROUND_Y, x, "-")


def draw_dino(stdscr, dino_y):
    body = [
        "  /\\",
        " /  \\_",
        " /_||_|",
        "  ||  ",
    ]
    for index, line in enumerate(body):
        y = int(dino_y) - len(body) + index + 1
        if 0 <= y < HEIGHT:
            stdscr.addstr(y, DINO_X, line)


def draw_obstacles(stdscr, obstacles):
    for obstacle in obstacles:
        x = obstacle["x"]
        kind = obstacle["kind"]
        if kind == "cactus":
            lines = ["  _|", " _|", "_| "]
            for offset, line in enumerate(lines):
                y = GROUND_Y - offset - 1
                if 0 <= y < HEIGHT:
                    stdscr.addstr(y, x, line)
        else:
            stdscr.addstr(GROUND_Y - 1, x, "o")


def run_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    stdscr.keypad(True)

    dino_y = GROUND_Y
    velocity = 0.0
    jumping = False
    obstacles = []
    spawn_timer = 0
    score = 0

    while True:
        key = stdscr.getch()
        if key in (ord("q"), 27):
            return False
        if key in (ord(" "), ord("w"), curses.KEY_UP):
            if not jumping:
                jumping = True
                velocity = JUMP_VELOCITY

        if jumping:
            velocity += GRAVITY
            dino_y += velocity
            if dino_y >= GROUND_Y:
                dino_y = GROUND_Y
                velocity = 0.0
                jumping = False

        spawn_timer += 1
        if spawn_timer > 22:
            obstacles.append({"x": WIDTH - 3, "kind": random.choice(["cactus", "rock"])})
            spawn_timer = 0

        for obstacle in obstacles:
            obstacle["x"] -= 1
        obstacles = [obs for obs in obstacles if obs["x"] + 2 >= 0]

        score += 1
        collision = False
        for obstacle in obstacles:
            if obstacle["x"] <= DINO_X + 2 and obstacle["x"] + 2 >= DINO_X and int(dino_y) >= GROUND_Y - 2:
                collision = True
                break
        if collision:
            break

        stdscr.erase()
        draw_ground(stdscr)
        draw_dino(stdscr, dino_y)
        draw_obstacles(stdscr, obstacles)
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
    print("Welcome to Dino Dash!")
    print("Run this game in a terminal window for the best experience.")
    print("Press Enter to start...")
    input()

    while True:
        try:
            replay = curses.wrapper(run_game)
        except KeyboardInterrupt:
            break
        if not replay:
            break

    print("Thanks for playing Dino Dash!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
