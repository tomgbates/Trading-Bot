import random
import pandas as pd

def choice_years():
    f = open('.\Historic_Data_txt\Details.txt', 'a')
    f.write(f'You chose to run for: {range_years} Year(s)\n')
    f.write(f'You will generate data for: {str(iteration_total)} iterations\n')
    f.close()
    print(f'You will generate {str(iteration_total)} entries of data.')
def choice_months():
    f = open('.\Historic_Data_txt\Details.txt', 'a')
    f.write(f'You chose to run for: {range_months} Month(s)\n')
    f.write(f'You will generate data for: {str(iteration_total)} iterations\n')
    f.close()
    print(f'You will generate {str(iteration_total)} entries of data.')
def choice_days():
    f = open('.\Historic_Data_txt\Details.txt', 'a')
    f.write(f'You chose to run for: {range_days} Day(s)\n')
    f.write(f'You will generate data for: {str(iteration_total)} iterations\n')
    f.close()
    print(f'You will generate {str(iteration_total)} entries of data.')
def choice_hours():
    f = open('.\Historic_Data_txt\Details.txt', 'a')
    f.write(f'You chose to run for: {range_hours} Hour(s)\n')
    f.write(f'You will generate data for: {str(iteration_total)} iterations\n')
    f.close()
    print(f'You will generate {str(iteration_total)} entries of data.')

FILE_INPUT = input('Please choose the name of the .txt file you want to write to:\n')
FILE_NUMBER = int(input('\nHow many files do you want to generate?:\n'))
f = open('.\Historic_Data_txt\Details.txt', 'w')
f.write(f'You chose to generate {str(FILE_NUMBER)} file(s)\n')
f.close()

iteration = input('\nEvery how many minutes do you want data?:\n')
f = open('.\Historic_Data_txt\Details.txt', 'a')
f.write(f'You chose to generate data every: {iteration} minute(s)\n')
f.close()

if iteration.isdigit():
    time_duration = input('\nDo you want to run it for Years, Months, Days, or Hours?:\n1. Years\n2. Months\n3. Days\n4. Hours\n')
    if time_duration == '1' or time_duration == 'Years' or time_duration == '1. Years' or time_duration == 'Y' or time_duration == 'years' or time_duration == '1. years' or time_duration == 'y':
        print('\nYou chose Years') 
        range_years = input('How many Years? Please input an integer:\n')
        iteration_total = int((int(range_years) * 525600)/int(iteration))
        choice_years()
    elif time_duration == '2' or time_duration == 'Months' or time_duration == '2. Months' or time_duration == 'M' or time_duration == 'months' or time_duration == '2. months' or time_duration == 'm':
        print('\nYou chose Months')
        range_months = input('How many Months? Please input an integer (Note: The average number of days for a month will be taken as 30):\n')
        iteration_total = int((int(range_months) * 43200)/int(iteration))
        choice_months()
    elif time_duration == '3' or time_duration == 'Days' or time_duration == '3. Days' or time_duration == 'D' or time_duration == 'days' or time_duration == '3. days' or time_duration == 'd':
        print('\nYou chose Days')
        range_days = input('How many Days? Please input an integer:\n')
        iteration_total = int((int(range_days) * 1440)/int(iteration))
        choice_days()
    elif time_duration == '4' or time_duration == 'Hours' or time_duration == '4. Hours' or time_duration == 'H' or time_duration == 'hours' or time_duration == '4. hours' or time_duration == 'h':
        print('\nYou chose Hours')
        range_hours = input('How many Hours? Please input an integer:\n')
        iteration_total = int((int(range_hours) * 60)/int(iteration))
        choice_hours()
    else:
        print('Your choice is invalid, goodbye')
        exit()
else:
    print('Your input was incorrect, goodbye')
    exit()

starting_price = float(input('\nWhat is your starting price?:\n'))
new_price = float('%.2f' % starting_price)
print('Your starting price is ' + 'R%.2f' % starting_price)
f = open('.\Historic_Data_txt\Details.txt', 'a')
f.write('Your starting price is: ' + 'R%.2f' % starting_price + '\n' + '\n')
f.close()

i = 1
j = 1
while j <= FILE_NUMBER:
    NAME_WITHOUT_EXTENSION = FILE_INPUT + '_' + str(j)
    TXT_FILE_WRITE = FILE_INPUT + '_' + str(j) + '.txt'
    print(TXT_FILE_WRITE)
    i = 1
    j += 1
    new_price = float('%.2f' % starting_price)
    while i <= iteration_total:
        up_or_down = ['up', 'down']
        up_or_down_decision = random.choice(up_or_down)
        if up_or_down_decision == 'up':
            change = [0.001, 0.002, 0.00005, 0.01, 0.003]
            change_decision = random.choice(change)
            added_price = new_price * change_decision
            new_price = new_price + added_price
            formatted_new_price = float('%.2f' % new_price)
            f = open('.\Historic_Data_txt\\' + TXT_FILE_WRITE, 'a')
            f.write(f'{str(i)} {str(formatted_new_price)} \n')
            f.close()
            i += 1
        elif up_or_down_decision == 'down':
            change = [0.001, 0.002, 0.00005, 0.01, 0.003]
            change_decision = random.choice(change)
            subtracted_price = new_price * change_decision
            new_price = new_price - subtracted_price
            formatted_new_price = float('%.2f' % new_price)
            f = open('.\Historic_Data_txt\\' + TXT_FILE_WRITE, 'a')
            f.write(f'{str(i)} {str(formatted_new_price)} \n')
            f.close()
            i += 1
    read_file = pd.read_csv (r'.\Historic_Data_txt\\' + NAME_WITHOUT_EXTENSION + '.txt')
    read_file.to_csv (r'.\Historic_Data_csv\\' + NAME_WITHOUT_EXTENSION + '.csv', index=None)