

food_logs = [

          [1,"adithya","dosa","meals","chapathy",1800],#0
#          0      1       2      3        4        5
          [2,"shreya","idly","biriyani","chapathy",2100],#1
#          0     1       2       3          4       5
          [3,"amritha","appam","meals","puttu",1700],#2
#          0     1        2       3       4     5         
          [4,"dijo",";protein shake","mandhi","puttusalad",1900]#3
#          0    1         2             3          4         5


]

# print(food_logs[1][5])
# print(food_logs[3][4])


social_media_posts =[
                     
        [1,"goodmorning",500,600,"arun"],
        [2,"goodnight",400,300,"vipin"],
        [3,"goodevening",100,700,"sibin"],
        

]

print(social_media_posts[1][2])

for lst in social_media_posts:
    
    print(lst[4])

# all_names = [lst[4] for lst in social_media_posts]

# print(all_names)

# insta_views = [lst[2] for lst in social_media_posts]

# print(insta_views)



# max_insta_views = max(insta_views)

# print(max_insta_views)



# for lst in social_media_posts:
    
#     facebook_likes = lst[3]

#     if facebook_likes==700:

#         print(lst[4])


# for lst in social_media_posts:
    
#     if lst[3] == 700:

#         print(lst[4])


# facebook_filter = [lst[4] for lst in social_media_posts   if lst[3]==700]

# print(facebook_filter)


# max_cal = max([lst[-1] for lst in food_logs])

# print(max_cal)

# max_calorie_name = [lst[1] for lst in food_logs if lst[-1]==max_cal]

# print(max_calorie_name)


# min_cal = min([lst[-1] for lst in food_logs])

# print(min_cal)

# min_calorie_name = [lst[1] for lst in food_logs if lst[-1]==min_cal]

# print(min_calorie_name)
    
movies = [
    [1, "K.G.F: Chapter 1", "Yash", "Kannada", 8.2, 1234567],
    [2, "K.G.F: Chapter 2", "Yash", "Kannada", 8.3, 678900],
    [3, "K.G.F: Chapter 3", "Yash", "Kannada", 9.5, 456789], # Anticipated
    [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
    [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], # Hype Rating
    [6, "Aavesham", "Fahadh Faasil", "Malayalam", 7.9, 1234567]
]

# # display all movie title
# # movie with top rating
# # display kannada movies
# # display movies whre actor is yash
# # which language most number of movies
# # movie with max budget
# # languages



# all_movie_title = [lst[1] for lst in movies]

# # print(all_movie_title)


# max_rating = max([lst[4] for lst in movies])

# max_rating_movie_name = [lst[1] for lst in movies if lst[4]==max_rating]

# # print(max_rating_movie_name)

# movie_name = [lst[1] for lst in movies if lst[3]=="Kannada"]

# # print(movie_name)


movie_name = [lst[1] for lst in movies if lst[2]=="Yash"]

print(movie_name)




# max_budjet = max([lst[5] for lst in movies])

# # print(max_budjet)


# languages = [lst[3] for lst in movies]

# # print(languages)

# language_count={}

# for lst in movies:

#     language = lst[3]

#     if language in language_count:

#         language_count[language]+=1
#     else:
#         language_count[language]=1

# # print(language_count)

# max_language = None
# max_count=0

# for language,count in language_count.items():

#     if count>max_count:

#         max_count=count
#         max_language=language

# # print(max_language,max_count)

# orders = {"tea":15,"coffee":21,"dosa":34,"rice":67}

# result = sorted(orders)

# # print(result)

# orders_list = [[v,k] for k,v in orders.items()]

# # print(orders_list)

# print(sorted(orders_list,reverse=True))


# text ="python programming"

# char_count = {ch:text.count(ch) for ch in text}

# # print(char_count)


# text ="python programming"

# char_count = {ch:text.count(ch) for ch in text}

# # print(char_count)


# char_count_list = [[v,k] for k,v in char_count.items()]

# # print(sorted(char_count_list,reverse=False))
# # print(sorted(char_count_list,reverse=True))


# languages= [ "thamil","malayalam","kannada","telungu","kannada","telungu","thamil","malayalam","thamil","malayalam"]
 
# language_count = {l:languages.count(l) for l in languages}

# # print(language_count)


# language_count_list = [[v,k] for k,v in language_count.items()]

# # print(sorted(language_count_list,reverse=False))

# # print(sorted(language_count_list,reverse=True))
# # print(sorted(language_count_list,reverse=True)[0]) #max value
# # print(sorted(language_count_list,reverse=True)[-1])#min value








