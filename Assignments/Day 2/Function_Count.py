##Closure
def outer():
    count=0
    def inner():
        nonlocal count
        count=count+1
        print(count)
    return inner

#counter in hello, count is increased only when hello() is called
hello = outer()
hello()
hello()
hello()
#Hi has separate count, count is increase only when hi() is called
hi = outer()
hello()
hello()
hello()
hi()
hi()
hi()






