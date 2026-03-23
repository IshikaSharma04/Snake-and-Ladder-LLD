Snake and Ladder Game (Java, LLD)

This is a simple console-based Snake and Ladder game built in Java, designed with a strong focus on clean low-level design.

The goal of this project is not just to make the game work, but to structure it in a way that’s modular, extensible, and easy to reason about—like you’d expect in a real system design interview.

What this project does
Supports multiple players taking turns
Lets you choose how the board is created:
Classic board (fixed snakes & ladders)
Random board with difficulty levels
Fully custom board
Handles snakes and ladders dynamically during gameplay
Notifies game events using an observer pattern
Keeps the logic clean and separated using interfaces
How it’s designed

Instead of putting everything in one class, the code is broken down into smaller components, each with a clear responsibility.

Core idea
Game → controls the flow
Board → stores snakes and ladders
Player → tracks position
Dice → generates moves

Everything else builds around this.

Design patterns used (and why)
Strategy Pattern

Used in two places:

Board setup (different ways to create snakes/ladders)
Game rules (can easily change movement logic)

This makes it easy to plug in new behaviors without touching existing code.

Factory Pattern

Handles game creation:

Standard game
Random game
Custom game

Keeps object creation clean and centralized.

Observer Pattern

Used for notifications like:

Player moves
Snake/ladder hits
Game start/end

Right now it prints to console, but you could easily plug in logging, UI updates, etc.

How to run it

Compile:

javac SnakeAndLadder.java

Run:

java SnakeAndLadder
How the game flows
You choose the type of game (standard / random / custom)
Board gets initialized
Players are added
Game starts:
Player rolls dice
Moves forward
Hits snake or ladder (if any)
Checks for win
Next player’s turn

The game continues until someone reaches the last cell exactly.

Example
Player1 rolled: 4  
Ladder! Moving from 2 to 38  

Player2 rolled: 6  
Snake! Moving from 99 to 54  

Player1 wins!
