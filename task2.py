def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title

def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print ("Имя:", first_name)
    print("Фамилия:", last_name)
    print("Профессия:", job)
    print("Титул:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")