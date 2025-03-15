

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.lower()
    return full_name


def main():
    print("Hello World!")
    print( get_full_name("JOHN", "Houston"))

if __name__ == "__main__":
    main()
