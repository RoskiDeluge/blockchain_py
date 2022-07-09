# f = open('demo.txt', mode='w')
# f.write('Hello from python.')
# f.close()

# f = open('demo.txt', mode='a')
# f.write('Add this content.\n')
# f.close()

# f = open('demo.txt', mode='r')
# f.write('Add this content.\n')
# file_content = f.read()
# file_content = f.readlines()
# f.close()

# for line in file_content:
#     print(line[:-1])

# print(f.readline())

# f = open('demo.txt', mode='r')
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
# f.close()

with open('demo.txt', mode='r') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
print('Done')
