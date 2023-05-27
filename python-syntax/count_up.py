#  """Print all numbers from start up to and including stop.
#
#  For example:
#
#      count_up(5, 7)
#
# should print:
#
#      5
#      6
#      7
#  """
# start = input("Please enter a starting number: ")
# stop = input("Please enter a stopping number: ")\

def count_up(start, stop):
    num = start
    while start <= num <= stop:
        print(num)
        num += 1
    return

start = int(input("Starting Number: "))
stop = int(input("Stopping Number: "))
print(f"Let's Count: {count_up(start, stop)}")
