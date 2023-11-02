def calculate_expenditure(list_of_expenditure):
    total = 0
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print(total)
    except TypeError:
        print("The type is wrong")
    except ZeroDivisionError:
        print("The value been divided by zero")
    except:
        print("Some error occurred")
    print("Returning back from function.")


list_of_values = [100, 200, 300, "A", 500]
calculate_expenditure(list_of_values)
