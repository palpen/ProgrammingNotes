# Notes and Basic template for designing shell scripts with options parsed using case statements

```bash
#!/usr/bin/env bash

# Script name: my_script.sh

usage() {
    echo -n "
    Synopsis:

    This is my script

    Usage:
        $0 -b | --begin <YEAR> -e | --end <YEAR>  --option1 | --option2 [--num_workers] <INTEGER>

        -h --help                   Display usage information
        -b --begin                  First year of data to process (e.g. 2010)
        -e --end                    Last year of data to process (e.g. 2015)
        --option1 --option2         Option to execute
    "
}

if [ $# -eq 0 ]; then
  echo ""
  echo "ERROR: missing required arguments - see usage below."
  echo ""
  usage
  exit 1
fi

while [ "$1" != "" ]
    do
        case $1 in
            -b | --begin )  shift
                            BEG=$1
                            ;;
            -e | --end )    shift
                            END=$1
                            ;;
            --option1 )     RUN="--option1"
                            ;;
            --option2 )     RUN="--option2"
                            ;;
            -h | --help )   usage
                            exit
                            ;;
            * )             usage
                            exit 1
        esac
        shift
    done

echo "Beg: $BEG, End: $END, Run: $RUN, Number of Workers: $NUM_WORKERS"
```

Positional parameters passed to the script from the command line will be stored in the local variables $1, $2, $3, etc. $0 is reserved for the scripts file name (e.g. `my_script.sh`).

Executing `my_script.sh -b 2001 -e 2010 --option1` stores `-b` in `$1`, `2001` in `$2`, so on and so forth with `--option1` stored in `$5`.

In the while loop above, using case statement will check the value of `$1`. If if it matches `-b` or `--begin`, the `shift` operator will "shift" the parameters so that the parameter `2001` will now occupy `$1`, `-e` will now occupy `$2`, and so on. The "new" value of `$1` will be stored in `BEG`.

Having found a match, case will exit, the the shift operator is once again called to move `-e` to `$1`, which was previously occupied by `2001`. Because `$1` is not empty, we enter case again and repeat the previous steps until all the passed in parameters have been consumed.

Case statements need not be used in a while loop. It is useful for checking the value of a variable among a set of known values. It saves one from having to use multiple `if` statements, which can clutter ones code:

```bash
NAME="john"

case $NAME in
    mike )  echo "Name is mike"
            ;;
    neil )  echo "Name is neil"
            ;;
    john )  echo "Name is john"
            ;;
    steve ) echo "Name is steve"
            ;;
    * )     echo "Name not on list..."
            exit 1
esac
```


