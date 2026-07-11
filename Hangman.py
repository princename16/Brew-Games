#!/usr/bin/env python3
"""Simple Hangman CLI game"""
import random
import sys

WORD_LIST = [
	"python", "programming", "hangman", "dinosaur", "challenge",
	"computer", "keyboard", "function", "variable", "algorithm"
]


def choose_word():
	return random.choice(WORD_LIST).lower()


def display_state(secret, guessed):
	return " ".join(c if c in guessed else "_" for c in secret)


def play():
	secret = choose_word()
	guessed = set()
	wrong = set()
	max_wrong = 6

	while True:
		print("\nWord: ", display_state(secret, guessed))
		print(f"Wrong guesses ({len(wrong)}/{max_wrong}):", " ".join(sorted(wrong)))

		if all(c in guessed for c in secret):
			print("Congratulations! You guessed the word:", secret)
			break

		if len(wrong) >= max_wrong:
			print("Out of guesses. The word was:", secret)
			break

		choice = input("Enter a letter (or full word): ").strip().lower()
		if not choice:
			continue

		if len(choice) == 1:
			if not choice.isalpha():
				print("Please enter a letter.")
				continue
			if choice in guessed or choice in wrong:
				print("You already tried that.")
				continue
			if choice in secret:
				guessed.add(choice)
				print("Good guess!")
			else:
				wrong.add(choice)
				print("Wrong!")
		else:
			# full word guess
			if choice == secret:
				print("Correct! The word is:", secret)
				break
			else:
				print("Wrong word guess.")
				wrong.add(choice)


def main():
	print("Welcome to Hangman!")
	while True:
		play()
		ans = input("Play again? (y/N): ").strip().lower()
		if ans != 'y':
			print("Goodbye!")
			break


if __name__ == '__main__':
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		sys.exit(0)

