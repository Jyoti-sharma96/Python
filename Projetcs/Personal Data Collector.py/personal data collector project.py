#*********************************WELCOME INSTRUCTIONS***********************************

print("Welcome to the Personal Data Collector ")
print(" ")
print("This program collects , processes , stores and displays your personal information")
print("-"*81)
print(" "," "," ")

#*********************************COLLECTING INFORMATION CODE*****************************
name=input("Enter your name : ")
age=input("Enter your age : ")
height=input("Enter your height : ")
weight=input("Enter your weight : ")
fav_no=input("Enter your Favourite number : ")
fav_hob=input("Enter your Favourite hobbie : ")


#type casting
age_tc=int(age)
height_tc=float(height)
weight_tc=float(weight)
fav_num=int(fav_no)
print(" ")
print("Thankyou -Here is the information we collected .")
print("-"*81)
print(" ")

#--------------------------------------Display code---------------------------------------

print(f"Name: {name}, Type: {type(name)}, Memory Address: {id(name)}")
print(f"Age: {age_tc}, Type: {type(age_tc)}, Memory Address: {id(age_tc)}")
print(f"Height: {height_tc}, Type: {type(height_tc)}, Memory Address: {id(height_tc)}")
print(f"Weight: {weight_tc}, Type: {type(weight_tc)}, Memory Address: {id(weight_tc)}")
print(f"Favourite Number: {fav_num}, Type: {type(fav_num)}, Memory Address: {id(fav_num)}")
print(f"Favourite Hobby: {fav_hob}, Type: {type(fav_hob)}, Memory Address: {id(fav_hob)}")
print(" ")
print(" ")

#==============================================birthyear code================================
present_year=2026
approx_by=present_year-age_tc
print(f"Your approx birth year is :{approx_by} based on your given age.")
print(" ")

print("="*81)
print("Thankyou for using the personal data collector.Have a Good day :)")
