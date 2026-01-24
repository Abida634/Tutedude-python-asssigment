# TASK - 1
# Read a File and Handle Errors

print("Reading file content:")

try:
    f = open("sample.txt", "rt")

    line1 = f.readline()
    print("Line 1:", line1.strip())

    line2 = f.readline()
    print("Line 2:", line2.strip())

    f.close()

except:
    print("Error: The file 'sample.txt' was not found.")





