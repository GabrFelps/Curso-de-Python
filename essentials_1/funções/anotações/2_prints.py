#print com end

print("Oi, meu nome é", end=" ")  #junta os print atual com o posterior recebendo um argumento em string " "; ""; "pipipipopopo"
print("Felipe")
#output= Oi, meu nome é Felipe

#print com sep

print("My", "name", "is", "Monty", "Python.", sep="-") #caracteriza o termo que vai separar cada argumento do print 
#output= My-name-is-Monty-Python.

#utilização do end e sep juntos

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n") 
#output= My_name_is*Monty*Python.*

