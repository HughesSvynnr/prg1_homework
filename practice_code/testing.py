'''print("Give me a number")
number = input(">")
factors_list=[]
for x in range(1, int(number)+1):
    if(int(number)%x==0):
        factors_list.append(x)
print(number, " has ",len(factors_list)," factors, "," which are ",factors_list)

print("Tell me a word")
word = input(">")
word_split = word.split(" ")
for x in word:'''
city_to_check = input("What city are we checking? Cheyenne, Santa Fe, Tucson, Great Falls, or Honolulu? >")
cleanest_cities = ["Cheyenne","Santa Fe","Tucson","Great Falls","Honolulu"]
for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("its a clean city")
    else:
        print("not a clean city")