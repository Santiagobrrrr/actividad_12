students = {}
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
        if num_students > 0:
            break
        else:
            print(f"Intente de nuevo")


for i in range(num_students):
    print(f"\nEstudiante #{i+1}")
    name_student = input(f"Nombre del estudiante {i+1}: ")
    while True:
        try:
            count_grades_student = int(input(f"\n¿Cuántas notas desea ingresar para {name_student}?: "))
            if count_grades_student >= 0:
                break

        except ValueError:
            print(f"Error: ingreso mal el tipo de valor")

        except TypeError:
            print(f"Error: ingreso mal el tipo de valor")

        except Exception as e:
            print(f"Error: {e}")

    sum = 0
    for j in range(count_grades_student):
        while True:
            try:
                nota = float(input(f"Ingrese la nota #{j + 1}: "))
                if nota >= 0 and nota <= 100:
                    sum += nota
                    break
                else:
                    print(f"La nota debe de ser entre 0 y 100")

            except ValueError:
                print(f"Ingrese una nota válida.")

            except TypeError:
                print(f"Error: ingreso mal el tipo de valor")

            except Exception as e:
                print(f"Error: {e}")
    try:
        avg = sum / count_grades_student
        students[name_student] = avg

    except ZeroDivisionError:
        print(f"Error: no puede dividir por 0")

    except Exception as e:
        print(f"Error: {e}")

    else:
        break

print(f"\n--- Promedios ---")
if len(students) == 0:
    print("No hay promedios ingresados")

else:
    for estudiante, avg in students.items():
        print(f"{estudiante}: {avg}")