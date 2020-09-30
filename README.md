# Formal-language-tasks
This repository contains solutions to tasks from the course of the theory of formal languages of St. Petersburg State University in 2020
____
## Installation:
This project uses miniconda to download and install packages, if you don't have it installed, the installation script will download and install it itself.

To run the installation script, execute the command:
```
bash install.sh
```
____
## Usage:
```
python main.py --graph %GRAPH_PATH% --queries %QUERIES_FOLDER_PATH% [--fr %FROM_VERTICES_PATH%] [--to %TO_VERTICES_PATH%]
```
### Arguments:
```
--graph - path to file with graph file
--queries - path to folder with regexes
--fr - path to file with start vertices. If not specified, all vertices are used.
--to - path to file with end vertices. If not specified, all vertices are used.
```
### File formats:
#### Graph:
```
0 a 1
0 b 2
1 c 2
```
#### Query:
```
Regex
Example: (a|b)* 
```
#### Fr/To:
```
1 2
```
____
### Benchmarks run:
To run docker use:
```
docker build -t flt . && docker run --rm -it flt
```
In docker, use main.py as usual
____
## Build status: 
master: [![Build Status](https://travis-ci.com/Rimalon/formal-language-tasks.svg?branch=master)](https://travis-ci.com/Rimalon/formal-language-tasks)
____
## Tasks status:
:yellow_square: Task 1

:green_square: Task 2

:green_square: Task 3

:green_square: Task 4

:black_square_button: Task 5

:black_square_button: Task 6

:black_square_button: Task 7

:black_square_button: Task 8

:black_square_button: Task 9

:black_square_button: Task 10

:black_square_button: Task 11
