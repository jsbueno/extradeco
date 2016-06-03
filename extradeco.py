from functools import wraps, partial
from inspect import signature, _empty, Parameter as P

def parametrized(flat_decorator):
    """
    A super-flatter decorator decorator!

    One is supposed to decorate what would be your inner "wrapper" function in a decorator with
    "paramtrized". That "wrapper" can now be used as a parametrized decorator with extra parameters
    whatever parameters it takes when decorating are passed along with the func object when the func itself
    is called - "*args" and "**kwargs" arguments should be passed down in the call to the original `func`.

    """
    sig = signature(flat_decorator)
    first_parameter = next(iter(sig.parameters.values()))
    if first_parameter.kind not in (P.POSITIONAL_ONLY, P.POSITIONAL_OR_KEYWORD) or first_parameter.default is not _empty:
        raise TypeError("Decorators must have a mandatory first parameter that accepts the decorated object")
    var_positional_found = False
    var_keyword_found = False
    for name, parameter in reversed(list(sig.parameters.items())):
        var_positional_found |= parameter.kind is P.VAR_POSITIONAL
        var_keyword_found |= parameter.kind is P.VAR_POSITIONAL
        if var_positional_found and var_keyword_found: break
    else:
        raise TypeError("Decorators must accept var_positional (*args) and var_keyword(**kwargs) parameters:\n"
            "    these will contain the parameters to be passed to the decorated function at call time")

    decorator_parameters = [par for par in sig.parameters.values() if par.kind in (P.POSITIONAL_ONLY, P.POSITIONAL_OR_KEYWORD)]

    minimum_parameters = sum(1 for par in decorator_parameters if par.default is _empty)
    maximum_parameters =  len(decorator_parameters)

    @wraps(flat_decorator)
    def decorator_wrapper(*args, **kwargs):
        # called at "parameters for the decorator binding time"

        decorator_level_parameters = sig.bind(*((None, ) + args), **kwargs)
        num_args = len(decorator_level_parameters.args)
        if decorator_level_parameters.kwargs:
            raise TypeError("""Decorator '{}' called with more named parameters than explicit in its signature:\n"
                "    keyword only args are reserved to be used by calls to the decorated function at runtime""".format(flat_decorator.__name__))
        if num_args < minimum_parameters:
            raise TypeError("Missing mandatory positional parameters for decorator '{}'".format(flat_decorator.__name__))
        if num_args > maximum_parameters:
            raise TypeError("More positional parameters than supported for decorator '{}':\n"
                "Extra positional parameters are to be passed to the decorated function at call time".format(flat_decorator.__name__))

        decorator_defaults = decorator_level_parameters.args[1:] + tuple(par.default  for par in decorator_parameters[num_args: maximum_parameters])
        def actual_decorator(func):
            # called when the parametrized decorator is actually decorating (called with a function as sole parameter)
            @wraps(func)
            def function_wrapper(*args, **kwargs):
                # called at final-decorated-function call time.
                final_args =  decorator_defaults + args
                return flat_decorator(func, *final_args, **kwargs)
            return function_wrapper
        return actual_decorator
    return decorator_wrapper


"""
# desired use:

@parametrized
def ubberlog(func, loglevel, *args, **kw):
    if loglevel > 2:
        print ("doing things")
    if loglevel > 1:
        print("doing less things")
    result = func(*args, **kw)
    if loglevel:
        print("function returned", result)
    return result


@ubberlog(2)
def soma(a, b):
    return a + b


@ubberlog(1)
def s1(a, b):
    return a + b

# Needs more testing- some corner cases are not right.
"""