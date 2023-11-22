for i in range(100):
    if i < 10:
        print("{:02}".format(i), end=", ")
    elif str(i)[0] != str(i)[1] and int(str(i)[0]) < int(str(i)[1]):
        if i != 89:
            print("{}".format(i), end=", ")
        else:
            print("{}".format(i), end=", ")
