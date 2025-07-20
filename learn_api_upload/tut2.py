def greet(name: str) -> None:
    print(f"Hello, {name}")

def farewell(name: str) -> str:
    return f"Good Bye, {name}"

def main() -> None:
    greet("Alice")

    msg = farewell("Alice")

    print(msg)




if __name__ == "__main__":
    main()