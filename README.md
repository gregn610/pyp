The Pyed Piper (pyp)
====================

The original project page on Google Code here: http://code.google.com/p/pyp/

Installation
------------

    git clone https://github.com/alexbyrnes/pyp.git
    cd pyp
    chmod u+x pyp
    # Optionally: cp pyp /usr/local/bin

It's handy to put pyp into a directory on your path (for example /usr/local/bin) so you can type "pyp" instead of "./pyp".


####Background

Pyp, or The Pyed Piper, is an incredibly useful command line tool for:

* High volume transformations of unstructured data
* Operations that aren't available in Unix/Linux, or aren't easy
* Thinkers-in-python


####Usage

Filters

    cat very_large_file.csv | pyp -L " len(p) > 5 " > only_long_lines.csv
    
Regular Expressions

    cat very_large_file.csv | pyp -L " p.re('[0-9a-fA-F]*') " > only_hex_digits.csv
    
Compose multiple operations

    cat v ery_large_file.csv | pyp -L " p.upper() | whitespace | p[:2] " > first_two_colums_uppercase.csv
      
Many more examples in the manual, and in the test files test.sh and tests_orig.sh.


####Running the Tests

The tests are currently just a list of commands comparing the original output to the -L flag ouput:

    ./tests.sh > Ltests
    ./tests_orig.sh > noLtests
    diff Ltests noLtests #Should be blank    


#####New Features

* -L flag for large (> 50,000 line) files
* --DEBUG to debug output with line numbers and stack trace
* -D to output tab delimited text.  The large file flag includes this automatically.  Add -S to specify the delimiter.

