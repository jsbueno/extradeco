
## extradeco

###   parametrized(flat_decorator)

A super-flatter decorator decorator!

One is supposed to decorate what would be your inner "wrapper" function in a decorator with
"parametrized". That "wrapper" can now be used as a paramterized decorator with extra parameters
whatever parameters it takes when decorating are passed along with the func object when the func itself
is called - "*args" and "**kwargs" arguments should be passed down in the call to the original `func`.

### Example of use:

Create a flat decorator which wants parameters by doing:

```
from extradeco import paremetrized

@parametrized
def ubberlog(func, loglevel, *args, **kw):
    if loglevel > 2:
        print ("doing things")
    if loglevel > 1:
        print("doing less things")
    # Line that calls the original function directly on the decorator body
    result = func(*args, **kw)
    if loglevel:
        print("function returned", result)
    return result
```

And then, the new logger decorator is ready to be used like this:


```

@ubberlog(2)
def soma(a, b):
    return a + b


@ubberlog(1)
def s1(a, b):
    return a + b
```

### Warning
For now, the parameter names in the decorator cannot match any parameter name in the final decorated function.
It is advised that you prefix the parameter names in the decorator with somethign that won't be present in the decorated functions.
