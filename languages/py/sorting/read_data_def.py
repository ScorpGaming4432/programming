def read_data():
    with open('data.txt') as file:
        return list(map(int, file.readline().split(', ')))