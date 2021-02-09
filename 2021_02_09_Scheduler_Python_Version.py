import time

def schedule(f, n):
    time.sleep(n / 1000.0)
    f()

def test_func():
    print('Done')

schedule(test_func, 3000)
