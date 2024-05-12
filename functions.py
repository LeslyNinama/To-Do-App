def get_todos(filepath="todos.txt"):

    """reads a text file and returns the list of
    to-do items"""

    with open(filepath, "r") as file:
        todos = file.readlines()
        return todos


def write_todos(todos_args, filepath="todos.txt"):
    """Write the to-do intem list in the text file"""

    with open(filepath, "w") as file:
        file.writelines(todos_args)


print(__name__)


if __name__ == "__main__":
    print("Hello")
    print("How the fuck you did this ?")
