# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}


# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if student_scores[key] < 100 and student_scores[key] >= 91:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] < 90 and student_scores[key] >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] < 80 and student_scores[key] >= 71:
#         student_grades[key] = "Acceptable"
#     elif student_scores[key] <= 70:
#         student_grades[key] = "Fail"
    

# # 🚨 Don't change the code below 👇
# print(student_grades)


# travel_log = {
#     "Europe": {"cities_visited": ["Paris", "Berlin", "Loundon"], "food_review": {"France": 10, "Berlin": 7, "Loundon": 3}}
# }

# print(travel_log["Europe"]["food_review"]["Loundon"])

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, times_visited, cities_visited):
    print("Updating Travel Log:")
    print(f"Country visited: {country}")
    print(f"Number of times visited: {times_visited}")
    print(f"Cities visited: {', '.join(cities_visited)}")
    travel_log.append({"contry": country, "visits": times_visited, "cities": cities_visited})


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
