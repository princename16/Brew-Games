#!/usr/bin/env python3

"""Simple Hangman CLI game"""
import random
import sys

WORD_LIST = [
	"python", "programming", "hangman", "dinosaur", "challenge",
	"computer", "keyboard", "function", "variable", "algorithm", "Crazy", "Pythonista", "Terminal", "Code", "Debugging", "Exception", "Recursion", "Iteration", "Syntax", "Compilation", "Interpreter", "Object", "Class", "Inheritance", "Polymorphism", "Encapsulation", "Abstraction", "Module", "Package", "Library", "Framework", "Script", "Command", "Argument", "Parameter", "Return", "Loop", "Condition", "Boolean", "String", "Integer", "Float", "List", "Tuple", "Dictionary", "Set", "Array", "Stack", "Queue", "Tree", "Graph", "Node", "Edge", "Vertex", "Pathfinding", "Sorting", "Searching", "Hashing", "Encryption", "Decryption", "Compression", "Decompression", "Networking", "Protocol", "Socket", "Threading", "Concurrency", "Parallelism", "Asynchronous", "Synchronous", "Event", "Callback", "Promise", "Future", "Lambda", "Decorator", "Generator", "Iterator", "Comprehension", "Expression", "Statement", "Block", "Scope", "Namespace", "Import", "Export", "Dependency", "Versioning", "Repository", "Branch", "Merge", "Commit", "Push", "Pull", "Clone", "Fork", "Stash", "Rebase", "Cherry-pick", "Tag", "Release", "Build", "Deploy", "Continuous", "Integration", "Delivery", "Pipeline", "Testing", "Unit", "Integration", "System", "Acceptance", "Regression", "Performance", "Load", "Stress", "Security", "Vulnerability", "Exploit", "Patch", "Update", "Upgrade", "Downgrade", "Rollback", "Backup", "Restore", "Monitoring", "Logging", "Alerting", "Notification", "Dashboard", "Analytics", "Visualization", "Reporting", "Audit", "Compliance", "Governance", "Policy", "Procedure", "Standard", "Best-practice", "Guideline", "Checklist", "Template", "Blueprint", "Architecture", "Design", "Pattern", "Anti-pattern", "Refactoring", "Optimization", "Profiling", "Benchmarking", "Documentation", "Commenting", "Annotation", "Metadata", "Configuration", "Parameterization", "Customization", "Localization", "Internationalization", "Accessibility", "Usability", "User-experience", "Interface", "Interaction", "Navigation", "Layout", "Typography", "Color-scheme", "Theme", "Skin", "Iconography", "Imagery", "Animation", "Transition", "Effect", "Feedback", "Error-handling", "Exception-handling", "Logging", "Debugging", "Tracing", "Profiling", "Monitoring", "Alerting", "Notification", "Health-check", "Heartbeat", "Status", "Metric", "Gauge", "Counter", "Histogram", "Timer", "Event", "Log", "Trace", "Span", "Context", "Correlation", "Propagation", "Sampling", "Aggregation", "Visualization", "Dashboard", "Report", "Alert", "Notification", "Incident", "Response", "Recovery", "Post-mortem", "Root-cause-analysis", "Lessons", "Hangman", "Game", "challenge", "guess", "letter", "word", "hangman", "dinosaur", "python", "programming", "terminal", "cli", "interface", "input", "output", "display", "state", "secret", "guessed", "wrong", "max_wrong", "congratulations", "out_of_guesses", "play_again", "goodbye", "keyboardinterrupt", "error", "exit", "holy"
]


def choose_word():
	return random.choice(WORD_LIST).lower()


def display_state(secret, guessed):
	return " ".join(c if c in guessed else "_" for c in secret)


def play():
	secret = choose_word()
	guessed = set()
	wrong = set()
	max_wrong = 10

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

