p = 'fdsnfdsnfdsf' \
    'djfndjfndsfndslknfdsf' \
    ''



l = [i for i in p.split('\n')]
l = [i for i in l[0].split(':')]
l = [i.replace(" ", "") for i in l[1].split(',')]
print(l)