# Hangman Game 🎯

A Python implementation of the classic Hangman game where players guess letters to reveal a hidden word.

## Problem Statement
Players must uncover a randomly chosen word by guessing one letter at a time. Incorrect guesses reduce the number of lives. The game ends when:
- The word is fully revealed (win), or
- All lives are lost (lose).

## Features
- Randomly selected words from a predefined word list.
- Tracks guessed letters to avoid duplicate guesses.
- Visual feedback for wrong guesses using ASCII art.
- Interactive and beginner-friendly.

## How to Play
1. Run the game using Python:
   ```bash
   python hangman_game.py

## Sample Gameplay
Welcome to Hangman!
Guess a letter: a
_ a _ _ a _
Guess a letter: b
You guessed 'b', that's not in the word and you lose a life.
