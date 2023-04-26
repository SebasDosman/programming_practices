from Department import Department
from Doctor import Doctor
from DoctoralStudent import DoctoralStudent
from PAS import PAS
from PDI import PDI
from People import People
from Student import Student
from UndergraduateStudent import UndergraduateStudent 
from University import University
from Worker import Worker

department = Department("Mathematics")
doctor = Doctor(1, "Mauro", "01/01/2020")
doctoral_student = DoctoralStudent(1, "Carlos", "Computer science")
pas = PAS("Doctor", doctor)
pdi = PDI("A", doctor)
people = People(1, "Juan")
student = Student(1, "Pedro")
undergraduate_student = UndergraduateStudent(1, "Maria", "Computer science")
university = University("Oxford", "USA", department)
worker = Worker(1, "Luis", "01/01/2020")

print("\n", department.name,
      "\n", doctor.name,
      "\n", doctoral_student.name,
      "\n", pas.worker.name,
      "\n", pdi.worker.name, 
      "\n", people.name, 
      "\n", student.name,
      "\n", undergraduate_student.name, 
      "\n", university.department.name,   
      "\n", worker.name)