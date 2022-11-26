"""Utility code for getting data from an API endpoint."""

##############################################################################
# HTTPX imports.
import httpx

##############################################################################
async def get( url: str ) -> httpx.Response:
    """Get a response from a URL.

    Args:
        url (str): The URL to get a response from.

    Returns:
        httpx.Response: The response.
    """
    async with httpx.AsyncClient() as client:
        return await client.get( url, follow_redirects=True )

### getter.py ends here
