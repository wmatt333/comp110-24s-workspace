"""A practice memory diagram."""

i: int = 0
s: str = ""

while i < 4:
    if i % 2 == 0:
        s += "h"
    elif i % 3 == 0:
        s += "!"
    else:
        s += "e"
    i += 1
print(s)