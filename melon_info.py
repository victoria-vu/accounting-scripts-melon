"""Print out all the melons in our inventory."""


from melons import melons 


def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    # have_or_have_not = 'have'
    # if seedless:
    #     have_or_have_not = 'do not have'

    # print(f'{name}s {have_or_have_not} seeds and are ${price}')

    for melon, attributes in melons.items():
        print(melon.upper())

        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")

        print()

print_melon(melons)
