import csv, os # Imported os for directory info
import sys
from datetime import datetime
from matplotlib import pyplot as plt
from tkinter import filedialog, Tk  # Import Tk for GUI file dialog

# Resource: Stack Overflow
# Adding a matplotlib legend: #https://stackoverflow.com/questions/19125722/adding-a-matplotlib-legend
# How to join paths nice way: https://stackoverflow.com/questions/60045721/how-to-join-paths-nice-way



# Welcome message and instructions
print("\nWelcome to the Sitka Weather Summary from 2018")
print("\nThis program will allow you to see a plotted graph of Temperatures")

# Menu Selection and Welcome Message
def menu_selection():
    print("\nNote: You will need to close the pop-up graph before you can choose to view another graph")
    print("1. View the High Temperature Plotted Graph")
    print("2. View the Low Temperature Plotted Graph")
    print("3. View both the High and Low Temperatures Plotted Graph") # Resource Stack Overflow
    print("4. Exit the Program\n")

# Function to choose a file. I used this years ago with a colleague on a project and wanted to use this option here
def get_file():
    Tk().withdraw()  # Hide the root window Tkinter opens
    filename = filedialog.askopenfilename(initialdir=os.getcwd())  # Show file dialog box to select a file
    return filename # returning the new file and path selected

# Moved this code to a function for loading the data from the CSV file. It now stores the low temp TMIN as list lows
def load_data(filename):
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            lows.append(int(row[6]))  # Low temperatures are in index 6 place which is the 7th column if opened in excel
            highs.append(high)
    return dates, highs, lows # added to return the values for lists dates=DATE, highs=TMAX and lows=TMIN

# Moved this code to a function to plot high temperature graph if option 1 from menu_selection is chosen
def high_temp_graph(dates, highs):
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot
    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Duplicated the High temp code to plot low temperature graph if option 2 from menu_selection is chosen
def low_temp_graph(dates, lows):
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue') # uses values from lows list and sets the color to blue

    # Format plot
    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Duplicated the High temp code to plot high/low temperature graph if option 3 from menu_selection is chosen
def high_and_low_temp_graph(dates, highs, lows): # uses the list values from dates, highs and lows
    fig, ax = plt.subplots()

    # Label added for the legend
    ax.plot(dates, highs, c='red', label='High Temps') # uses values from highs list and sets the color to red

    # Label added for the legend
    ax.plot(dates, lows, c='blue', label='Low Temps') # uses values from lows list and sets the color to blue

    # Format plot
    plt.title("Daily High and Low Temperatures - 2018", fontsize=18)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # The legend is added to this graph to show the ax.plot values of 'c' for line color and 'label' for the text
    plt.legend()

    # Show the plot
    plt.show()


# Main function to control the flow of the program
def main():
    # Default file path if the user doesn't choose to select a new file/location
    file = 'sitka_weather_2018_simple.csv'

    # Get the current working directory where the Python script is being executed
    current_directory = os.getcwd()
    full_path = os.path.join(current_directory, file) #

    # Print the default file the program will look for and the current directory the program is run from
    print(f"\nThe program will use the file: {file} located in this directory: {current_directory}")

    # Ask if the user wants to choose a new file
    while True:
        change_file = input("\nWould you like to choose a new file from a different directory? (Y/N): ")
        if change_file.upper() == "Y":
            new_file = get_file() # This will call the get_file function
            if new_file:  # If a file was chosen and the user didn't click Cancel or close the dialog box, else default
                file = new_file  # Update the file path to the new file selected
                print(f"\nUsing file from new location: {file}")  # Print the full path of the new file for the user to see
                break  # Exit the loop since the user selected a new file
        elif change_file.upper() == "N":
            print(f"\nWe will use the default location: {full_path}")
            break  # Exit the loop since the user chose the default file
        else:
            print("\nPlease enter a correct response: 'Y' for Yes or 'N' for No")

    while True:
        menu_selection()
        choice = input("Please choose an option (1/2/3/4): ")

        if choice == '1':
            # Load data and plot the high temperature graph
            dates, highs, lows = load_data(file)
            high_temp_graph(dates, highs)
        elif choice == '2':
            # Load data and plot the low temperature graph
            dates, highs, lows = load_data(file)
            low_temp_graph(dates, lows)
        elif choice == '3':
            # Load data and plot high and low temperature graph
            dates, highs, lows = load_data(file)
            high_and_low_temp_graph(dates, highs, lows)
        elif choice == '4':
            print("\nExiting the program. Have a nice day!")
            sys.exit()
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
