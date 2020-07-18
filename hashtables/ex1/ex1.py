def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #set an open dict to cache
    cache = {}

    # loop if the key is present, get() the key
    for key in range(length):
        results = cache.get(limit - weights[key])
    
        if results != None:
            return key, results
        
        cache[weights[key]] = key


    return None
