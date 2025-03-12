# from .vrint import Vrint
# import functools

# vrint = Vrint()

# # Optional decorator for function-scoped verbose control
# def with_vrint_state(func):
#     @functools.wraps(func)
#     def wrapper(vrint_state, *args, **kwargs):
#         # If it's our temporary state object
#         if hasattr(vrint_state, '_for_function_scope'):
#             with vrint.temp_state(vrint_state.value):
#                 return func(vrint_state, *args, **kwargs)
#         else:
#             # Regular boolean or other value
#             return func(vrint_state, *args, **kwargs)
#     return wrapper

# __all__ = ['vrint', 'with_vrint_state']




# # try2.py
# from .vrint import Vrint
# import functools
# import inspect

# vrint = Vrint()

# # Optional decorator for function-scoped verbose control
# def with_vrint_state(func):
#     sig = inspect.signature(func)
#     has_vrint_param = 'vrint_state' in sig.parameters
    
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         vrint_state = kwargs.pop('vrint_state', None)
        
#         if vrint_state is not None:
#             # Temporarily set vrint state during function execution
#             with vrint.state(vrint_state):
#                 if has_vrint_param:
#                     kwargs['vrint_state'] = vrint_state
#                     return func(*args, **kwargs)
#                 else:
#                     return func(*args, **kwargs)
#         else:
#             # No vrint_state provided, just call the function normally
#             if has_vrint_param:
#                 kwargs['vrint_state'] = None
#             return func(*args, **kwargs)
            
#     return wrapper

# __all__ = ['vrint', 'with_vrint_state']





# # try3.py
# from .vrint import Vrint

# # Create a single instance of Vrint
# vrint = Vrint()

# # Export only the vrint instance
# __all__ = ['vrint']


# try4.py
from .vrint import Vrint
import functools
# Create a single instance of Vrint
vrint = Vrint()

# Decorator for function-scoped verbose control
def with_vrint_state(func):
    """
    Decorator that allows a function to accept a vrint_state parameter
    to control verbosity within that function.
    
    Usage:
    @with_vrint_state
    def my_func():
        vrint("This message may or may not be printed")
        
    my_func(vrint_state=vrint.verbose)  # Will print the message
    my_func(vrint_state=vrint.quiet)    # Will not print the message
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check if first arg is a VerboseStateObject (from vrint.verbose or vrint.quiet)
        vrint_state = None
        if args and hasattr(args[0], 'vrint_obj') and hasattr(args[0], 'value'):
            vrint_state = args[0]
            args = args[1:]  # Remove the vrint_state from args
        else:
            # Check for explicit vrint_state in kwargs
            vrint_state = kwargs.pop('vrint_state', None)
        
        # Store original state
        original_state = vrint._verbose
        
        try:
            # Set temporary state if provided
            if vrint_state is not None:
                if hasattr(vrint_state, 'value'):
                    vrint._verbose = vrint_state.value
                else:
                    vrint._verbose = bool(vrint_state)
            
            # Call function with new state
            return func(*args, **kwargs)
        finally:
            # Restore original state
            vrint._verbose = original_state
            
    return wrapper

# Export the vrint instance and the decorator
__all__ = ['vrint', 'with_vrint_state']