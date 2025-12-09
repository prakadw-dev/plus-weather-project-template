# from weather import format_temperature
# output = format_temperature(70)
# print(output)

# from weather import convert_date
# iso_date = '2025-12-07'
# print (convert_date(iso_date))

# from weather import convert_f_to_c
# output = convert_f_to_c(365)
# print(output)

# from weather import calculate_mean
# data = [1, 2, 3, 4]
# mean = calculate_mean(data)
# print(f"The mean weather value is: {mean}")

# from weather import load_data_from_csv
# # csv_file = "tests/data/example_one.csv"
# print(load_data_from_csv)

from weather import find_min
temperatures = [25, 22, 28, 20, 24, 20, 26]
min_temp, min_index = find_min(temperatures)

print(f"Data: {temperatures}")
print(f"Minimum Value: {min_temp}")
print(f"Last Position (Index): {min_index}")