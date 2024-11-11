
def chunk_data(data,chunk_size):
    counter = 0
    counter_chunksize = chunk_size
    result = ()
    while counter < len(data):
        mytuple = ()
        while counter < counter_chunksize:
            mytuple += (data[counter], )
            counter+=1
        if counter_chunksize+chunk_size > len(data):
            counter_chunksize = len(data)
        else:
            counter_chunksize = counter_chunksize + chunk_size
        result += ( mytuple,)
    return result


def main():
    data = [1,2,3,4,5,6,7,8]
    for i in chunk_data(data, 3):
        print(i)
    print()
    for i in chunk_data(data, 5):
        print(i)
    print()
    for i in chunk_data(data, 2):
        print(i)

main()