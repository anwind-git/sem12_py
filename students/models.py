import csv
import re


class Descriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        cleaned_value = re.sub(r'[^А-Яа-я]', '', value)
        instance.__dict__[self.name] = cleaned_value.title()

    def __set_name__(self, owner, name):
        self.name = name


class Student:
    last_name = Descriptor()
    first_name = Descriptor()
    middle_name = Descriptor()

    def __init__(self, id_student, last_name, first_name, middle_name, birth_year):
        self.id_student = id_student
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birth_year = birth_year
        self.subjects = []
        self.appraisal = {}
        self.load_subjects_from_csv()

    def load_subjects_from_csv(self):
        with open('subject.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                subject = row[0]
                self.subjects.append(subject)
                self.appraisal[subject] = {'оценка': None, 'тест': None}

    def add_appraisal(self, subject, appraisal, test_result):
        if subject in self.appraisal:
            self.appraisal[subject]['оценка'] = appraisal
            self.appraisal[subject]['тест'] = test_result
        else:
            print(f"Предмета: {subject} не существует для данного студента.")

    def calculate_average_test_grade(self, subject):
        if subject in self.appraisal:
            test_result = self.appraisal[subject]['тест']
            if isinstance(test_result, list):
                if test_result:
                    return sum(test_result) / len(test_result)
                else:
                    return None
            else:
                return None
        else:
            print(f"Предмета '{subject}' не существует для данного студента.")

    def calculate_overall_average_grade(self):
        appraisal = []
        for subject in self.appraisal.values():
            grades = subject.get('оценка', [])
            if isinstance(grades, int):
                grades = [grades]
            appraisal.extend(grade for grade in grades if grade is not None)
        if appraisal:
            return sum(appraisal) / len(appraisal)
        else:
            return None