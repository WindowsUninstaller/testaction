import time
print('Hello, Actions!')
with open('output.bin', 'w') as file:
    print('Hello, Actions!', file=file)
    print(f'time:{time.time()}', file=file)
    print(f'perf_counter:{time.perf_counter()}', file=file)
