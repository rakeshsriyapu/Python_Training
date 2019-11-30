date = int(input("Enter Date:"))
day = date%7;
dict_day = {1:"Friday",2:"Saturday",3:"Sunday",4:"Monday",5:"Tuesday",6:"Wednesday",7:"Thursday"}
if(date>=1) and (date<=30):
    print(dict_day[day])
else:
    print("Invalid Date")
