from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    if n%2 == 0:
        time.sleep(5)
        return "Even Number.."

#fx(2) and fx(4) isn't stored in cache, so will run late
print(fx(2))
print("Done for 2.")
print(fx(4))
print("Done for 4")

#fx(2) is stored in cache, so it runs instantly
print(fx(2))
print("Again for 2..")
