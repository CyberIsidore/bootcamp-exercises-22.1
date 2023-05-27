def convert_temp(unit, temp):
    while True:
        if unit == "c":
            result = (temp * 1.8) + 32
        else:
            result = (temp - 32) * .55555
        return result


temp = int(input("Please enter the temperature: "))
unit = input("Are you measuring in (C)elsius or (F)ahrenheit? ").lower()
if unit == "c" or unit == "f":
    print(f"The converted temperature is {convert_temp(unit, temp)}.")
else:
    print("Please type 'C' or 'F'.")



# print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
# print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
# print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
# print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
# print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

# """Convert fahrenheit <-> celsius and return results.
#
# - unit_in: either "f" or "c"
# - unit_out: either "f" or "c"
# - temp: temperature (in f or c, depending on unit_in)
#
# Return results of conversion, if any.
#
# If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".
#
# For example:
#
#   convert_temp("c", "f", 0)  =>  32.0
#   convert_temp("f", "c", 212) => 100.0
# """
