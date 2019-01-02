x = None
while not x:
    try:
        x = int(input('input number:'))
    except StandardError as e:
        print ('error { %s } happened. try once more') % (e.message)
print ('finally!')