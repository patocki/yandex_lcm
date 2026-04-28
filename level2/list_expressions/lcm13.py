print(
    *[
        "".join(
            {let.lower() for word in input().split() for let in word if let.isalpha()}
        )
        for _ in range(int(input()))
    ],
    sep="\n",
)
