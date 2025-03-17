from typing_extensions import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.lower()
    return full_name

def process_items0(items: list[str]):
    for item in items:
        print(item)

def process_items1(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

def main():
    print("Hello World!")
    print( get_full_name("JOHN", "Houston"))
    l : list[str] = ["François", "Michel", "Robert"]
    process_items0(l)
    d : dict[str, float] = {"first": 100, "second": 200, "third": 300}
    process_items1(d)
    print("Bienvenue with \"{0}\"".format(say_hello('John Deer')))



if __name__ == "__main__":
    main()
