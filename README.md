# Who am I?

**I am an A level student studying Computer Science, Physics, Mathematics and Chemistry. I have found a passion for programming, and enjoy creating games as a way to learn programming languages and any respective libraries. I started learning [Python](#python-projects) (my very first programming language in 2018) and [C++](#c-projects) late 2019.**

## Python Projects

With python, I have mostly used the [pygame](#pygame) libraries, but have also experimented with some other libraries such as the [Panda3d Game Engine](#panda-3d).

#### Pygame

- **Garden Defence**

![An in-game screen shot](/ProgramRepos/Pygame-GardenDefence/GardenDefenceFiles/Images/ScreenShotForGithubPages-shrunk.png)

Garden Defence is my own tower defence strategy game. Players place different gnomes into the garden to fight the attacking insects. Money is earned from killing enemies, and can be used to buy more gnomes or upgrade existing gnomes. Upgrades can be bought by clicking the existing gnome, clicking the upgrade arrow, and then choosing between increasing range or power.

The majority of the game is played using only a mouse (or touchscreen), with the only exception being the ability to cancel a gnome placement using the escape button on the keyboard.

[Github Repository](https://github.com/owenpauptit/pygame-gardendefence)

[Download for Windows](/ProgramRepos/Pygame-GardenDefence/GardenDefence.zip?raw=true "Zip file download for Garden Defence")

---

- **Maze Generator**

This program generates a maze that the user can then use the arrow keys to navigate the player (red) and reach the finish square (green).

The generation part of the program uses a recursive backtracking algorithm to create the maze, which can be viewed when "Show Maze Generation" is selected in the set up menu. 

![The Recursive Backtracking Algorithm](/ProgramRepos/Pygame-MazeGenerator/MazeGeneratorFiles/PlayingScreenShot-shrunk.png)

Once the maze has been created, the user can then try to reach the finishing square (indicated by a green square) using the arrow keys on the keyboard. If the user completes the maze, they can choose to play either an easier maze, a harder maze or a maze of the same difficulty. Or, the user can press 'S' to go to the set up menu, where they can manually set the size of the grid.

![The playing screen, red square = player, green square = finish](/ProgramRepos/Pygame-MazeGenerator/MazeGeneratorFiles/GenerationScreenShot-shrunk.png)

[Github Repository](https://github.com/owenpauptit/pygame-mazegenerator)

[Download for Windows](/ProgramRepos/Pygame-MazeGenerator/MazeGenerator.zip?raw=true "zip file download for the Maze Generator")

---

- **Snake**

Snake is a simple game in which the player uses the arrow keys to control the snakes movement. The player aims to eat the fruit (indicated by the red square) which causes the snake to grow. The player dies if the snake's head touches it's body or the walls of the game area. There are basic settings window's which allow the user to change the size of the grid, the speed of the snake and the number of fruit.

[Github Repository](https://github.com/owenpauptit/Pygame-snake)

---

- **Mitosis**

Mitosis is the process of cell division. This program initially creates a single cell which moves around randomly, at random velocities calculated from the velocity in the previous frame. When a cell is left-clicked by the mouse, it divides creating two new cells both of which have half the radius of the parent, and inherit some of the parents qualities, such as it's speed before division, and colour. However these qualities mutate slightly creating two slightly different cells.

![Screenshot of mitosis simulation/game](/ProgramRepos/Pygame-Mitosis/MitosisFiles/screenshot.png)

A cell will grow if it is right-clicked by the mouse, and no other qualities will change. This means that the simulation can continue to evolve without the cells becoming too small to see. A cell can be killed by using the middle mouse button, allowing a user to remove any unwanted cells. The simulation will reset if the 'R' button is pressed on the keyboard.

[Github Repository](https://github.com/owenpauptit/pygame-mitosis)

---

- **2048**

2048 is a sliding block puzzle game first created by Italian web developer Gabriele Cirulli. The player starts with a single block on the board, and can use the arrow keys to move the block up, down, left or right. As each move takes place, a new bvlock is spawned on the board. The blocks start off with a value of 2, but if two blocks with the same number collide, their values sum and they become one block.

This process continues until every space on the board is taken up by a block. It is the player's goal to have a block with the value 2048, but they can continue playing to try and achieve the highest score they can.

[Github Repository](https://github.com/owenpauptit/pygame-2048)

---

- **Painter**

This is a simple program that lets the user 'paint' onto a canvas using the mouse. Different colours can be selected from the HUD at the top of the screen, and the size can be altered using the slider. To erase, simply select the white paint.

---

- **Calculator**

This program is a very basic calculator which can perform simple arithemtic operations. It can either be controlled with the keyboard, or by clicking the buttons on the GUI.

---

- **Rain**

This is a simple program that simulates a rain effect. The speed of the rain is dependent on the X position of the mouse inside the window. The sound effects can be muted and unmuted by pressing the space bar.

If 'P' is pressed on the keyboard, the rain becomes purple and Prince starts playing.

---

- Dropper Dodge

---

#### Panda 3D

- Procedural Terrain Generation

## C++ Projects

I recently started learning C++, and soon after, I started experimenting with the [SFML](#sfml) libraries.

#### SFML

- Flappy Bird

- **Conway's Game of Life**

This program is a simulation of Conway's Game of Life using SFML.

Conway's game of life is a zero player game, which takes a single input, then computes the following generations. It consists of a grid of cells which can either be alive or dead. When the next generation is calculated, the cells live or die depending on 3 rules:

> - If a living cell is surrounded by less than two other cells, it dies of underpopulation
> - If a living cell is surrounded by more than three other cells, it dies of overpopulation
> - if a dead cell is surrounded by exactly three other cells, it is born

The surrounding cells of a cell are the 8 cells neighbouring that cell, either horizontally, vertically or diagonally.

White squares represent alive cells, and black squares represent dead cells.

You can progress through each generation by clicking the mouse inside the game window.

---

- Pong

- Noughts and Crosses

***  
  
  
>
>
> | **[Linked in](https://linkedin.com/in/owen-pauptit/)** | **[GitHub](https://github.com/owenpauptit/)** |
>
