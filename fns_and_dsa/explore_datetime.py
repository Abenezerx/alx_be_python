from datetime import datetime, timedelta
#part 1
def display_current_datetime ():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S") 
    print(f"Current date and time: {formatted_date}")

#part 2
def calculate_future_date(days_to_add):
    current_date = datetime.datetime.now() 
    future_date = current_date + datetime.timedelta(days=days_to_add) 
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date
def main():
    display_current_datetime() 
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(days_to_add) 
    print(f"Future date: {future_date}")

    if __name__ == "__main__":
        main()