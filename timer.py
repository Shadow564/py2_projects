from datetime import datetime

print datetime.now()

def time():
  beginer = raw_input("Hit enter when your want to start")
  begin_time = datetime.now()
  bminute = begin_time.minute
  bsecond = begin_time.second
  bmsecond = begin_time.microsecond / 1000
  buffering = raw_input("Hit enter when your done")
  end_time = datetime.now()
  eminute = end_time.minute
  esecond = end_time.second
  emsecond = end_time.microsecond / 1000
  elapsed_minutes = eminute - bminute
  elapsed_seconds = esecond - bsecond
  elapsed_microseconds = emsecond - bmsecond
  if elapsed_microseconds < 0 == True:
    elapsed_microseconds = (1000 - emsecond) + bmsecond
    if elapsed_microseconds >= 1000:
      elapsed_microseconds = elapsed_microseconds - 1000
      elapsed_seconds += 1
    else: pass
  if elapsed_seconds < 0 == True:
    elapsed_minutes -= 1
    elapsed_seconds = (esecond + 60) - bsecond
  print begin_time
  print end_time
  print '%02d:%02d:%03d' % (elapsed_minutes, elapsed_seconds, elapsed_microseconds)

while True:
  time()
