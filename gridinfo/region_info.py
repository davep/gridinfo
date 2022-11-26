"""Provides a screen for viewing region information."""

##############################################################################
# Textual imports.
from textual.app        import ComposeResult
from textual.screen     import Screen
from textual.widgets    import Header, Footer, Input, Button, Static
from textual.containers import Horizontal
from textual.binding    import Binding

##############################################################################
# Local imports.
from .card       import Card, DataPair
from .gridsurvey import region_info
from .sl_api     import region_map

##############################################################################
class RegionInfo( Screen ):
    """Screen for looking up information about a specific region."""

    BINDINGS = [ Binding( "escape", "app.pop_screen", "Close" ) ]
    """Bindings for this screen."""

    def compose( self ) -> ComposeResult:
        """Compose the display of the screen.

        Returns:
            ComposeResult: The main layout for the application.
        """
        yield Header()
        yield Horizontal(
            Input( placeholder="Second Life Region Name" ),
            Button( "Search", disabled=True ),
            id="region-input"
        )
        yield Card(
            "Region Details",
            DataPair( "Name", "name", cleaner=lambda name: name.replace( "+", " " ) ),
            DataPair( "Status", "status", cleaner=str.capitalize ),
            DataPair( "X", "x" ),
            DataPair( "Y", "y" ),
            DataPair( "Access", "access", cleaner=str.capitalize ),
            DataPair( "Estate", "estate" ),
            DataPair( "First Seen", "firstseen" ),
            DataPair( "Last Seen", "lastseen" ),
            DataPair( "Objects Map", "objects_uuid" ),
            DataPair( "Terrain Map", "terrain_uuid" ),
            DataPair( "Updated", "updated" ),
            DataPair( "UUID", "region_uuid" ),
            id      = "region-info"
        )
        yield Card( "Map", Static( id="map" ), id="map-wrap", can_focus=True )
        yield Footer()

    def on_mount( self ) -> None:
        """Set the app up once the DOM is loaded."""
        self.set_focus( self.query_one( "#region-input Input", Input ) )

    def on_input_changed( self, event: Input.Changed ) -> None:
        """React to the region name being modified.

        Args:
            event (Input.Changed): The event for the change.
        """
        self.query_one(  "#region-input Button", Button ).disabled = not bool( event.input.value.strip() )
        self.query_one( Input ).remove_class( "bad-region" )

    async def update_region_data( self ) -> None:
        """Update the region data."""
        if "region_uuid" in ( data := await region_info( self.query_one( Input ).value ) ):
            self.query_one( "#region-info", Card ).show( data )
            self.query_one( "#map", Static ).update( await region_map( data[ "objects_uuid" ], 80 ) )
        else:
            self.app.bell()
        self.query_one( Input ).set_class( "region_uuid" not in data, "bad-region" )

    async def on_input_submitted( self, _: Input.Submitted ) -> None:
        """React to input being submitted.

        Args:
            event (Input.Submitted): The event for the submit.
        """
        await self.update_region_data()

    async def on_button_pressed( self, _: Button.Pressed ) -> None:
        """React to the search button being pressed.

        Args:
            event (Button.Pressed): The event for the press.
        """
        await self.update_region_data()

### region_info.py ends here
