"""
This type stub file was generated by pyright.
"""

"""Utilities for safely pickling exceptions."""
unwanted_base_classes = (Exception, BaseException, object)
STRTOBOOL_DEFAULT_TABLE = { 'false': False,'no': False,'0': False,'true': True,'yes': True,'1': True,'on': True,'off': False }
def subclass_exception(name, parent, module):
    """Create new exception class."""
    ...

def find_pickleable_exception(exc, loads=..., dumps=...):
    """Find first pickleable exception base class.

    With an exception instance, iterate over its super classes (by MRO)
    and find the first super exception that's pickleable.  It does
    not go below :exc:`Exception` (i.e., it skips :exc:`Exception`,
    :class:`BaseException` and :class:`object`).  If that happens
    you should use :exc:`UnpickleableException` instead.

    Arguments:
        exc (BaseException): An exception instance.
        loads: decoder to use.
        dumps: encoder to use

    Returns:
        Exception: Nearest pickleable parent exception class
            (except :exc:`Exception` and parents), or if the exception is
            pickleable it will return :const:`None`.
    """
    ...

def itermro(cls, stop):
    ...

def create_exception_cls(name, module, parent=...):
    """Dynamically create an exception class."""
    ...

def ensure_serializable(items, encoder):
    """Ensure items will serialize.

    For a given list of arbitrary objects, return the object
    or a string representation, safe for serialization.

    Arguments:
        items (Iterable[Any]): Objects to serialize.
        encoder (Callable): Callable function to serialize with.
    """
    ...

class UnpickleableExceptionWrapper(Exception):
    """Wraps unpickleable exceptions.

    Arguments:
        exc_module (str): See :attr:`exc_module`.
        exc_cls_name (str): See :attr:`exc_cls_name`.
        exc_args (Tuple[Any, ...]): See :attr:`exc_args`.

    Example:
        >>> def pickle_it(raising_function):
        ...     try:
        ...         raising_function()
        ...     except Exception as e:
        ...         exc = UnpickleableExceptionWrapper(
        ...             e.__class__.__module__,
        ...             e.__class__.__name__,
        ...             e.args,
        ...         )
        ...         pickle.dumps(exc)  # Works fine.
    """
    exc_module = ...
    exc_cls_name = ...
    exc_args = ...
    def __init__(self, exc_module, exc_cls_name, exc_args, text=...) -> None:
        ...
    
    def restore(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    @classmethod
    def from_exception(cls, exc):
        ...
    


def get_pickleable_exception(exc):
    """Make sure exception is pickleable."""
    ...

def get_pickleable_etype(cls, loads=..., dumps=...):
    """Get pickleable exception type."""
    ...

def get_pickled_exception(exc):
    """Reverse of :meth:`get_pickleable_exception`."""
    ...

def b64encode(s):
    ...

def b64decode(s):
    ...

def strtobool(term, table=...):
    """Convert common terms for true/false to bool.

    Examples (true/false/yes/no/on/off/1/0).
    """
    ...

def jsonify(obj, builtin_types=..., key=..., keyfilter=..., unknown_type_filter=...):
    """Transform object making it suitable for json serialization."""
    ...

def raise_with_context(exc):
    ...
