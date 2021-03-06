import statistics


def main():
    print("ET07035 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()  # prompts user to enter value
    num_list = get_user_input()  # gets input values as a string which is converted into a list (type float)
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)
    calc_median_temperature(num_list) # sorts values in ascending value and finds median value


def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5,2,6,7)")


def get_user_input():
    user_str = input()  # creates a string (array) in the form of ['33','44','11','10','3']
    str_list = user_str.split(",")  # converts the string into a list in the form of [33,44,11,10,3]
    # print(str_list)
    float_list = []
    for number in str_list:
        float_list.append(float(number))

    print("The entered values are", float_list)

    return float_list


def calc_average_temperature(num_list):
    average = sum(num_list) / len(num_list)
    print("Average value is", average)
    return average


def calc_min_max_temperature(num_list):
    temp_list = [min(num_list), max(num_list)]
    print("Minimum and maximum values are", temp_list, "respectively")
    return


def calc_median_temperature(num_list):
    num_list.sort()
    print("List of values in ascending order:", num_list)
    median = statistics.median(num_list)
    print("The median value is", median)


if __name__ == "__main__":
    main()
