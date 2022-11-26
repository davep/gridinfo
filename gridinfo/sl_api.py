"""Utility code for talking to the Second Life API."""

##############################################################################
# Python imports.
from tempfile import NamedTemporaryFile

##############################################################################
# Rich Pixels imports.
from rich_pixels import Pixels

##############################################################################
# Local imports.
from .getter   import get
from .unpacker import unpack_data

##############################################################################
async def grid_data() -> dict[ str, str ]:
    """Get the main data about the grid.

    Returns:
        dict[ str, str ]: The main grid information.
    """
    return unpack_data( ( await get( "https://api.secondlife.com/datafeeds/homepage.txt" ) ).text, "\n" )

##############################################################################
async def region_map( map_uuid: str, size: int=40 ) -> Pixels:
    """Given a map UUID, get the texture.

    Args:
        map_uuid (str): The UUID of the map to acquire.
        size (int, optional): The size of a side of the resulting map tile.

    Returns:
        Pixels: The ``Pixel`` image.
    """
    with NamedTemporaryFile() as img:
        map_data = await get( f"http://secondlife.com/app/image/{map_uuid}/2" )
        img.write( map_data.content )
        return Pixels.from_image_path( img.name, resize=( size, size ) )

### sl_api.py ends here
