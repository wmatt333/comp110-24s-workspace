"""A basic while loop."""

condition: bool = True
num_loops: int = 0
STOP: int = 2
while condition:
    print(num_loops)
    if num_loops >= STOP:
        condition = False
    num_loops += 1
        
        