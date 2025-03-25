#Part 1 (Getting general details from user)

def checkint(string):   
   while True:
      try:
          variable = int(input(string))
          return variable
      except:
          print("Please enter an integer!")

name = input("Please enter your name: ")

age = checkint("Enter your age: ") 

family_size = checkint("Enter the number of residents: ")

income = checkint("Enter your monthly income: ")

house_list = (
    'HDB',
    'Condominium',
    )

house_string = (
'''
Please select house of your choosing
{}
'''.format(house_list)
                )

def checklist(string,listing):
    while True: 
        choice = input(string)
        if choice not in listing:
            print("Please choose from selection!")
        else:
            return choice

house_type = checklist(house_string,house_list)

def checkintrange(string,minimum,maximum):   
   while True:
      try:
          variable = int(input(string))
          if variable in range(minimum,maximum+1):
              return variable
          else:
              print("Please enter a number from the given range!")
      except:
          print("Please enter a valid number!")
          


#part 2
attribute_dict={1:"Area of house",2:"Size of house",3:"Budget range",4:"TOP of house",5:"Number of bedrooms",6:"Number of bathrooms"}

print("Please specify the following house attributes in order of consideration.\nPlease write the number listed in the [] only.\nIf you are satisifed with your choices or wish to reselect your choices, enter any non-number character to continue.")
for j,k in attribute_dict.items():
    print("[{}] {}".format(j,k))

def house_attribute(): 
        ranking_list=[]
        ranking=["first","second","third","forth","fifth","sixth"]
        i=0
        while True:
            input1=input("Enter your {} choice: ".format(ranking[i]))

            if input1.isnumeric(): #checks if input is an integer
                input1=int(input1)
                
                if input1 in ranking_list: #checks if input has been entered
                    print("Please do not enter a repeating number.")
                elif input1 <= 6 and input1 >=1: #checks if input is in range of 1 to 6
                    ranking_list.append(input1)
                    i+=1
                    if len(ranking_list)==6:
                        print("Your choices in order are: ")
                        for k in ranking_list:
                            print(attribute_dict[k])
                        confirmation=input("Input N to reenter your choices, else press any key to continue: ")
                        if confirmation.upper() != "N" :
                            return ranking_list         
                        else:
                            ranking_list = []
                            i=0
                else:
                    print("Please insert a valid number!")
            else:
                print("Your choices in order are:")
                for k in ranking_list:
                    print(attribute_dict[k])
                confirmation=input("Input N to reenter your choices, else press any key to continue:")
                if confirmation.upper() != "N" :
                    return ranking_list
                else:
                    ranking_list = []
                    i = 0
                
# Part 3
def chooserange(string,listing):
    for i,j in enumerate(listing):  # first index (0) put empty string
        print(f"{i+1}. {j}")
    print("Please enter only the listing number.")
    while True:
        user = input(string)
        

        if user.isnumeric() == True and int(user) <=len(listing) and int(user) > 0:
            return user
        else:
            print("Plesae enter a valid selection!")

ranking_list = house_attribute()

area_list = ["North-East","North-West","South-East","South-West","Central"]
floorsize_list = [700,800,900,1000,1100,1200,1300]
budgetHDB_list = [400000,450000,500000,550000,600000,650000]
budgetcondo_list = [1500000,2000000,2500000]
for q in ranking_list:
    
    if q==1:
        area=chooserange("Enter desired area of property: ",area_list)
    elif q==2:
        floor_size=chooserange("Enter your preferred floor size: ",floorsize_list)
    elif q==3:
        if house_type=='HDB' :
            budget=chooserange("Choose a budget range: ",budgetHDB_list)
        elif house_type=='Condominium' :
            budget=chooserange("Choose a budget range: ",budgetcondo_list)
    elif q==4:
        TOP=checkintrange("Enter preferred year of TOP issued from 1979 to 2017: ",1979,2017)
    elif q==5:
        no_of_bedrooms = checkintrange("Enter your preference on the no. of bedrooms from 1 to 4: ",1,4) 
    elif q==6:
        no_of_bathrooms = checkintrange("Enter your preference on the no. of bathrooms from 1 to 2: ",1,2)

#Part 4
if ranking_list == []:
    ranking_list = [3,5]
    if family_size == 1:
        no_of_bedrooms = 1
    else:
        no_of_bedrooms = min(family_size - 1,4)
    
    if house_type == 'HDB':
        if income < 4000:
            budget = 1
        elif income > 6500:
            budget = 6
        else:
            budget = 3
    else:
        if income < 15000:
            budget = 1
        elif income > 25000:
            budget = 3
        else:
            budget = 2

#Part 5
def weighter(value):
    elements = len(ranking_list)
    weight = 2*(len(ranking_list)-ranking_list.index(value))/(elements+elements**2)
    return weight

no_of_property=7   
property_attribute_list=open("property-attributes.txt","r")       
property_list=open("property-listing.txt","r")
property_listing=[]
def prop_attribute():
    templist=[]
    for i in range(12):
        i=property_list.readline()
        i=i.lstrip("0 1 2 3 4 5 6 7 8 9 10")
        i=i.strip("\n :")
        templist.append(i)
    newtemplist=templist[1:-1]
    property_listing.append(newtemplist)
    
for j in range(no_of_property):
    prop_attribute()

def score(variable,list_index):
    score_list = []
    y=[]
    for i in property_listing:
        x = abs(int(variable)-int(property_listing[property_listing.index(i)][list_index]))
        y.append(int(property_listing[property_listing.index(i)][list_index]))
        score_list.append(x)

    for j in range(len(score_list)):
        score_list[j] = 1 - score_list[j]/max(y)
    return score_list

k = 0
for q in ranking_list:
    if q==1:
        score_area = [0,0,0,0,0,0,0]
        k=0
        for i in property_listing:
            if area_list[int(area)-1] == property_listing[property_listing.index(i)][2]:
                score_area[k] = 1
                k+=1
            else:
                score_area[k] = 0
                k+=1

                
    if q==2:
        score_floorsize = score(floorsize_list[int(floor_size)-1],5)
    
    if q==3:
        if house_type == 'HDB':
            score_budget = score(budgetHDB_list[int(budget)-1],9)
        elif house_type == 'Condominium':
            score_budget = score(budgetcondo_list[int(budget)-1],9)
    
    if q==4:
        score_TOP = score(TOP,6)
        
    if q==5:
        score_bedrooms = score(no_of_bedrooms,7)
    
    if q==6:
        score_bathrooms = score(no_of_bathrooms,8)

weight = []
for i in ranking_list:
    weight.append(weighter(i))
    if i == 1:
        score_area = [x*weight[ranking_list.index(i)] for x in score_area]
    elif i == 2:
        score_floorsize = [x*weight[ranking_list.index(i)] for x in score_floorsize]
    elif i == 3:
        score_budget = [x*weight[ranking_list.index(i)] for x in score_budget]
    elif i == 4:
        score_TOP = [x*weight[ranking_list.index(i)] for x in score_TOP]
    elif i == 5:
        score_bedrooms = [x*weight[ranking_list.index(i)] for x in score_bedrooms]
    elif i == 6:
        score_bathrooms = [x*weight[ranking_list.index(i)] for x in score_bathrooms]

if 1 not in ranking_list:
    score_area = [0]*7
if 2 not in ranking_list:
    score_floorsize = [0]*7
if 3 not in ranking_list:
    score_budget = [0]*7
if 4 not in ranking_list:
    score_TOP = [0]*7
if 5 not in ranking_list:
    score_bedrooms = [0]*7
if 6 not in ranking_list:
    score_bathrooms = [0]*7

final_score = []

for i in range(no_of_property):
    score_sum=score_area[i]+score_floorsize[i]+score_budget[i]+score_TOP[i]+score_bedrooms[i]+score_bathrooms[i]
    final_score.append(score_sum)

# Part 6
choosing_order=[]
for j in final_score:
    choosing_order.append(j)
choosing_order.sort(reverse=True)
attribute_name=["Address","Area","Town","Postal Code","Property Type","Floor size","TOP","Number of bedrooms","Number of bathrooms","Asking price"]
print(f"Dear {name}, the properties that best match your criteria are as follows:")
print("-"*50)
for i in choosing_order:
    
    final_index=(final_score.index(i))
    print("Property {}: ".format(final_index+1))
    for j in range(10):
        print("{:<20}: {}".format(attribute_name[j],property_listing[final_index][j]))
    print("-"*50)
