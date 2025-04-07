import os

from BinarySearchTree import BinarySearchTree
from Node import Node
from PrintTree import pretty_tree

# tree = BinarySearchTree()
# random = [3, 10, 7, 2, 8, 4, 9, 5, 1, 6]
# sorted = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
# reverse_sorted = [34, 25, 22, 18, 15, 11, 9, 7, 3, 1]
#
# for data in random:
#     tree.insert(Node(data))
#
# print(pretty_tree(tree), tree.height(tree.root))


def readfile(tree, previously_read):
    data = []
    valid = True
    bad_input = True
    error = None
    file_value = None
    os.system("cls" if os.name == "nt" else "clear")
    while bad_input:
        (
            print("Select a File or 'menu' for the Menu:")
            if valid
            else print("Please Select a Valid File:")
        )
        for file in os.listdir():
            if file.find(".txt") != -1:
                print("  ", file)
        if error:
            print("Error: ", error)
        error = None
        value = input(":: ")
        file_value = value
        if value == "menu":
            return
        elif value in previously_read:
            print("File has already been read. ")
            input("Press enter to continue. ")
            return
        try:
            for line in open(value):
                line = line.strip()
                data.append(line)
            bad_input = False
        except Exception as e:
            os.system("cls" if os.name == "nt" else "clear")
            error = e

    try:
        for i, value in enumerate(data):
            if not tree.dataType:
                if value.find(".") == -1:
                    value = int(value)
                else:
                    value = float(value)
            elif tree.dataType is int:
                value = int(value)
            elif tree.dataType is float:
                value = float(value)
            data[i] = value
    except Exception as e:
        print("File is not in proper format. File read terminated.")
        input("Press enter to continue. ")
        return

    for value in data:
        tree.insert(Node(value))
    previously_read.append(file_value)
    print("File Read Successfully. ")
    input("Press enter to continue. ")


options = [
    "Read Data File",
    "Insert",
    "Remove",
    "Print Tree",
    "Search",
    "Check Height",
    "Quit",
]
previously_read = []
tree = BinarySearchTree()

running = True
valid = True
os.system("cls" if os.name == "nt" else "clear")
while running:
    print("Select an Option:") if valid else print("Please Select a Valid Option:")
    for i, opt in enumerate(options):
        print(f"{i}: {opt}")
    inp = input(":: ")
    match inp:
        case "0":
            readfile(tree, previously_read)
        case "1":
            print("Value to insert:")
            while True:
                value = input(":: ")
                try:
                    if value.find(".") == -1:
                        value = int(value)
                    else:
                        value = float(value)
                except:
                    pass
                try:
                    tree.insert(Node(value))
                    break
                except Exception as e:
                    print(f"An error has occured: ", e)
                    print("Please input a valid value ")

            input("Value inserted successfully. Press enter to continue. ")
        case "2":
            print("Value to remove:")
            while True:
                value = input(":: ")
                try:
                    if tree.dataType is int:
                        value = int(value)
                    elif tree.dataType is float:
                        value = float(value)
                except Exception as e:
                    print(f"An error has occured: ", e)
                    print("Please input a valid value ")
                    continue
                try:
                    if tree.search(value):
                        tree.remove(value)
                        input("Value removed successfully. Press enter to continue. ")
                    else:
                        input("Nothing to remove. Press enter to continue. ")

                    break
                except Exception as e:
                    print(f"An error has occured: ", e)

        case "3":
            print(pretty_tree(tree))
            input("Press enter to continue. ")
        case "4":
            print("Value to Search:")
            while True:
                value = input(":: ")
                try:
                    if tree.dataType is int:
                        value = int(value)
                    elif tree.dataType is float:
                        value = float(value)
                    break
                except Exception as e:
                    print(f"An error has occured: ", e)
                    print("Please input a valid value ")
                    continue
            if tree.search(value):
                print("Found")
            else:
                print("Not Found")
            input("Press enter to continue. ")
        case "5":
            height = tree.height(tree.root)
            if height == -1:
                print(
                    "Tree is empty. Please add some values before checking its height. "
                )
            else:
                print(f"Tree's current height is {height}")
            input("Press enter to continue. ")
        case "6":
            running = False
        case _:
            valid = False
    os.system("cls" if os.name == "nt" else "clear")
