Usage: python3 anonymous.py "full program run in a string"

or get into your .bashrc and type in 

alias anon='python3 ~/path/to/anonymous.py'

then use

anon "full program run in a string"

remember when you first install an alias you'll need to restart the terminal completely to be able to use it from the .bashrc

Processes and subprocesses that are run through anonymous can not escape the lambda sandbox, that means no writing to file.
