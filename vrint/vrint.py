# # vrint.py

# class VrintToken:
#     """A token that changes the vrint state when accessed."""
#     def __init__(self, value, parent):
#         self.value = value
#         self.parent = parent
    
#     def __bool__(self):
#         """When used in boolean context, change the parent's state."""
#         self.parent._verbose = self.value
#         return self.value

# class Vrint:
#     _instance = None
#     _verbose = True
    
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(Vrint, cls).__new__(cls)
#         return cls._instance

#     def __call__(self, *args, **kwargs):
#         """
#         Prints the given arguments only if verbose is True.
        
#         Parameters:
#         *args: Arguments to be printed. vrint.true/vrint.false can be included to control printing.
#         **kwargs: Keyword arguments passed to print function
#         """
#         # Check for override tokens in args
#         override_on = next((arg for arg in args if isinstance(arg, VrintToken) and arg.value is True), None)
#         override_off = next((arg for arg in args if isinstance(arg, VrintToken) and arg.value is False), None)
        
#         # Determine if we should print
#         if override_off is not None:
#             should_print = False
#         elif override_on is not None:
#             should_print = True
#         else:
#             should_print = self._verbose
            
#         # Filter out the control tokens from what gets printed
#         filtered_args = [arg for arg in args if not isinstance(arg, VrintToken)]
        
#         if should_print and filtered_args:  # Only print if there are actual args
#             print(*filtered_args, **kwargs)

#     # Property for checking current verbose state
#     @property 
#     def verbose(self):
#         """Get or set the verbose mode to True."""
#         old_verbose = self._verbose
#         self._verbose = True
#         return VrintToken(True, self)

#     @property
#     def quiet(self):
#         """Set the verbose mode to False."""
#         old_verbose = self._verbose
#         self._verbose = False
#         return VrintToken(False, self)

#     @property
#     def true(self):
#         """Return a token to force printing regardless of verbose setting."""
#         return VrintToken(True, self)

#     @property
#     def false(self):
#         """Return a token to force no printing regardless of verbose setting."""
#         return VrintToken(False, self)





# import functools
# from contextlib import contextmanager

# class Vrint:
#     def __init__(self):
#         self._verbose = False
#         self._stack = []  # Stack to track verbose states
    
#     def __call__(self, message, state=None):
#         # Determine if we should print based on current state or provided override
#         should_print = self._verbose
#         if state is not None:
#             if hasattr(state, '_for_function_scope'):
#                 # If it's our special temporary state object, don't change global state
#                 should_print = state.value
#             else:
#                 # Direct boolean or other value
#                 should_print = bool(state)
        
#         if should_print:
#             print(message)
    
#     @property
#     def verbose(self):
#         """Permanently sets verbose mode to True globally"""
#         self._verbose = True
#         return True
    
#     @property
#     def quiet(self):
#         """Permanently sets verbose mode to False globally"""
#         self._verbose = False
#         return False
    
#     @property
#     def true(self):
#         """Returns a temporary state object that doesn't affect global state"""
#         return _TemporaryState(True)
    
#     @property
#     def false(self):
#         """Returns a temporary state object that doesn't affect global state"""
#         return _TemporaryState(False)
    
#     @contextmanager
#     def temp_state(self, state):
#         """Context manager for temporarily changing the verbose state"""
#         previous_state = self._verbose
#         self._verbose = state
#         try:
#             yield
#         finally:
#             self._verbose = previous_state

# class _TemporaryState:
#     """Special object for function-scoped temporary states"""
#     def __init__(self, value):
#         self.value = value
#         self._for_function_scope = True  # Special marker
    
#     def __bool__(self):
#         return self.value
    
#     def __call__(self):
#         # This allows vrint_state() to work inside functions
#         # but doesn't actually do anything except evaluate to the state value
#         return self.value




# from contextlib import contextmanager

# class VerboseStateObject:
#     """Smart state object that works both globally and for function scope"""
#     def __init__(self, vrint_obj, value):
#         self.vrint_obj = vrint_obj
#         self.value = value
#         self._for_function_scope = True  # Marker for the decorator
    
#     def __bool__(self):
#         return self.value

# class Vrint:
#     def __init__(self):
#         self._verbose = False
    
#     def __call__(self, message, state=None):
#         should_print = self._verbose
#         if state is not None:
#             if hasattr(state, '_for_function_scope'):
#                 should_print = state.value
#             else:
#                 should_print = bool(state)
        
#         if should_print:
#             print(message)
    
#     @property
#     def verbose(self):
#         """Smart property that changes state globally when accessed directly"""
#         self._verbose = True
#         return VerboseStateObject(self, True)
    
#     @property
#     def quiet(self):
#         """Smart property that changes state globally when accessed directly"""
#         self._verbose = False
#         return VerboseStateObject(self, False)
    
#     # For backward compatibility
#     @property
#     def true(self):
#         return self.verbose
    
#     @property
#     def false(self):
#         return self.quiet
    
#     @contextmanager
#     def temp_state(self, state):
#         """Context manager for temporarily changing the verbose state"""
#         previous_state = self._verbose
#         self._verbose = state
#         try:
#             yield
#         finally:
#             self._verbose = previous_state





# # try2.py
# from contextlib import contextmanager

# class VerboseStateObject:
#     """Smart state object that works both globally and for function scope"""
#     def __init__(self, vrint_obj, value):
#         self.vrint_obj = vrint_obj
#         self.value = value
#         self._for_function_scope = True  # Marker for the decorator
    
#     def __bool__(self):
#         return self.value

# class Vrint:
#     def __init__(self):
#         self._verbose = False
    
#     def __call__(self, message, state=None):
#         should_print = self._verbose
#         if state is not None:
#             if hasattr(state, '_for_function_scope'):
#                 should_print = state.value
#             else:
#                 should_print = bool(state)
        
#         if should_print:
#             print(message)
    
#     @property
#     def verbose(self):
#         """Smart property that changes state globally when accessed directly"""
#         self._verbose = True
#         return VerboseStateObject(self, True)
    
#     @property
#     def quiet(self):
#         """Smart property that changes state globally when accessed directly"""
#         self._verbose = False
#         return VerboseStateObject(self, False)
    
#     # For backward compatibility
#     @property
#     def true(self):
#         return self.verbose
    
#     @property
#     def false(self):
#         return self.quiet
    
#     @contextmanager
#     def temp_state(self, state):
#         """Context manager for temporarily changing the verbose state"""
#         previous_state = self._verbose
#         self._verbose = state
#         try:
#             yield
#         finally:
#             self._verbose = previous_state
            
#     def state(self, state_obj):
#         """Context manager to temporarily set vrint state from a state object"""
#         if hasattr(state_obj, '_for_function_scope'):
#             return self.temp_state(state_obj.value)
#         else:
#             return self.temp_state(bool(state_obj))



# # try3.py
# from contextlib import contextmanager
# import functools, inspect

# class VerboseStateObject:
#     """Smart state object that works both globally and for function scope"""
#     def __init__(self, vrint_obj, value):
#         self.vrint_obj = vrint_obj
#         self.value = value
#         self._for_function_scope = True  # Marker for the decorator
    
#     def __bool__(self):
#         return self.value
    
#     def __getattr__(self, name):
#         """
#         Dynamic attribute access to enable syntax like:
#         vrint.quiet.my_function()
#         vrint.verbose.some_other_function()
#         """
#         # Look for the function in the global namespace
#         import sys
#         caller_globals = inspect.currentframe().f_back.f_globals
        
#         if name in caller_globals and callable(caller_globals[name]):
#             # Get the function from caller's global namespace
#             func = caller_globals[name]
            
#             # Return a wrapper that runs the function with this state
#             @functools.wraps(func)
#             def wrapped_func(*args, **kwargs):
#                 with self.vrint_obj.state(self):
#                     return func(*args, **kwargs)
            
#             return wrapped_func
        
#         # Look in the caller's local namespace if not found in globals
#         caller_locals = inspect.currentframe().f_back.f_locals
#         if name in caller_locals and callable(caller_locals[name]):
#             func = caller_locals[name]
            
#             @functools.wraps(func)
#             def wrapped_func(*args, **kwargs):
#                 with self.vrint_obj.state(self):
#                     return func(*args, **kwargs)
            
#             return wrapped_func
        
#         raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}', "
#                             f"and no function named '{name}' was found in the current scope")

# class Vrint:
#     def __init__(self):
#         self._verbose = False
    
#     def __call__(self, message, state=None):
#         should_print = self._verbose
#         if state is not None:
#             if hasattr(state, '_for_function_scope'):
#                 should_print = state.value
#             else:
#                 should_print = bool(state)
        
#         if should_print:
#             print(message)
    
#     @property
#     def verbose(self):
#         """Smart property that changes state globally when accessed directly"""
#         self._verbose = True
#         return VerboseStateObject(self, True)
    
#     @property
#     def quiet(self):
#         """Smart property that changes state globally when accessed directly"""
#         self._verbose = False
#         return VerboseStateObject(self, False)
    
#     # For backward compatibility
#     @property
#     def true(self):
#         return self.verbose
    
#     @property
#     def false(self):
#         return self.quiet
    
#     @contextmanager
#     def temp_state(self, state):
#         """Context manager for temporarily changing the verbose state"""
#         previous_state = self._verbose
#         self._verbose = state
#         try:
#             yield
#         finally:
#             self._verbose = previous_state
            
#     def state(self, state_obj):
#         """Context manager to temporarily set vrint state from a state object"""
#         if hasattr(state_obj, '_for_function_scope'):
#             return self.temp_state(state_obj.value)
#         else:
#             return self.temp_state(bool(state_obj))









# try4.py
import functools

class VerboseStateObject:
    """Smart state object that works for function scope and per-call control"""
    def __init__(self, vrint_obj, value):
        self.vrint_obj = vrint_obj
        self.value = value
    
    def __bool__(self):
        return self.value
    
    def __call__(self, func_result):
        """Enable syntax: vrint.verbose(myfunc())"""
        # Function was already called, this just modifies state temporarily
        return func_result

class Vrint:
    def __init__(self):
        self._verbose = False
    
    def __call__(self, message, state=None):
        should_print = self._verbose
        if state is not None:
            if hasattr(state, 'value'):
                should_print = state.value
            else:
                should_print = bool(state)
        
        if should_print:
            print(message)
    
    @property
    def verbose(self):
        """Smart property that changes state globally when accessed directly"""
        self._verbose = True
        return VerboseStateObject(self, True)
    
    @property
    def quiet(self):
        """Smart property that changes state globally when accessed directly"""
        self._verbose = False
        return VerboseStateObject(self, False)