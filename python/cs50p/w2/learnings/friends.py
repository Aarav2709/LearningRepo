# This is a {Dictionary} embedded into a [List]! Left to colon is Key and colon to Right is the Value associated.
friends = [
    {"name": "Aarav", "nickname": "Aaru", "hobby": "Coding"},
    {"name": "Aditya", "nickname": "Adi", "hobby": "Studying"},
    {"name": "John", "nickname": "Johnny", "hobby": "Yapping"},
    {"name": "Pranjal", "nickname": "Prawn", "hobby": "Caring"},
]

# Good ol' loop.
for friend in friends:
    print(
        "Name is",
        friend["name"],
        "Nickname is",
        friend["nickname"],
        "Hobby is",
        friend["hobby"],
        sep=": ",
    )
