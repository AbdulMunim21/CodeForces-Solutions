year = input()
int_year = int(year) + 1
set_year = set(str(int_year))

while(len(set_year) != 4): 
    int_year = int_year + 1
    set_year = set(str(int_year))
    
print(int_year)