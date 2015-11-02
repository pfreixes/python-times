# python-times

Get the real, user and system time used by your Python programs from your
Python code.

This package implements a new type called Times to pick up the real, user
and system time used for a while by one Python program. This type is a 
Python implementation of the bash command called *time* to be used by the
programmer to check those times wherever of code he want.

Once the Times is instantiated it picks up the current values of the clock
system using the *times* syscall, to get the time spent from when the 
Times has instatiated we use the times method publised by the Times type.

As exampe:

```python
import time
from times import Times
t = Times()
time.sleep(1)
print "Real {0}s, User {1}s, Sys {2}s".format(*t.times())
```

## Install

Python-times comes with the minium files to be installed as a Python package build
using the setuptools. Install it can be done following the following command.

```bash
$ python setup.py install
```

## Contributing and testing

To run the tests firt you should create a virtualenv where Times will be
deployed in development way. Use the following instructions for that:

```bash
$ mkvirtualenv python-times
$ python setup.py develop
```

And then just executes the test with the following command

```bash
$ python test_times.py
.
----------------------------------------------------------------------
Ran 1 test in 1.002s

OK
```
