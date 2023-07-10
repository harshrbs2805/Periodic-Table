import pandas as pd
import os.path as path
from termcolor import colored
import colorama
colorama.init()

print(colored('\t\t\tModern Periodic Table', 'blue'))
print(colored('\t\t\t\t   Digital', 'green'))
print('\t\t\t\t   _______\n\n\n\n')

def displayInfo(info):
    print('Name: ', colored(info.iloc[0].Name, 'green'))
    print('Symbol: ', colored(info.iloc[0].Symbol, 'green'))
    print('Atomic Number: ', colored(info.iloc[0]['Atomic Number'], 'green'))
    print('Atomic Weight: ', colored(info.iloc[0]['Atomic Weight'], 'green'))
    print()

######  open file if already exist
column_names = ['Atomic Number', 'Symbol', 'Atomic Weight', 'Name']
if path.isfile('./table.csv'):
    df = pd.read_csv('./table.csv')
else:
    df = pd.DataFrame(columns = column_names)
######
while(True):
    print(colored('Please select what you wanna do:\n','yellow'))
    print(colored('1. Add new Element Information\n','green'))
    print(colored('2. Explore\n','green'))
    print(colored('3. Quit\n','green'))

    choice = int(input('Enter your choice: '))
    if (choice==1):
        # Get element data from user, store into the dataframe and update the csv file

        ## Getting data
        atomicNumber = int(input('Enter Atomic Number of the element'))
        atomicWeight = float(input('Enter Atomic Weight of the element'))
        name = input('Enter Name of the element')
        symbol = input('Enter symbolic name of the element')

        ## Storing into dataframe
        mod_df = df.append({'Name': name, 'Symbol': symbol, 'Atomic Number': atomicNumber, 'Atomic Weight': atomicWeight}, ignore_index=True)
        ## dataframe to file
        mod_df.to_csv('./table.csv', index=False)
        df = pd.read_csv('./table.csv')
    elif (choice==2):
        print(colored('Please enter your search criteria','green'))
        print(colored('1. Search by NAME','blue'))
        print(colored('2. Search by ATOMIC NUMBER','blue'))
        print(colored('3. Search by ATOMIC WEIGHT','blue'))
        print(colored('4. Search by SYMBOLIC NAME','blue'))

        search_choice = int(input('Enter the choice: '))
        if (search_choice == 1):
            name = input('Enter the name of element: ')
            info = df.loc[df['Name'] == name]
            if (info.shape[0] > 0):
                displayInfo(info)
            else:
                print(colored('No Data found!!\n', 'red'))
        elif (search_choice == 2):
            atnu = int(input('Enter the atomic number of element: '))
            info = df.loc[df['Atomic Number'] == atnu]
            if (info.shape[0] > 0):
                displayInfo(info)
            else:
                print(colored('No Data found!!\n', 'red'))
        elif (search_choice == 3):
            atwt = float(input('Enter the atomic weight of element: '))
            info = df.loc[df['Atomic Weight'] == atwt]
            if (info.shape[0] > 0):
                displayInfo(info)
            else:
                print(colored('No Data found!!\n', 'red'))
        elif(search_choice == 4):
            symbol = input('Enter the symbolic name of element: ')
            info = df.loc[df['Symbol'] == symbol]
            if (info.shape[0] > 0):
                displayInfo(info)
            else:
                print(colored('No Data found!!\n', 'red'))
        else:
            print('your choice is wrong')
            continue
    elif (choice==3):
        print('Thanks for using our application, bye!')
        break
    else:
        print(colored('Your choice is wrong!!','red'))
        continue

