from main import farewell, greet


def test_greet():
    assert greet("world") == "Hello, world!"


def test_farewell():
    assert farewell("world") == "Goodbye, world!"
