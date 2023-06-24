from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

store = Store()
#print(store.bd)

name_1= "Priscila"
job_1 = "QA"

user = User(name=name_1, job=job_1)
#print(user.name)
#print(user.job)


print ("#Primeiro Teste")
name_1= "Daniele"
job_1 = "QA"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
print(service.store.bd[0].name)
print(service.store.bd[0].job)
print(resultado)

print ("#Segundo Teste")
name_1= None
job_1 = "QA"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
print(resultado)

print ("#Terceiro Teste")
name_1= 123987
job_1 = "QA"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
print(resultado)

print ("#Quarto Teste")
name_1= "Amanda"
job_1 = "QA"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
resultado = service.add_user(name=name_1, job=job_1)
print(resultado)

print ("#Quinto Teste")
name_1= "Joao"
job_1 = "QA"

service = ServiceUser()
resultado = service.remove_user(name=name_1)
print(resultado)

print ("#Sexto Teste")
name_1= "Fabricio"
job_1 = "QA"
job_2 = "Dev"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
resultado = service.update_user(name=name_1, new_job=job_2)
print(resultado)

print ("#Setimo Teste")
name_1= "Aline"
job_1 = "Finance"
name_2= "Camila"
job_2 = "Finance"
name_3= "Marcelo"
job_3 = "Dev"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
resultado = service.add_user(name=name_2, job=job_2)
resultado = service.add_user(name=name_3, job=job_3)
resultado = service.list_user(job=job_1)
print(resultado)

print ("#Oitavo Teste")
name_1= "Aline"
job_1 = "Finance"
name_2= "Camila"
job_2 = "Finance"
name_3= "Marcelo"
job_3 = "Dev"
job_4 = "PO"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
resultado = service.add_user(name=name_2, job=job_2)
resultado = service.add_user(name=name_3, job=job_3)
resultado = service.list_user(job=job_4)
print(resultado)








