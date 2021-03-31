randomNumer = 1


def format_position(lat, long):
    pattern = "Lat{} - Long {}"
    formatPosition = "Lat{} - Long {}".format(lat, long)
    print(pattern)
    global randomNumer
    randomNumer = 4
    return formatPosition


def calculate_sum(number1, numberTwo):
    numeroThree = number1 + numberTwo + randomNumer
    print
    return numeroThree


print(calculate_sum(1, 2))

print(format_position(1233, 123.88888888888888888124124))
