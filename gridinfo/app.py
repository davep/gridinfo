"""The main application class for the app."""

##############################################################################
# Textual imports.
from textual.app import App

##############################################################################
# Local imports.
from .main_screen import Main
from .region_info import RegionInfo

##############################################################################
class GridInfo( App[ None ] ):
    """TUI app for showing information about the Second Life grid."""

    CSS_PATH = "gridinfo.css"
    """The name of the CSS file for the app."""

    TITLE = "Grid Information"
    """str: The title of the application."""

    SCREENS = {
        "main": Main,
        "region": RegionInfo
    }
    """The collection of application screens."""

    def on_mount( self ) -> None:
        """Set up the application on startup."""
        self.push_screen( "main" )

##############################################################################
def run() -> None:
    """Run the application."""
    GridInfo().run()

### app.py ends here
