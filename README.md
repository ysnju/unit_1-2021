# Unit 1: A classic game 
![](game.gif)

# Criteria A: Planning

## Problem definition

The owner of the local game shop is an enthusiast of classic computer games. He has been looking for a talented programmer that can help him revive his passion for text-based games. He has few requirements for this task:

1. The game has to be entirely text-based.
2. The game must record the time played.
3. The game must record the player name and score.

## Proposed Solution
I will design and make a Text-based game for a client who is an owner of a local game shop. The Text-based game will be made in the Mac computer and is constructed using the software Python. I wil use python3 because it is the only programming language I know, but more than that, it is the most used programming language, meaning that I would be able to get more help.Also it will allow other users to access the code and adjust it to their own liking. It will take  30+hours to make and will be evaluated according to the criteria A,B and C.

The game is a RPG of a cat in ISAK. This game will be developed to introduce the food in ISAK, and the life in ISAK. 

Apart for this requirements, the owner is open to any type of game, topic or genre.

## Success Criteria
1. The game is entirely text-based.
2. The game must record the time played.
3. The game must record the player name and score
-Original-
4. The game will allow the player to input a number to increase the difficulty.
5. The game will allow the player to end up with three different results.
6. The game will allow the player to save and resume while the game at every end of the chapter.

## Software testing

## [Unit testing]

First I started with unit testing because I have used functions often. By using functions often, it makes unit testing easy to check errors in each function. Making it easier to identify where the bug is.

1.Testing [introduction] ○
Because it was a simple code mainly constructed with printing and if and else statement executes.
<img width="982" alt="Screenshot 2021-10-27 at 14 48 54" src="https://user-images.githubusercontent.com/89366347/139007213-8ba009c5-4b2c-42c9-a9ed-c5bac15c2a73.png">

2.Testing [secret encoder] ○
This worked since the function was supposed to make all of the letters small, and was supposed to move the letters 17 times, which makes Anju→real

<img width="982" alt="Screenshot 2021-10-27 at 14 50 41" src="https://user-images.githubusercontent.com/89366347/139007357-0a640302-63f0-460f-8a18-1b333d83b9e2.png">

3. Testing each file ×
This did not work to all of the files. This game is made with 5 files in total. From the results 1 and 2, we can prove that the functions contaned in the files had no problem. This identified that the error came from the connection between the files.

## Integration Testing

By doing the integration testing, errors occored. The main cause of the errors were because the code [import] was used in multiple files. This caused the files to import each other. As a result, the exact same errors where shown when each file was unit tested.

## Performance Testing
Performance testing revealed that improvement was needed in the stop watch function.
When the function was run in the performance test, it showed that no matter how long the user was on the game, it did not change the result. This was not able to be found out unless the performance test. Because this identified that the function did not collorate with the game, it needed to be re coded.

-previous code
<img width="712" alt="Screenshot 2021-10-27 at 15 38 04" src="https://user-images.githubusercontent.com/89366347/139012782-1fe597b3-327b-4505-9064-d6c100230ddc.png">


-improved code
<img width="1064" alt="Screenshot 2021-10-27 at 15 41 01" src="https://user-images.githubusercontent.com/89366347/139013212-0620dda1-2b0b-4353-9375-f8c42e7a6c92.png">

## Usability Testing
Usser friendliness was tested by a different person, in order to make sure that the wording is accurate enough to explain the game. The game creator sometimes does not realise how much explination is needed to a bystander because the ideas and concepts are what the game creator has made. Because I had several friends use the game, I realised the importance of an introduction and rule explination. The program is in python3, and will crash when something unexpected happens. To prevent this, the introduction function was made.

<img width="926" alt="Screenshot 2021-10-27 at 15 45 53" src="https://user-images.githubusercontent.com/89366347/139013914-4cd9ce47-ad3f-4708-bad4-e0cc99506d0b.png">




# Criteria B: Design

## System Diagram

Version where the game was run by single file
![System Diagram 1 0](https://user-images.githubusercontent.com/89366347/138597632-bb995f3d-c302-49e9-87a3-b778bbd7fd30.jpg)
Version where the game runs with 3 files.(However, errors occur)
![System Diagram 1 1](https://user-images.githubusercontent.com/89366347/138598061-4dd3ca2e-30c6-4f45-90a2-c4b3514aa741.jpg)

## Flow Diagrams
![Flowchart1 name_confirm](https://user-images.githubusercontent.com/89366347/138598549-6d25309b-0715-4174-a48a-7bfaf4977027.jpg)

## Record of Tasks
| Task No | Planned Action                                          | Planned Outcome                                                                                        | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create introduction to the game                         | Introduces game rules                                                                                  | 1h            | 10/10                  | B         |
| 2       | Create timer                                            | Shows the time the game has been played by the player                                                  | 1h            | 10/11                  | C         |
| 3       | Create scores                                           | Shows the score of the player                                                                          | 3h            | 10/11                  | C         |
| 4       | Create difficulty                                       | A number inputted by the player will be the difficulty                                                 | 5 min         | 10/21                  | C         |
| 5       | Unit Test: function for encoding witht he Caesar cypher | To check that the function works as expected with input "anju" and key=17, the outcome should be "real | 5min          | 10/7                   | E         |
| 6       | Create story line                                       | N/A                                                                                                    | 1h            | 10/13                  |           |
| 7       | Divide the story line to while loops                    | Shows wrong inputs/ forces the user to the right answer                                                | 1h            | 10/15                  |           |
| 8       | Divide the story line with if                           | Makes the chapters                                                                                     | 30h           | 10/16                  |           |
| 9       | Create ending                                           | prints the name score and total time the user was on the game                                          | 30min         |                        |           |
|         |                                                         |                                                                                                        |               |                        |           |
|         |                                                         |                                                                                                        |               |                        |           |
