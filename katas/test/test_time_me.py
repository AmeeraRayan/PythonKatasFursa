import unittest
import time
from katas.time_me import measure_execution_time

class TestMeasureExecutionTime(unittest.TestCase):
    def test_sample_function(self):
        def sample_function():
            time.sleep(0.5)  # Sleep for 500 milliseconds

        time_taken = measure_execution_time(sample_function)
        # Check that time is around 500ms (give it some range like 450 to 550)
        self.assertTrue(450 <= time_taken <= 550)

    def test_quick_function(self):
        def quick_function():
            pass  # Very quick, does almost nothing

        time_taken = measure_execution_time(quick_function)
        # Check that time is very small (less than 10ms)
        self.assertTrue(time_taken < 10)

    def test_function_with_print(self):
        def printing_function():
            print("Hello!")

        time_taken = measure_execution_time(printing_function)
        # Still very fast, check under 50ms
        self.assertTrue(time_taken < 50)

    def test_function_with_calculation(self):
        def calc_function():
            sum(range(100000))  # Do a small calculation

        time_taken = measure_execution_time(calc_function)
        # Should be very fast, under 50ms
        self.assertTrue(time_taken < 50)
