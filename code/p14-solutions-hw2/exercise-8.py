def itExists(needle, haystack):
    counter = 0
    for x in haystack:
        if x == needle:
            counter += 1

    if counter > 0:
        return True
    else:
        return False

n = 10
numbers = [4, 7, 10, 12, 1, 8, 20]

if itExists(n, numbers):
    print("FOUND IT")
else:
    print("Couldn't find that number")
