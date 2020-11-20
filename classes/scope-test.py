def scope_test():
    def scope_local():
        var = 'locally scoped var'

    def scope_nonlocal():
        nonlocal var
        var = 'non locally scoped var'

    def scope_global():
        global var
        var = 'globally scoped var'

    var = 'test variable'
    scope_local()
    print("After local assignment:", var)
    scope_nonlocal()
    print("After nonlocal assignment:", var)
    scope_global()
    print("After global assignment:", var)


scope_test()
print("In global scope:", var)