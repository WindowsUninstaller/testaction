import time
print('Hello, Actions!')
writetext=f'Hello, Actions!\ntime:{time.time()}\nperf_counter:{time.perf_counter()}\n'
print(writetext)
with open('output.bin', 'w') as file:
    print(writetext, file=file)
