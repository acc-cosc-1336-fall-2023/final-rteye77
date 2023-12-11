#write functions here, don't add input('') statements here!
def create_multiplication_table():
    table = []
    one = 1
    six = 6
    eleven=11
    for i in range(one, six):
        row = []
        for j in range(one, eleven):
            row.append(i * j)
        table.append(row)
    return table


def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(f"{value:4}", end=" ")
        print()