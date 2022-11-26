"""The main screen for the application."""

##############################################################################
# Python imports.
from datetime import datetime

##############################################################################
# Textual imports.
from textual.app     import ComposeResult
from textual.screen  import Screen
from textual.binding import Binding
from textual.widgets import Header, Footer

##############################################################################
# Local imports.
from .card       import Card, DataPair
from .gridsurvey import concurrency_data, grid_size_data
from .sl_api     import grid_data

##############################################################################
class Main( Screen ):
    """The main screen for the application."""

    BINDINGS = [
        Binding( "escape", "app.quit", "Quit" ),
        Binding( "slash", "app.push_screen( 'region' )", "Region Search" )
    ]
    """The bindings for the main screen."""

    def compose(self) -> ComposeResult:
        """Compose the layout of the main screen.

        Returns:
            ComposeResult: The layout for the main screen.
        """

        def _unix_to_local( unix: str ) -> str:
            return str( datetime.utcfromtimestamp( int( unix or "0" ) ) )

        def _human_number( value: str ) -> str:
            try:
                return f"{int( value or '0' ):,}"
            except ValueError:
                return f"{float( value or '0' ):,}"

        def _linden_dollar( linden_dollar: str ) -> str:
            return f"L$ {( linden_dollar or '0.00' )} per USD"

        yield Header()
        yield Card(
            "Grid Info",
            DataPair( "Exchange Rate", "exchange_rate", cleaner=_linden_dollar ),
            DataPair( "In-world Last Updated", "inworld_updated_unix", cleaner=_unix_to_local ),
            DataPair( "In-World", "inworld", cleaner=_human_number ),
            DataPair( "Signups Last Updated", "signups_updated_unix", cleaner=_unix_to_local ),
            DataPair( "Signups", "signups", cleaner=_human_number ),
            DataPair( "Exchange Rate Last Updated", "exchange_rate_updated_unix", cleaner=_unix_to_local ),
            id = "grid-data"
        )
        yield Card(
            "Grid Concurrency",
            DataPair( "As Of", "date" ),
            DataPair( "Last Updated", "updated" ),
            DataPair( "Median", "median_online", cleaner=_human_number ),
            DataPair( "Mean", "mean_online", cleaner=_human_number ),
            DataPair( "Minimum", "min_online", cleaner=_human_number ),
            DataPair( "Maximum", "max_online", cleaner=_human_number ),
            id = "grid-concurrency"
        )
        yield Card(
            "Grid Size",
            DataPair( "Private Regions", "private", cleaner=_human_number ),
            DataPair( "Adult Regions", "adult", cleaner=_human_number ),
            DataPair( "Linden Lab Regions", "linden", cleaner=_human_number ),
            DataPair( "Mature Regions", "mature", cleaner=_human_number ),
            DataPair( "Linden Home Regions", "linden_homes", cleaner=_human_number ),
            DataPair( "General Regions", "pg", cleaner=_human_number ),
            DataPair( "Total Regions", "total", cleaner=_human_number ),
            DataPair( "Last Updated", "updated" ),
            id = "grid-size"
        )
        yield Footer()

    async def refresh_grid_info( self ) -> None:
        """Refresh the information about the grid."""
        self.query_one( "#grid-data", Card ).show( await grid_data() )

    async def refresh_grid_concurrency( self ) -> None:
        """Refresh the grid concurrency data."""
        self.query_one( "#grid-concurrency", Card ).show( await concurrency_data() )

    async def refresh_grid_size( self ) -> None:
        """Refresh the grid size data."""
        self.query_one( "#grid-size", Card ).show( await grid_size_data() )

    def on_mount( self ) -> None:
        """Set things in motion on mount"""
        self.call_after_refresh( self.refresh_grid_info )
        self.call_after_refresh( self.refresh_grid_concurrency )
        self.call_after_refresh( self.refresh_grid_size )

### main_screen.py ends here
