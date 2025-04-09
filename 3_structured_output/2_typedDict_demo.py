from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int


person1: Person = {"name": "Darshan Subedi", "age": 20}
person2: Person = {"name": "Darshan Subedi", "age": "20"} # does not give error

print(person1, person2)