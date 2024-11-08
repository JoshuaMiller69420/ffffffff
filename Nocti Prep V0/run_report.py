"""
WITHOUT THE USE OF AI
 
1. Load the data
2. Loop through the list of customers
    -For each customer:
        print their name
        print a report header
        -for each product ordered
            print Item Purchased, Selling Price,
            Unit Cost, Profit per Unit, Quantity,
            Total Item Profit, Total Item Price
        -after printing all product orders for a customer
            print subtotal, tax, shipping, and order total
 
3. After all customer were processed print:
    -Total items sold on the day
    -Total profit processed
"""
import json
class bcolors:
    ENDC = '\033[0m'
    WARNING = '\033[93m'                                                    


def print_report_line(product, price, cost, qty):
    print(f"|{product.ljust(25)} | {price.ljust(8)} | {cost.ljust(18)} | {qty.ljust(8)} |")


def process_orders(data):
    #loop through the data and print customer name
    for cust in data:
        print(f"{bcolors.WARNING}{cust["cust_name"]}{bcolors.ENDC}")
        print(f"/---------------------------------------------------------------------\\")
        print_report_line("Product","Price", "Cost To Produce", "Quantity")
        print("|---------------------------------------------------------------------|")
        print_report_line(cust["orders"][0]["product"], str(cust["orders"][0]["selling_price"]), str(cust["orders"][0]["cost_to_produce"]), str(cust["orders"][0]["qty"]))
        print("|---------------------------------------------------------------------|")
        print_report_line(cust["orders"][1]["product"], str(cust["orders"][1]["selling_price"]), str(cust["orders"][1]["cost_to_produce"]), str(cust["orders"][1]["qty"]))
        print("\\-------------------------------------------------------------------/")
        print("")

def load_data():
    with open("orders.json", "r") as file:
        data = json.load(file)
        return data

def main():
    data = load_data()
    process_orders(data)

if __name__ == "__main__":
    main()