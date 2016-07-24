# Comparisons

Count the number of comparisons used to sort the input by Quick Sort algorithm.

## Sample client

Client options:

    $ ./client.py -h

Count the number of comparisons when sorting a list of integers read from the
standard input or a file, using the default pivot option:

    $ ./client.py numbers.txt

    2092227

Count the number of comparisons when sorting a list of all integers between
1-100000 in random order, using the default pivot option:

    $ ./client.py -b 100000

    2081547

Count the number of comparisons when sorting a list of all integers between
1-100000 in random order, using the median-of-three pivot option:

    $ ./client.py -b 100000 -p median

    1693897
