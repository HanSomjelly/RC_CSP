# RC, Conditionals Notes, CSP, 6th

military_time = 900

if military_time < 600:
    print('its to early why are you awake!!!!!')
elif military_time < 900:
    print('good morning!')
elif military_time < 1200:
    print('good morning you should be at school!')
elif military_time < 1700:
    print('good afternoon')
else:
    print('Good evening')

#nesting coditionals
day = "saturday"
time = 900

if time > and time < 1600:
    if day != "saturday" or day != "sunday":
        print('you should be at school!')
    else:
        if time > 1200:
            print('good afternoon')
        else:
            print('good morning')
else: