
from threading import Timer

def debounce(wait):
    """ Decorator that will postpone a functions
        execution until after `wait` seconds
        have elapsed since the last time it was invoked. """
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)
            if not hasattr(debounced, '_timer'):
                debounced._timer = None
            if debounced._timer is not None:
                debounced._timer.cancel()
            debounced._timer = Timer(wait, call_it)
            debounced._timer.start()
        return debounced
    return decorator