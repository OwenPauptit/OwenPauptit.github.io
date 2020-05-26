# Who am I?

**I am an A level student studying Computer Science, Physics, Mathematics and Chemistry. I have found a passion for programming, and enjoy creating games as a way to learn programming languages and any respective libraries.**

**I started learning [Python](/PythonPage.md) (my very first programming language in 2018) and [C++](/CppPage.md) late 2019. As of March 2020, I have begun learning [C#](/CsPage.md) - the language that I have decided to use for my A level Computer Science coursework.**

---

## [C# Projects](home.md)

I decided in March 2020, that for my A level coursework a language like C# or Java would be more suitable. I chose C# due to my familiarity with visual studio from my experience with C++. I started off by creating some simple [text-based programs that run in the console](#text-based-programs). In May 2020, I picked up [Xamarin](#xamarin) for android and made a few apps.

#### Text-based Programs


#####  • Dijkstra's Shortest Path Algorithm

Dijkstra's Shortest Path Algorithm is a method of finding for finding the shortest paths between nodes in a graph. In this implementation, however, I use a matrix. The program will find the shortest path from a start point to an end point while avoiding obstcales (walls).

It can either:
 - Randomly generate a start point, end point and walls
 - Load a text file that describes a particular set up
 - Take a series of inputs from the user indicating the coordinates of different points in the matrix
 
It has been created so that diagonals are included, but have 1.5 time the weight of travelling in a straight line.

![Image](/Resources/Images/Dijkstra.PNG)

For it to work in the C# console, the matrix is a multidimensional array of colours. This is printed every refresh, where '██' represents each cell/node. The green node is the start, the red node is the end, and the white nodes are walls.

Text files can be created to make custom grids, the start is represented by a capital 'S', the end is represented by a capital 'F' and walls are represented by capital 'X's.
 
[Github Repository](https://github.com/owenpauptit/Dijkstra)

[Download for Windows](https://github.com/OwenPauptit/OwenPauptit.github.io/blob/master/ProgramRepos/Console-Dijkstra/Dijkstra.zip?raw=true) 

---

#####  • Dungeon Explorer

Dungeon explorer is a game where the player navigates (using WASD) through a series of randomly generated rooms with varying sizes, proportions and doors. Sometimes, these rooms will have randomly generated monsters which will attack the player - either by shooting or chasing the player.

The player can attack the monsters back by shooting at them (using the arrow keys).

A player's score is the number of monsters they have killed, if a monster manages to successfully hit the player (either by shooting or chasing) then the player dies and it is game over.

The different monster types are as follows:

| **Monster** | **Description**                                                        | **Chance of spawning*** |
| ----------- | ---------------------------------------------------------------------- | ----------------------- |
| ѫ           | Fast, but not very much health and cannot shoot.                       |  50 %                   |
| Ѫ           | Slow, but double health and cannot shoot at the player.                |  35 %                   |
| Ж           | Won't move, but will shoot rapidly in the player's direction.          |  10 %                   |
| Ӝ           | Won't move, will shoot at a slower rate, but in all directions.        |  5  %                   |

\*  The chance of spawning is the chance that, given a monster is being spawned, that particular monster will be spawned
 

[Github Repository](https://github.com/owenpauptit/DungeonExplorer)

[Download for Windows](/ProgramRepos/Console-DungeonExplorer/DungeonExplorer.exe?raw=true)

---

#####  • Mastermind

Mastermind is a game that involves the use of several colours (Orange, blue, red, green, pink, white and yellow). Four of these colours are chosen by the computer and placed in a random order.

The player has ten guesses to find the order of the colours. Each time the player makes a guess, they are told how many are the correct colour and correct position, and how manya re the correct colour but incorrect position. For example...

If the code is

> **YPRB** *(Yellow Pink Red Blue)*

And the user guesses

> **YOBR** *(Yellow Orange Blue Red)*

the computer will output:

```
    Correct colour, correct position:     1
    Correct colour, incorrect position:   2
```

As you can see, the **Y** is in the correct position, and while the **B** and **R** are both present in the code, they are not in the correct position.

The player wins when they guess the correct combination.

[Github Repository](https://github.com/owenpauptit/MasterMind)

[Download for Windows](/ProgramRepos/Console-Mastermind/Mastermind.zip?raw=true)

---

#### Xamarin


##### • Notes App

"Notes!" is a note taking app that lets you create new notes, save those notes, and edit existing notes created with the app. Each note has a title and body.

!["Notes!" screenshots](/Resources/Images/NotesApp.png)

The app works by saving text files with the title of each note being the name of the text file (i.e. "title.txt") and the content of the note saved inside the document.

[Github Repository](https://github.com/owenpauptit/xamarin-notesapp)

[APK download](/ProgramRepos/Xamarin-Notes/com.AeselStudios.Notes-Signed.apk) (Must have 3rd party downloads enabled)

---

## [Python Projects](/PythonPage.md)

## [C++ Projects](/CppPage.md)

***  
  
  
>
>
> | **[Linked in](https://linkedin.com/in/owen-pauptit/)** | **[GitHub](https://github.com/owenpauptit/)** |
>
