# print(
#     ' ab '.strip()
# )
import datetime
from pathlib import Path

print(datetime.datetime.utcnow())
p = Path('nodejs') / 'temp.txt'

open(p.resolve(), 'wb')
# print(str(p))
