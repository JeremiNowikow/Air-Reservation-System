def my_max(*args):
    temp_max = args[0]
    for i in args:
        if i > temp_max:
            temp_max = i
    return temp_max


print(my_max(1,3,6,33,4,5))