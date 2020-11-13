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
## My queries executor syntax

This is an illustrative and non-formal version of the grammar that is stored in the syntax_grammar.txt file and is used in my project.

For productions, correct expressions are used from the point of view of scripting.

Observing the described rules and correctly substituting the right parts, you will write the correct script.

```python
#main expressions:
Script - text with one Statement on each line
Statement -> connect String;
Statement -> create_named_pattern(String, Pattern); #add new production to grammar
Statement -> select Object from Graph;
Graph -> intersect(Graph, Graph)
Graph -> query(Pattern)
Graph -> set_start_and_final(Vertices, Vertices, Graph)
Graph -> String #path to file with graph
Vertices -> range(Int, Int)
Vertices -> { IntList }
Vertices -> none
Object -> ObjectCollection | ObjectAggregated
ObjectCollection -> edges
ObjectCollection -> filtered_edges(Condition, ObjectCollection)
ObjectAggregated -> count(ObjectCollection)

#auxiliary expressions:
Pattern - regex string. 
Pattern -> String
Pattern -> Pattern+
Pattern -> Pattern*
Pattern -> Pattern?
Pattern -> Pattern or Pattern
Pattern -> (Pattern)(Pattern) #for соnсаt
Pattern -> (Pattern)
Pattern -> term(String)
Pattern -> nonterm(String)
Condition -> (String, String, String => Boolean)
Condition -> Condition or Condition
Condition -> Condition and Condition
Condition -> not Boolean
Condition -> (Condition)
Boolean -> is_start
Boolean -> is_final
Boolean -> String == String
Boolean -> Boolean or Boolean
Boolean -> Boolean and Boolean
Boolean -> not Boolean
Boolean -> (Boolean)
String - string of lowercase letters
Int - numeric value
IntList - comma separated list of Int
```

## Script code style:
* Only lower case characters
* One line - one statement
* There is ';' at the end of the statement
* There is one blank after every comma
* For list of values uses this format: "{\_val1,\_val2\_}" where \_ - only one blank

## Expressions examples:
#### Script:
```
connect somedatabase;
create_named_pattern(astar, (a)*);
select filtered_edges((u, e, v => is_final), filtered_edges((u, e, v => e == b), edges)) from intersect(firstgraph, secondgraph);
```
#### Statement:
```
connect somedatabase;
``` 
```
create_named_pattern(anystring, pattern);
``` 
```
select edges from graph;
``` 
Additional examples of expressions you can find in syntax_expressions_data.txt
____
## Syntax checker usage:
```
python syntactic_analyzer.py [-h] --script %SCRIPT_PATH% [--syntax %SYNTAX_PATH%]
```
### Arguments:
```
--script - path to file with script
--syntax - path to file with syntax
```
### File formats:
#### Syntax: (pyformlang.cfg format)
```
The text contains one rule per line.
The structure of a production is:
head -> body1 | body2 | ... | bodyn
where | separates the bodies.
A variable (or non terminal) begins by a capital letter.
A terminal begins by a non-capital character
Terminals and Variables are separated by spaces.
```
#### Script format depends on your syntax
____
## Query execution usage:
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
