#import datetime 
import datetime
#import csv to store data into excel later
import csv

#list for location
location = [ ]

#list to store coverage for each region 
central_coverage = []
north_coverage = []
northeast_coverage = []
east_coverage = []
west_coverage = []

#list to store bitrates for each region
central_bits = []
north_bits = []
northeast_bits = []
east_bits = []
west_bits = []



#to get the locale date time based on user's system
now = datetime.datetime.now()


#set up a menu
def print_menu():
    print(20* '==')
    print('Enter 1 start the program')   
    print('Enter -1 to quit the program')

#validation check to allow letters A-Z only for name
while True:
    name = input('Enter your name:')
    if not name.replace(' ' ,'').isalpha():
        print('Please enter letters A-Z only!')
        continue
    else:
        print('')
        #print a welcome message for the user
        print('Welcome to the program',name)
        break
    
print_menu()

#validation for user's menu choices, only allowing an integer value
while True:
    try:
        number = int(input('Enter your choice:'))
    except ValueError:
         #if user did not enter an integer, this error message will come out
        print('Sorry, I didn\'t understand that.')
        continue
    else:
        break
        
#loop
while number != -1:
    if number == 1:
        print(20* '==')         
  #validation check for integer value only
        while True:
            try:
                data = int(input('How many data to enter? >>'))
            except ValueError:
                print('Sorry, I didn\'t understand that.')
                continue
            #this will stop user from entering 0 or negetive value for number of data
            if data <1:
                print('You cannot have negative or zero data to enter, please enter again.')
                continue
            else:
                break
            
        
        #loop for each data
        i = 0
        while i < data:
            i +=1
            print('---Data' , i)
            
            #validation check for region, allowing letters only
            while True:
                region = input('Enter the region>>')
                if not region.replace(' ', '').isalpha():
                    print('Please enter letters A-Z only!')
                    continue
                else:
                    #replace spaces , if user accidentally entered one
                    region2 = region.replace(' ' , '')
                    #change input to lowercase, incase user entered in upper case
                    final_region = region2.lower()
                    #check with user, only allowing these region
                    if final_region != 'west' and final_region != 'east' and \
                       final_region != 'central' and final_region != 'north' \
                       and final_region != 'northeast':
                        
                        #if user enter a region that does not match the above, then this error message gets printed
                        #and it will loop until user enters an above region
                        print('Please enter a correct region')
                        continue 
                    else:
                        break
                    break
                
            #insert this region into the location list  
            location.append(final_region)
                
                    
            
            while True:
                coverage = input('Enter the coverage>>>')
                coverage2 = coverage.replace(' ' , '')
                final_coverage = coverage2.lower()
                
                #condition check for yes coverage
                #if coverage is yes, then user get to enter bitrates, if not, move on
                if final_coverage == 'yes':
                    #validation check, to make sure user enter a positive value
                    while True:
                        try:
                            bitrates = float(input('Bitrates (mbps):'))
                        except ValueError:
                            #when value entered is not a number, this error message prints out
                            print('Sorry, I didn\'t understand that.')
                            continue
                        #condition checking to make sure the number is not smaller than 1
                        if bitrates <1:
                            print('Bitrates cannot be 0 or negative!')
                            continue
                        else:
                            break
                
                #condition check to only accept yes or no input for coverage        
                elif final_coverage != 'yes' and final_coverage != 'no' :
                    print('Please enter Yes or No only!')
                    continue
                elif final_coverage == 'no':
                    break
                break
            
                
                                       
                
            #insert the corresponding coverage input to its corresponding region    
            if final_region == 'west':
                west_coverage.append(final_coverage)

            elif final_region == 'central':
                central_coverage.append(final_coverage)

            elif final_region == 'north':
                north_coverage.append(final_coverage)
                
            elif final_region == 'northeast':
                northeast_coverage.append(final_coverage)
     
            else:
                east_coverage.append(final_coverage)

             #insert the corresponding bitrates to its corresponding region
             #only insert bitrate if the coverage is yes
            if final_region == 'west' and final_coverage == 'yes':
                west_bits.append(bitrates)
            elif final_region == 'central' and final_coverage == 'yes':
                central_bits.append(bitrates) 
            elif final_region == 'north' and final_coverage =='yes':
                north_bits.append(bitrates)
            elif final_region =='northeast' and final_coverage =='yes':
                northeast_bits.append(bitrates)
            elif final_region == 'east' and final_coverage =='yes':
                east_bits.append(bitrates)
            

            
                

        #count the amount of regions inserted in the location list
        #count by region names to get number of regions for its corresponding region
        
        central_count = location.count('central')
        west_count = location.count('west')
        north_count = location.count('north')
        north_east_count = location.count('northeast')
        east_count = location.count('east')
        
        #get the number of data entered for each region's coverage
        centralTotalCoverage = len(central_coverage)
        #get the number of "yes" entered for coverage
        yesCentral = central_coverage.count('yes')
        
        westTotalCoverage = len(west_coverage)
        yesWest = west_coverage.count('yes')
        
        northTotalCoverage = len(north_coverage)
        yesNorth = north_coverage.count('yes')
        
        northeastTotalCoverage = len(northeast_coverage)
        yesNortheast = northeast_coverage.count('yes')
        
        eastTotalCoverage = len(east_coverage)
        yesEast = east_coverage.count('yes')
        
        #compute the bitrates total
        sumCentralBits = sum(central_bits)
        sumWestBits = sum(west_bits)
        sumNorthBits = sum(north_bits)
        sumNortheastBits = sum(northeast_bits)
        sumEastBits = sum(east_bits)
        
        #count the number of bitrates for each region
        centralBitsCount = len(central_bits)
        westBitsCount = len(west_bits)
        northBitsCount = len(north_bits)
        northeastBitsCount = len(northeast_bits)
        eastBitsCount = len(east_bits)
                                
        
        #compute the coverage percentage
        try:
            #if there is data to calculate, this will compute the outcome
            finalCentral = 100 / centralTotalCoverage * yesCentral
            #round up to 2 decimal with the % sign
            finalCentral = '{0:.2f}%'.format(finalCentral)
        #if no data to calculate, this will be the outcome
        except ZeroDivisionError:
            finalCentral = 'No Data'

            
        try:
            finalWest = 100 / westTotalCoverage * yesWest
            finalWest = '{0:.2f}%'.format(finalWest)
        except ZeroDivisionError:
            finalWest = 'No Data'

                
        try:
            finalNorth = 100 / northTotalCoverage * yesNorth
            finalNorth = '{0:.2f}%'.format(finalNorth)
        except ZeroDivisionError:
            finalNorth = 'No Data'

            
        try:
            finalNortheast = 100 / northeastTotalCoverage * yesNortheast
            finalNortheast ='{0:.2f}%'.format(finalNortheast)
        except ZeroDivisionError:
            finalNortheast = 'No Data'

            
        try:
            finalEast = 100 / eastTotalCoverage * yesEast
            finalEast ='{0:.2f}%'.format(finalEast)
        except ZeroDivisionError:
            finalEast = 'No Data'  

        

        #compute the average bitrates for each region
        try:
            #if there is data to calculate, this will compute the outcome
            finalCentralBits = sumCentralBits / centralBitsCount
            #round up the computed outcome to 2 decimal
            finalCentralBits ='{0:.2f} mbps'.format(finalCentralBits)
        except ZeroDivisionError:
            #if no data to compute, this will be the outcome
            finalCentralBits = 'No Data'
      
        
        try:
            finalWestBits = sumWestBits / westBitsCount
            finalWestBits = '{0:.2f} mbps'.format(finalWestBits)
        except ZeroDivisionError:
            finalWestBits = 'No Data'

                
        try:
            finalNorthBits = sumNorthBits / northBitsCount
            finalNorthBits = '{0:.2f} mbps'.format(finalNorthBits)
        except ZeroDivisionError:
            finalNorthBits = 'No Data'

            
        try:
            finalNortheastBits = sumNortheastBits / northeastBitsCount
            finalNortheastBits = '{0:.2f} mbps'.format(finalNortheastBits)
        except ZeroDivisionError:
            finalNortheastBits = 'No Data'
            
        try:
            finalEastBits = sumEastBits / eastBitsCount
            finalEastBits = '{0:.2f} mbps'.format(finalEastBits)
        except ZeroDivisionError:
            finalEastBits = 'No Data'     
        
        #summarize all the data    
        print(15*'==','Summary',15*'==')
        print('Data Collected \t\t Network Coverage \t Average Download Bitrates')
        print('>>Central:','{:<13} {:<23}'.format(central_count, finalCentral),finalCentralBits)
        print('>>West:','{:<16} {:<23}'.format(west_count, finalWest),finalWestBits)
        print('>>North:','{:<15} {:<23}'.format(north_count,finalNorth),finalNorthBits)
        print('>>North-East:','{:<10} {:<23}'.format(north_east_count,finalNortheast),finalNortheastBits)
        print('>>East:','{:<16} {:<23}'.format(east_count,finalEast),finalEastBits)

        print(23* '===')
        
        #print who the data is collected from
        print('Data collected by >>', name)
        #show user the current date and time
        print('Collected on',now.strftime('%Y-%m-%d %H:%M:%S'))
        print('')
        
                 
        
        #validation check for user to enter letters only
        while True:
            end = input('Do you want to end the program?>>>')
            end2 = end.replace(' ', '')
            end3 = end2.lower()
            #condition check to only allow yes or no input
            if end3 != 'yes' and end3 != 'no':
                print('Please enter Yes or No only!')
                continue
            else:
                break
            break
        
        #condition check if user want to continue or no
        #if yes, then the program go back to the loop
        if end3 =='no':
            continue
        else:
            #Create a new csv folder called 'data'
            #Or write to existing csv folder, if it is already created
            f = open('data.csv', 'a', newline = '')
            
            #format all the lines to print first
            line1 = (' ')
            line2 = ('Data Collected',' ',' ','Network Coverage', ' ', 'Average Download Bitrates')
            line3 = ('Central',central_count,'', finalCentral,' ',finalCentralBits)
            line4 = ('West',west_count,' ',finalWest,' ',finalWestBits)
            line5 = ('North',north_count,' ',finalNorth,' ',finalNorthBits)
            line6 = ('North-East',north_east_count,' ',finalNortheast,' ',finalNortheastBits)
            line7 = ('East',east_count,' ',finalEast,' ',finalEastBits)
            line8 = ('Data collected by', name)
            line9 = ('Collected on',now.strftime('%Y-%m-%d %H:%M:%S'))
            line10 = (' ')
            
            #write all the lines into csv 
            
            write = csv.writer(f)
            write.writerow(line1)
            write.writerow(line2)
            write.writerow(line3)
            write.writerow(line4)
            write.writerow(line5)
            write.writerow(line6)
            write.writerow(line7)
            write.writerow(line8)
            write.writerow(line9)
            write.writerow(line10)
            
            #close the file
            f.close()             
            break
        
        
       
        break     
    
#condition check for wrong choices input by user from the menu options
    else:
        print('Invalid option.')
    #call back the menu again
    print_menu()
    
    #prompt user to re-enter a choice after wrong choices input by user
    #validation check again, for only integer value
    while True:
        try:
            number = int(input('Enter your choice:'))
        except ValueError:
            print('Sorry, I didn\'t understand that.')
            continue
        else:
            break
        
print('')
print('Goodbye and have a nice day!')


