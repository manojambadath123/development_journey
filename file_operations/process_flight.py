

fr = open("file_operations\\flight.txt","r")

flight =[]

for line in fr:

    data = line.rstrip("\n").split(",")

    # print(data)

    passenger_data = {"year":int(data[0]),"month":data[1],"passengers":int(data[2])}

    flight.append(passenger_data)

# print(flight)

year_wise_count ={}

for p in flight:

    year = p.get("year")

    p_count = p.get("passengers")

    if year in year_wise_count:

        year_wise_count[year]+=p_count

    else:

        year_wise_count[year]=p_count

print(year_wise_count)

year_wise_count_list = sorted([[v,k] for k,v in year_wise_count.items()],reverse=True)

print(year_wise_count_list)

year_wise_count_sorted = sorted(year_wise_count,key =year_wise_count.get)

print(year_wise_count_sorted)

year_wise_count_sorted = sorted(year_wise_count,key= lambda x:year_wise_count.get(x))

print(year_wise_count_sorted)


        





    



    

