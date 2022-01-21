# Putupe

Putupe (pronounced pytype) is a minimal terminal typing practice program.

Give it a text file and it will present it one line at a time for you to rewrite.

## Screenshot

<img src="https://i.imgur.com/LQuGG3p.png">

## Installation

    git clone https://github.com/dvolk/putupe
    cd putupe
    pip3 install argh blessed

## Running

    python3 putupe.py <text file>

Press enter once the line you entered matches the line presented to continue to the next line.

Press escape to leave the program. When exiting it prints the line you were last on, and this can be resumed with the `-r` argument.

Your text file must be word wrapped to a line length less than the terminal width.
