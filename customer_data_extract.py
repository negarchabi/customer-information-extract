output = []
try:
    with open('customers_info.txt', 'r') as file:
        lines = file.readlines()

    #  first line is a short introduction on the information within the .txt file
    for line in lines[1:]:
        customer_info = {}
        items_dict = {}
        order_number, customer_name, item1, item2, item3 = line.strip().split(',')
        customer_info["order_number"] = int(order_number)
        customer_info["customer_name"] = customer_name
        items_dict["item1"] = int(item1)
        items_dict["item2"] = int(item2)
        items_dict["item3"] = int(item3)
        customer_info["items"] = items_dict
        output.append(customer_info)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

print(output)


