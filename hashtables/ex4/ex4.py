def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for number in a:
        # start cache with 1 because 0 is neither negative nor positive
        cache[number] = 1
        if number != 0 and -number in cache:
            # abs will normalize appending only positive numbers
            result.append(abs(number))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
