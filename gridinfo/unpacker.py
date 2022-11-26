"""Utility code for unpacking data from the APIs."""

##############################################################################
def unpack_data( data: str, sep: str=" " ) -> dict[ str, str ]:
    """Unpack data coming from the text APIs.

    Args:
        data (str): The data to unpack.

    Returns:
        dict[ str, str ]: The unpacked data.
    """
    data_list = data.strip().split( sep )
    unpacked: dict[ str, str ] = {}
    while data_list:
        key, value, *data_list = data_list
        if key:
            unpacked[ key ] = value
    return unpacked

### unpacker.py ends here
