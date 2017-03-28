import random

random_list = []

# Function to display help options
def show_help():
    print("Welcome to the random item selector")
    print("Enter items and then a random item will be selected")
    print("Enter DONE to finish")
    print("Enter HELP to display commands")

def get_random_item():
  upper_bound = len(random_list)
  random_index = random.randint(0, upper_bound)
  random_sel_item = random_list[random_index]
  
  print("The random selection is: {}".format(random_sel_item))
    
# Main function
def main():
    show_help()

    while True:
        input_item = input("Enter item > ")

        if input_item.upper() == 'DONE':
            print(get_random_item())
            break
        elif input_item.upper() == 'HELP':
            show_help()
        else:
            random_list.append(input_item)
            print("Added {} to the list.".format(input_item))
            
main()
