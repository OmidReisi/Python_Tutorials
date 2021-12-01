import Advanced.__name__.name_main_1

# import name_main_1


print(f"This is the name of the file (name_main_2.py) : {__name__}")


# this checks if this file being run directly then execute main() function
def main():
    print("This file is being run directly")


if __name__ == "__main__":
    main()
