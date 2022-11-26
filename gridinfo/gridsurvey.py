"""Utility code for building URLs for the grid survey."""

##############################################################################
# Python imports.
from urllib.parse import quote

##############################################################################
# Local imports.
from .getter   import get
from .unpacker import unpack_data

##############################################################################
def gridsurvey( query: str ) -> str:
    """Return the URL for the given Grid Survey query.

    Args:
        query (str): The query to make.

    Returns:
        str: The full URL for the query.
    """
    return f"http://api.gridsurvey.com/{query}"

##############################################################################
async def concurrency_data() -> dict[ str, str ]:
    """Get the concurrency data about the grid.

    Returns:
        dict[ str, str ]: The grid's concurrency data.
    """
    return unpack_data( " ".join(
        ( await get( gridsurvey( "metricquery.php?metric=concurrency" ) ) ).text.split( "\n" )
    ) )

##############################################################################
async def grid_size_data() -> dict[ str, str ]:
    """Get the grid size data about the grid.

    Returns:
        dict[ str, str ]: The grid's size data.
    """
    return unpack_data( " ".join(
        ( await get( gridsurvey( "metricquery.php?metric=grid_size" ) ) ).text.split( "\n" )
    ) )

##############################################################################
async def region_info( region: str ) -> dict[ str, str ]:
    """Get information about a given region.

    Args:
        region (str): The region to get the information for.

    Returns:
        dict[ str, str ]: The data for that region.
    """
    return unpack_data( " ".join(
        ( await get( gridsurvey( f"simquery.php?region={quote( region )}" ) ) ).text.split( "\n" )
    ) )

### gridsurvey.py ends here
