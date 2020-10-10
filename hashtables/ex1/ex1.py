def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    for i, weight in enumerate(weights):
        try:
            second_i = cache[limit - weight]
        except:
            cache[weight] = i
        else:
            return tuple([i, second_i])

    return None
