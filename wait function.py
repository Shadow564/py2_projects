from datetime import datetime
def wait(seconds):
    start = datetime.now()
    lag = datetime.now()
    while lag.second - start.second < seconds:
        print lag.second - start.second
        lag = datetime.now()
        
    return str(seconds) + " second(s) have passed."

print wait(1)
