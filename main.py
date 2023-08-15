from students import models

s1 = models.Student(1, "иванов??11", "иван", "иванович", 2000)
s2 = models.Student(2, "петров", "петр   55", "петрович159", 2001)

s1.add_appraisal('физика', 3, 60)
s1.add_appraisal('химия', 2, 40)
s1.add_appraisal('математика', 5, 100)

average_overall_grade = s1.calculate_overall_average_grade()

print(s1.last_name, s1.first_name, s1.appraisal)

print(f"Общий средний балл: {average_overall_grade}")
print('---------------------------------------------')
s2.add_appraisal('физика', 4, 80)
s2.add_appraisal('химия', 5, 100)
s2.add_appraisal('математика', 4, 80)

average_overall_grade = s2.calculate_overall_average_grade()

print(s2.last_name, s2.first_name, s2.appraisal)

print(f"Общяя средяя оценка: {average_overall_grade}")