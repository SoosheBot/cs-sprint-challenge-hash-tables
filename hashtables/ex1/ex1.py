def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #set an open dict to cache
    hash_table = {}

    # loop if the key is present, get() the limit minus the weights at the i-th index
    for i in range(length):
        results = hash_table.get(limit - weights[i])
    
        if results != None:
            return i, results
        
        # set the hash_table at the weights at the i-th index...index equal to i
        hash_table[weights[i]] = i


    return None
