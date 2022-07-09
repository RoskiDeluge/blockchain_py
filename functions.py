def unlimited_arguments(*args, **keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)


# Does not error, but creates a tuple
unlimited_arguments(1, 2, 3, 4, name="Roberto", age=42)

# Unpacking arguments can also be done like this:
# unlimited_arguments(*[1, 2, 3, 4])
