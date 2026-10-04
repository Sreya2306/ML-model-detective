student_name = input("Enter your name: ")
hours_per_day = float(input("How many hours will you study per day? "))
study_days = int(input("How many days will you study this week? "))

total_hours = hours_per_day * study_days

print("\nStudy Plan")
print(f"Student: {student_name}")
print(f"Hours per day: {hours_per_day}")
print(f"Study days: {study_days}")
print(f"Total planned study hours: {total_hours}")