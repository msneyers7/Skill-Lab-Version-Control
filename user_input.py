def get_int_input(msg: str = "Please input an integer: ", error: str = "Invalid integer!") -> int:
    counter: int = 100 # ends after 100 tries
    while counter > 0:
        try:
            value: int = int(input(msg))
            return value
        except:
            print(error)
            counter -= 1
    raise RuntimeError("Exceeded maximum entry limit.")
