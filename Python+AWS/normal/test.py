from datetime import datetime

ts = datetime.now()

print('date in date time format' ,ts,type(ts))

ts = ts.timestamp()

print('date in float format', ts, type(ts))
