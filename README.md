**POINTS - 10**
>>CONTENTS
>1. About Project
>2. UML DIAGRAMS
>3. PROJECT REQUIREMENTS
>4. Analysis
>5. DDD-Domain Driven Design
>6. Metrics
>7. CCD-Clean Code Development
>8. Build Management
>9. Unit Tests
>10. IDE-Integrated Development Environment
>11. Functional Programming
>+ GIT COMMIT HISTORY




**About Project**
>> Number Guessing Game - Pet Coding Project Introduction

   The Pet Coding Project presents a simple number guessing game designed to reinforce basic programming skills while incorporating modern programming best 
   practices. This project aims to restore and enhance proficiency in fundamental language concepts such as variables, data types, conditional logic, loops, 
   functions, and classes. By implementing a straightforward game function, the researcher can focus on the right technology without getting overwhelmed by 
   complexity. The game is coded in Python, taking advantage of its simple syntax and extensive libraries.

>> Game Overview

The number guessing game generates a random integer between 1 and 100 using Python's built-in random module. Players attempt to guess the generated number, and validation ensures that only valid integers are accepted. The game allows multiple guesses within loops, and functions divide the execution into logical parts, such as initializing the game, asking for inputs, checking assumptions, and computing results.


**UML DIAGRAMS**


  I used the draw.io for generating/draw the UML diagrams.These diagrams helps to concept different aspects of the system before any code.They can also serve as a useful documentation for understanding and maintaining the application.
+ [ACTIVITY UML DIAGRAM](https://github.com/astaade/pet_project/blob/main/UML/ACTIVITY%20DIAGRAM.png)
  >>This models the flow of actions in the game
+ [CLASS UML DIAGRAM](https://github.com/astaade/pet_project/blob/main/UML/CLASS%20DIAGRAM.png)
  >>Shows key classes and relationships.
+ [USE CASE DIAGRAM](https://github.com/astaade/pet_project/blob/main/UML/USE%20CASE%20DIAGRAM.png)
  >>This depits the hardware and connections.

**PROJECT REQUIREMENTS**
 + [DASHBORD IN TRELLO.png](https://github.com/astaade/pet_project/blob/main/PROJECT%20REQUIREMENTS/DASHBORD%20IN%20TRELLO.png)
 + [PIE CHART IN JIRA.png](https://github.com/astaade/pet_project/blob/main/PROJECT%20REQUIREMENTS/PIE%20CHART%20IN%20JIRA.png)


**Analysis**

 >>A)ANALYSIS CHECKLIST[LIST](https://github.com/astaade/pet_project/blob/main/ANALYSIS/ANALYSIS%20CHECKLIST.pdf)

> >B)ANALYSIS EXPLANATION[EXP](https://github.com/astaade/pet_project/blob/main/ANALYSIS/ANALYSIS%20pdf.pdf)

**DDD-Domain Driven Design**

To expand the breadth of the game for domain modeling, this project  invented some additional capabilities:
-Multiplayer Mode
-Platform High Score Tracking
-Power-Ups and Bonuses
-Multiple Difficulty Settings
-Visual Representations And Animations
 + [Domain Mapping](https://github.com/astaade/pet_project/blob/main/DOMAIN%20DRIVEN%20DESIGN/DOMAIN%20MAPPING.png)
   >>The domain mapping diagram depicts the conceptual domains relevant to the guessing game application and the relationships between them. It was created in this project using the draw.io tool to visualize and expand upon the core gameplay functionality during the analysis phase.
   
 + [Core Concepts Chart](https://github.com/astaade/pet_project/blob/main/DOMAIN%20DRIVEN%20DESIGN/CORE%20CONCEPT%20CHART.png)
   >> The core concepts chart shows the key classes that will implement the logical components of the system design, supporting the domain model. Representing software artifacts visually in standardized modeling notations aids in communication, creativity, and setting direction before physical construction.

**Metrics**

To track code quality, this project integrated Sonarcloud which provides a detailed quality report including metrics like:
- Unit test coverage
-ode duplication
-Technical debt
-Coding standards
-Potential bugs
>>[SONAR CLOUD METRICS.png](https://github.com/astaade/pet_project/blob/main/metrics/SONAR%20CLOUD%20METRICS.png)


>SONAR CLOUD REPORT[REPORT](https://github.com/astaade/pet_project/blob/main/METRICS/SONAR%20Cloud%20Report.pdf)

**CCD-Clean Code Development**

 1) Why it is clean code[CCD Pdf](https://github.com/astaade/pet_project/blob/main/Clean%20Code%20Development/ccd%20pdf..pdf)

 2) Cheat sheet[CCD](https://github.com/astaade/pet_project/blob/main/Clean%20Code%20Development/Clean%20Code%20Development%20(CCD)%20cheat%20sheet.pdf)

**Build Management**

 >>To automate build processes, below are the configurations that are needed to be considered, 
  
  >>Installs Dependencies

  >>Runs Unit Test Suite

  >>Builds Documentation

  >>Deploys To Staging Server
>  ![image](https://github.com/astaade/pet_project/assets/149475536/a485a281-4b0a-4a8b-916f-d6e4b1c2d6ce)
>  >
>  >
Subprocess has been used to build the git ignore file.

**Unit Tests**

>>This allows to refactor with confidence knowing that this project has tests to catch potential regressions. Tests are executed during CICD pipelines.

--Debugging

>>Git Integration
>>Interactive Python Console
>>Unit Test Runner
>>Documentation Support

**IDE-Integrated Development Environment**

  >>Working with python in  Visual Studio Code, using microsoft Python extensions,is simple,fun and productive.

  >>It leverages all of VS Code's power to provide auto complete and intellisense ,linting,debugging,and unit testing,along with the ability to easily switch between Python environments ,including virtual and conda environments.

  >>favorite keys

     --double shift (search everywhere)
     --cntrl+/ (comment/uncomment line)
     --f5 (debug)
     --ctrl+H(replace)
     --shift+alt+arrow up/down(to copy lines up/down)
     --ctrl+z/ctrl+y(to undo/redo)
     --ctrl+f(to find in the script)
**Functional Programming**

CLEAN CODE[CLEAN CODE](https://github.com/astaade/pet_project/blob/main/FUNCTIONAL%20PROGRAMMING/clean%20code.py)

>>BUILD.GRADLE[BUILD GRADLE](https://github.com/astaade/pet_project/blob/main/FUNCTIONAL%20PROGRAMMING/build.gradle)

>>GAME[GAME](https://github.com/astaade/pet_project/blob/main/FUNCTIONAL%20PROGRAMMING/game.py)
>>
>>TRELLO[TRELLO](https://github.com/astaade/pet_project/blob/main/FUNCTIONAL%20PROGRAMMING/trello.csv)



**GIT COMMIT HISTORY**
[HISTORY](https://github.com/astaade/pet_project/commits/main/README.md)
