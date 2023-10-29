"""
File: weather_master.py
Name: Rebecca
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This constant controls when to stop
EXIT = -100  # Sentinel Value


def main():
	"""
	This weather forecast program allows users to input multiple temperatures,
	and it calculates and displays the following:
	1. The highest temperature
	2. The lowest temperature
	3. The average temperature
	4. The total number of cold days (temperatures below 16 degrees)
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if data == EXIT:  # Check if user's first input is the EXIT constant.
		print('No temperatures were entered.')
	else:
		#  If the first input is a valid temperature, initialize the variables with this temperature.
		maximum = data
		minimum = data
		sum_of_data = data
		count_of_data = 1
		if data < 16:
			count_cold_days = 1
		else:
			count_cold_days = 0
		#  Enter a loop to continuously prompt the user for new temperatures.
		while True:
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data == EXIT:  # If the input is the EXIT constant, break the loop.
				break
			sum_of_data = sum_of_data + data
			count_of_data += 1
			if data < 16:  # Increment count of cold days if temperature is below 16.
				count_cold_days += 1
			if maximum < data:
				maximum = data  # Update the maximum temperature.
			if minimum > data:  # Update the minimum temperature.
				minimum = data
		# Print the result.
		print('Highest temperature: ' + str(maximum))
		print('Lowest temperature: ' + str(minimum))
		print('Average = ' + str(sum_of_data / count_of_data))
		print(str(count_cold_days) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
