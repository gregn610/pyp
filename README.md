pyp - The Pyed Piper
====================

The original project page on Google Code here: http://code.google.com/p/pyp/

Installation
------------

    pip install git+git://github.com/alexbyrnes/pyp.git


#####Background

Pyp, or The Pyed Piper, is an incredibly useful command line tool for:

* High volume transformations of unstructured data
* Operations that aren't available in Unix/Linux, or aren't easy

*Note: This is currently exactly verion 2.11 of pyp with the -L flag to process large (> 50,000 line) files.  Uses [generators](http://en.wikipedia.org/wiki/Generator_%28computer_programming%29#Python) internally.*

#####Usage

    cat /tmp/very_large_file.csv | ./pyp -L " p.upper() | whitespace | p[:2] " > first_two_colums_uppercase.csv
    
    
#####Roadmap

* Better type handling
* Error handling with row numbers
 

    
    
    

