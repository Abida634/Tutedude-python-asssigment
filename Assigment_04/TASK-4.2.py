# TASK - 2
# Write and Append Data to a file

text = input("Enter text to write to the file: ")
f = open("output.txt", "wt")
f.write(text)
f.close()

print("Data successfully written to output.txt.")

text2 = input("Enter additional text to append: ")
f = open("output.txt", "a")
f.write("\n" + text2)
f.close()

print("Data successfully appended.")

print("Final content of output.txt:")
f = open("output.txt", "r")
data = f.read()
print(data)
f.close()
