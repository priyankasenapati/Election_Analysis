counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver' : 
     print(counties[1])
     
for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}   
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for county in counties_dict.values():
    print(county)  

for voters in counties_dict.values():
    print(voters)  

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key, value)

for key, value  in counties_dict.items():
    print(key, " county has ", value ," registered voters. ")
for value in counties_dict.values():
        print(value)
for key, value in counties_dict.items():
    print(key, "\n", value)   
for county in counties_dict:
    print(county)         
for key, value  in counties_dict.items():
    print(key + " county has " + str(value) + " registered voters. ")
for key, value in counties_dict.items():
    print(key, "/n", value)    

for key, value  in counties_dict.items():
    print(f"key  county has {value} registered voters. ")    


counties_dict = {"Arapahoe": 4229999.82999, "Denver": .46330053, "Jefferson": 432.438}  
for key, values in counties_dict.items():
    print(f"key county has { values:,.2f} registered voters")  