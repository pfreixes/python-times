# python-times

Get the real, user and system time used by your Python programs from your
Python code.

This package implements a new type called Times to pick up the real, user
and system time used for a while by one Python program. This type is a 
Python implementation of the bash command called *time* to be used by the
programmer to check those times as many times as he want in running time.

Once the Times is instantiated it picks up the current values of the clock
system using the [times syscall](http://linux.die.net/man/2/times) to get after
a while the real, user and system time spent at some specific point using the
*Times.times* method.

As exampe:

```python
>>> import time
>>> from times import Times
>>> t = Times()
>>> time.sleep(1)
>>> print "Real {0}s, User {1}s, Sys {2}s".format(*t.times())
Real 1.21s, User 0.0s, Sys 0.0s
```

Sometimes know the time consumed by our programs splitted between the real, user
and system time is useful to find out where our program is really consuming the time.
The following snippet of Python code finds out the cost of create 10K threads.

```python
import threading
import times

class MyThread(threading.Thread):
    def run(self):
        # do nothing and return
        pass

t = times.Times()
threads = [MyThread() for i in xrange(10000)]
map(lambda t: t.start(), threads)
map(lambda t: t.join(), threads)
print "Real {0}s, User {1}s, Sys {2}s".format(*t.times())
```

The output shows that the major time is still consumed by the Python code and not 
by the Operating System:

```bash
$ python threads.py 
Real 0.47s, User 0.43s, Sys 0.18s
```

*The System time and User time are the CPU-times consumed by the programs. In scenarios
with many processors and many threads as the previous example, the Real time would be lesser
than the sum of the System and User times*

## Install

Python-times comes with the minium files to be installed as a Python package build
using the setuptools. Install it can be done following the following command.

```bash
$ python setup.py install
```

## Contributing and testing

To run the tests first you should create a virtualenv where Python-times will be
deployed in development way. Use the following instructions:

```bash
$ mkvirtualenv python-times
$ python setup.py develop
```

And then just execute the test with the following command

```bash
$ python test_times.py
.
----------------------------------------------------------------------
Ran 1 test in 1.002s

OK
```
