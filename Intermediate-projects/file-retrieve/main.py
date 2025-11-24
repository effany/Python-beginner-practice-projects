with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


with open("my_file.txt", mode="a") as file:
    file.write("\nNew text")


# when open in write mode, if the file dont exsit, it'll create a new one