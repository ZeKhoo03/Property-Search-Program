# Property-Search-Program
The objective of this project is to optimize the user’s search for housing. 
The code will automatically sort the listing of available houses to match the user’s preference after getting the necessary details from them. It starts off by prompting the user for personal details such as household income and personnel.  After receiving the details, the code will then prompt the user more questions regarding their preferences for housing units. These details and the preferences will then be used to show the user a sorted list of houses, in order, of what units best suit the user’s preferences.
This program implements a property recommendation system that shows property results in accordance with the attributes and specifications that users prioritize. This allows users to filter through available properties with ease and find a selection of properties that best suit their needs. The program is useful for both sellers and buyers to obtain results of properties in the ranking of their preference.

Users will be prompted to input general details such as their name, age, number of residents, gross income, and housing choice. Functions are used to validate the input. These details will later be used by the program as a guide on the ranking of housing if user does not wish to rank the attributes. 

Users will be given the choice to rank the following attributes: area of the house, size of the house, budget range, TOP of the house, number of bedrooms, and number of bathrooms. Users are prompted to enter the numbers corresponding to their preferred house attributes in order of 1 to 6, with 1 being the most important and 6 being the least. Users do not have to enter all 6 numbers but rather only the ones they wish to factor in the ranking process (0 to 6). 

If the user doesn't input any preferences and leaves the ranking list empty, the system will set default values for the following attributes:

-	ranking_list: if list is empty, budget is most important attribute and number of bedrooms is the second most important attribute.
-	no_of_bedrooms: the value will depend on the family size, with a maximum value of 4.
-	budget: the value will depend on the house_type and the income of the user.

Then, the program will generate scores for each property based on the user’s preferred attributes. This program uses a weighted scoring system to rank the properties based on how well they match the user's preferences. The weight is calculated using a formula that gives higher weight to values that are higher in the list and lower weight to values that are lower in the list.

Once the weight is assigned, users will be asked to input specific details for each attribute. For example, for the area of the house attribute, users may be prompted to input their preferred location. Lastly, the results of the property will be displayed in order.
