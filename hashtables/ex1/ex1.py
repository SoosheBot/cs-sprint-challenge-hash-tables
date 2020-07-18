def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    # if the key is present, get() the key
    for i in range(length):
        results = cache.get(limit - weights[i])
    
        if results != None:
            return i, results
        
        cache[weights[i]]


    return None
