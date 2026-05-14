# Daily Study Planner - Version 2
# A simple program to plan your study schedule
# New features: Functions, background colors, breaks calculation, and saving to a file!

# This is an ANSI escape sequence to add a blue background and white text.
# It makes our terminal look cool!
BG_BLUE = "\033[44;37m"
RESET_COLOR = "\033[0m" # This resets the color back to normal

def display_header():
    """Prints the welcome banner with a blue background."""
    print(BG_BLUE + "======================================" + RESET_COLOR)
    print(BG_BLUE + "         DAILY STUDY PLANNER          " + RESET_COLOR)
    print(BG_BLUE + "======================================" + RESET_COLOR)
    print()

def get_study_data():
    """Asks the user for subjects and hours, then returns the lists."""
    num_subjects_str = input("How many subjects do you want to study today? ")
    num_subjects = int(num_subjects_str)

    subjects = []
    study_hours = []

    for i in range(num_subjects):
        print("\n--- Subject " + str(i + 1) + " ---")
        subject_name = input("Enter subject name: ")
        
        hours_str = input("Enter study hours for " + subject_name + ": ")
        hours = float(hours_str)
        
        subjects.append(subject_name)
        study_hours.append(hours)
        
    # Functions can 'return' data back to the main program
    return subjects, study_hours

def calculate_breaks(total_hours):
    """Calculates how much break time is recommended (10 mins per hour)."""
    # 10 minutes of break for every 1 hour of study
    total_break_minutes = total_hours * 10
    print("💡 Tip: You should take a total of " + str(total_break_minutes) + " minutes of breaks.")

def display_and_save_schedule(subjects, study_hours):
    """Prints the schedule to the screen AND saves it to a text file."""
    print("\n======================================")
    print("             YOUR SCHEDULE")
    print("======================================")

    total_hours = 0
    
    # We will also create a string to hold our schedule text to save it
    schedule_text = "--- MY STUDY SCHEDULE ---\n"

    # len(subjects) gets the number of items in the list
    for i in range(len(subjects)):
        line = subjects[i] + " - " + str(study_hours[i]) + " hours"
        print(line)
        schedule_text = schedule_text + line + "\n"
        total_hours = total_hours + study_hours[i]

    summary_line = "--------------------------------------\nTotal study hours: " + str(total_hours) + " hours\n--------------------------------------"
    print(summary_line)
    schedule_text = schedule_text + summary_line
    
    # Save to a file (new feature!)
    # 'w' means we are writing to the file
    with open("my_schedule.txt", "w") as file:
        file.write(schedule_text)
    print("\n💾 Your schedule has been saved to 'my_schedule.txt'!")

    return total_hours

def print_motivation(total_hours):
    """Prints a motivational message."""
    print()
    if total_hours == 0:
        print("Message: Everyone needs a break! Enjoy your rest day.")
    elif total_hours <= 2:
        print("Message: A solid start! Every little bit helps. Keep it up!")
    elif total_hours <= 5:
        print("Message: Great plan! You are going to accomplish a lot today.")
    else:
        print("Message: Wow, that's a lot of studying! Remember to take short breaks to keep your mind fresh.")

# This is the main part of our program
def main():
    # 1. Show the header
    display_header()
    
    # 2. Get the data
    subjects_list, hours_list = get_study_data()
    
    # 3. Display the schedule and calculate total hours
    total = display_and_save_schedule(subjects_list, hours_list)
    
    # 4. Suggest break times
    print()
    calculate_breaks(total)
    
    # 5. Show motivation
    print_motivation(total)
    
    print("\nGood luck with your studies!")

# This line checks if we are running this specific file
if __name__ == "__main__":
    main()
