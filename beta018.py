from contextlib import contextmanager
import time

class timeMeasurement:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {self.elapsed_time:.2f} seconds")
    

with timeMeasurement() as tm:
    # Simulate a long-running process
    time.sleep(2)


@contextmanager
def time_measurement():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

with time_measurement():
    # Simulate a long-running process
    time.sleep(2)
    