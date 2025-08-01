students = []
grade = []

while True:
    try:
        num_students = int(input(f"¿Qué cantidad de estudiantes ingresara? "))

    except ValueError:
        print(f"Error: ingreso mal un valor")

    except TypeError:
        print(f"Error: ingreso mal el tipo de valor")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

    else:
        num_students = num_students
        break

for i in range(num_students):
    print(f"Estudiante #{i+1}")
    name_student = input(f"Nombre del estudiante {i+1}: ")
    while True:
        try:
            count_grades_student = int(input(f"¿Cuántas notas desea agregar al estudiante {i+1}?: "))

        except ValueError:
            print(f"Error: ingreso mal el tipo de valor")

        except TypeError:
            print(f"Error: ingreso mal el tipo de valor")

        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

        else:
            count_grades_student = count_grades_student


for j in range(count_grades_student):
    grades_student = int(input(f"Notas del estudiante {i+1}: "))
