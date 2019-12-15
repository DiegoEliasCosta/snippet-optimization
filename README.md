# snippet-optimization

Project description to be added...


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Our project combines JupyterNotebook and Luigi in order to provide a flexible pipeline structure for code processing.
Therefore, in order to run the tasks you need to have installed in your system the following programs.

```
Python 3
Luigi - upgrade luigi to 2.8.8
Jupyter Notebook
```

## Running the tasks

1. With luigi daemon
luigid

Note that my_module needs to be in your PYTHONPATH, or else this can produce an error (ImportError: No module named my_module). Add the current working directory to the command PYTHONPATH with:

```
cd tasks
PYTHONPATH='.' luigi --module my_module MyTask
```

2. Without luigi daemon and local scheduler
```
cd tasks
PYTHONPATH='.' luigi --module my_module MyTask --local-scheduler
```

Luigi GUI could be seen at http://localhost:8082/

## Running the task earlier way
First of all, we need to launch the Luigi daemon with:

```
	luigid
```

This daemon will be responsible for scheduling and executing the tasks.

There are two ways to run a specific Luigi task:

```
	luigi --module my_module MyTask [parameters]
```

or 

```
	python -m luigi --module my_module MyTask [parameters]
```

Note that if a parameter name contains ‘_’, it should be replaced by ‘-‘. For example, if MyTask had a parameter called ‘my_parameter‘:

```
	luigi --module my_module MyTask --my-parameter 100 
```

## Developing a new Task

TBD
