import datetime

def ticket_generator():
    # Step 1: Read the current ticket number
    try:
        with open("ticketno.txt", "r") as file:
            content = file.read().strip()  # Read and strip whitespace/newline characters

        # Check if content is not empty to avoid ValueError
        if content: 
            current_ticket_no = int(content)  # Convert to int
            print("Ticket No: " + str(current_ticket_no) + "\n")
        else:
            print("No ticket number found. Starting from 1.")
            current_ticket_no = 1  # Start from 1 if the file is empty

    except FileNotFoundError:
        print("Ticket number file not found. Starting from 1.")
        current_ticket_no = 1

    # Step 2: Increment the ticket number
    ticket_no_increasor(current_ticket_no)

def ticket_no_increasor(current_ticket_no):
    # Step 3: Write the incremented ticket number back to the file
    with open("ticketno.txt", "w") as file:
        file.write(str(current_ticket_no + 1))  # Convert back to string for writing

# Print park information
print('''                           
                        VAN VIHAR

                Vanvihar National Park and 
                
                            Bhopal

                        VISITOR ENTRY 
                    
                        GATE: RAMU GATE''')

# Call the ticket generator
ticket_generator()

# Get and format current date and time
now = datetime.datetime.now()
formatted_date = now.strftime("%d/%b/%Y %H:%M:%S")
print("Date and Time:", formatted_date + "\n") 

# Take input for the number of visitors
try:
    no_of_visitors = int(input("No of Visitors? "))
    
    # Check if the number of visitors is a positive integer
    if no_of_visitors < 0:
        print("Number of visitors cannot be negative. Please enter a valid number.")
    else:
        print("No of visitors: " + str(no_of_visitors) + "\n")
        print("Amount: ₹" + str(no_of_visitors * 20) )
except ValueError:
    print("Please enter a valid integer for the number of visitors.")

# Print park rules
print(''' 
RIGHT OF ADMISSION IS RESERVED

THIS PERMIT IS VALID FOR 3 HRS ONLY

PERMIT VALIDITY IS SUBJECT TO PARK 

CLOSING TIME WHICHEVER IS EARLIER

1. PLEASE OBSERVE DO'S AND DONT'S OF THE NATIONAL
   PARK PROVIDED AT THE ENTRY GATES

2. ANYONE FOUND VIOLATING PARK RULES WILL BE FINED
''')
