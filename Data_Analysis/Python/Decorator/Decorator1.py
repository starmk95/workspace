import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"실행 시간: {end - start:.4f}초")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("작업 완료!")

slow_function()