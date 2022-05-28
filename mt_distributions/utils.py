def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
    
def frange(start, stop, step=0.1):
    start = float(start)
    stop = float(stop)

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1