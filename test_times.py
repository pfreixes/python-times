import times
import time
import unittest

class TestTimes(unittest.TestCase):
    def test_times(self):
        t = times.Times()
        time.sleep(1)
        real, user, sys = t.times()

        # just check the real time spent
        assert real >= 1.0

if __name__ == '__main__':
    unittest.main()
