def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
  
    #get the array count
    arr_count = len(arrays)

    #set an open dict
    total = {}
    
    #find the total for the first list, at the 0th position
    for i in arrays[0]:
        #add all i to the total dict
        total[i] = 1

    #for every list after
    for next_arr in arrays[1:]:

        #find total occurences
        for new_item in next_arr:
            #if the new item is in the total dict
            if new_item in total:
                #increment total at the new_item-th index by 1
                total[new_item] += 1

        #iterate through the key and value in total dict and set it equal to result   
        result = [key for (key, val) in total.items() if val == arr_count]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
