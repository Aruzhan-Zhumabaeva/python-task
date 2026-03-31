def hours_to_seconds(hours):
    return hours * 3600



def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "часов — это", secs, "секунд")


test(10)
test(1)
test(25)
test(100)
test(33)