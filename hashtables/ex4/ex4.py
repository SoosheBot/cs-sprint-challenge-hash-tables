def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    #set an open dict
    my_dict = {}

    #set an open list
    pos_nums = []

    # for all of the numbers in a
    for num in a:
        #add all of the numbers to my dictionary
        my_dict[num] = 1

        if num < 0 in my_dict:
            pos_nums.append(abs(num))


    return pos_nums


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
