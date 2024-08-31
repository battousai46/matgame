def str_to_bool(val: str) -> bool:
    """
    Converts a string to boolean.

    Raises ValueError if val is not a string or is not a valid value.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "1", "on"):
        return True
    elif val in ("n", "no", "f", "false", "0", "off"):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))
