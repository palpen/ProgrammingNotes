# Notes on Makefiles

General format for Makefiles

```
target: dependencies
    command
```

* `target` is the thing that will be created
* `dependencies` are the things that must be available for the command to run
* `command` is the command to run given dependencies (also called the recipe)


## Simple makefile

Create a text file called `Makefile` containing:

```
say_hello:
    echo "Hello there!"
```

Inside the directory containing `Makefile`, run it by executing the command `make`. The output should be

```
Hello there!
```

## Create multiple directories
```
DIR_DATA := data
DIR_BUILD := build

DIRS := $(DIR_DATA) $(DIR_BUILD)

$(DIRS):
    mkdir -p $@
```

## Variable definitions
$@ --> File name of the target of the rule

$^ --> The names of all the prerequisites, with space between them

$< --> The name of the first prerequisite

|  --> order-only pre-requisite: see https://stackoverflow.com/questions/24821611/order-only-prerequisites-not-working-correctly-in-gnu-make/24856711

* good reference: https://stackoverflow.com/questions/24821611/order-only-prerequisites-not-working-correctly-in-gnu-make/24856711


## Misc
* To run a specific make file (say you have multiple make files `Makefile.custom1`, `Makefile.custom2`, etc.), `make -f Makefile.custom1`

# References
* [Original Make manual](https://www.gnu.org/software/make/manual/make.html)
