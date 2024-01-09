# CodeInstitute-Project-2
<H1>Battleship game</H1>
Welcome to Battleships! This is a simple implementation of the classic game Battleships in Python.
You can play the game online by visiting [Battleships Game](https://example.com/battleships).

<img width="1147" alt="image" src="https://github.com/mick-s9/CodeInstitute-Project-3/assets/65968792/e9514e39-5daa-4dbf-9d90-93b8c61a1a16">



<h1>How to play</h1>
In this version of the Battleship game, the player determines the grid size and the number of ships to sink. Once both numbers are entered (which must be greater than 2 and 0, respectively), two grids are generated—one for the user and one for the computer.
Guesses are marked on the board with an X and. Hits are indicated by *.


<h1>Features</h1>
<ul>
    <li>The player selected the board size and the number of battleships to insert on the grig</li>
    <img width="572" alt="image" src="https://github.com/mick-s9/CodeInstitute_Project_2/assets/65968792/b1182fcd-fa17-495a-b035-594947c4f42b">
    <li>The two grids appear where in the player grid the ships are marked with an</li>
    <img width="599" alt="image" src="https://github.com/mick-s9/CodeInstitute-Project-3/assets/65968792/aa918de0-2fdc-4f5e-bc4c-20125fb624af">
    <li>Once the coordinates are entered, if a ship is hit it will be displayed on the grid with *</li>
    <img width="476" alt="image" src="https://github.com/mick-s9/CodeInstitute-Project-3/assets/65968792/42a7fd3c-d032-4d75-a9e0-867ff667910b">
    <li>If coordinates are entered that are outside the grid, the program will ask you to enter the numbers again (column and row)</li>
    <img width="401" alt="image" src="https://github.com/mick-s9/CodeInstitute-Project-3/assets/65968792/e4237b96-a074-417d-a203-59942f43d61f">
    <li>At the end of each round a message showing the score is displayed</li>
    <img width="466" alt="image" src="https://github.com/mick-s9/CodeInstitute-Project-3/assets/65968792/b99aa1ec-e50c-4a1a-84b6-d950371e1954">
    <li>When one of the two players hits all of the other's ships, a message appears with the total number of attempts. You are then asked if you want to play another game</li>
    <img width="710" alt="image" src="https://github.com/mick-s9/CodeInstitute-Project-3/assets/65968792/35dc1aee-3353-43d8-9fd7-4b20ea6b99e1">
</ul>

<h1> Data Model</h1>
<p>The game is played through the main loop of play_battleships(), which repeats until the user decides not to play anymore. During each turn, the user's and the computer's grids are displayed, users make their guesses, and game end conditions are checked. At the end of each game, scores are printed, and the user can decide whether to play again.</p>
<ol>
    <li><code>create_grid(size)</code>: Function that returns a grid of size <code>size x size</code> with all elements initialized to '0'.</li>
    <li><code>print_grid(grid)</code>: Function that prints the provided grid.</li>
    <li><code>place_battleships(grid, num_ships)</code>: Function that randomly places a specified number of battleships (<code>num_ships</code>) on the grid.</li>
    <li><code>calculate_distance(grid, x, y)</code>: Function that calculates the distance between a position <code>(x, y)</code> and the nearest battleship on the grid.</li>
    <li><code>get_user_guess(size)</code>: Function that prompts the user to enter coordinates to guess the position of a battleship on the grid.</li>
    <li><code>get_computer_guess(size)</code>: Function that randomly returns the coordinates of the computer's attempt to hit a battleship on the user's grid.</li>
    <li><code>count_total_sunk(grid)</code>: Function that returns the total number of sunk battleships on the grid.</li>
    <li><code>copy_stars(source_grid, destination_grid)</code>: Function that copies the '*' from the source grid to the destination grid.</li>
    <li><code>play_battleships()</code>: Main function that manages the game flow.</li>
</ol>

<h1>Testing</h1>
<p>I have manually tested this project by doing the following:</p>
<ul>
    <li>Passed the code through a PEP8 linter and confirmed there are no problems</li>
    <li>Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice</li>
    <li>Tested in my local terminal and the Code Institute Heroku terminal</li>
</ul>

<h1>Deployment</h1>
<p>This project was deployed using Code Institute's mock terminal for Heroku.</p>
<ul>
    <li>Fork or clone this repository</li>
    <li>Create a new Heroku app</li>
    <li>Set the buildpacks to Python and Node.js in that order</li>
    <li>Link the Heroku app to the repository</li>
    <li>Click on Deploy</li>
</ul>

