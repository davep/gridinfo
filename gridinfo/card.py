"""Provides a widget that is a card of information with a title."""

##############################################################################
# Python imports.
from typing import Any, Callable

##############################################################################
# Textual imports.
from textual.app        import ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.widgets    import Static, Label
from textual.css.query  import NoMatches

##############################################################################
class DataPair( Horizontal ):
    """Provides a widget for displaying a data/value pair."""

    def __init__( self, title: str, id: str, initial: str="", cleaner: Callable[ [ str ], str ]=str ) -> None:
        """Initialise the data pair display.

        Args:
            title (str): The title for the data pair.
            id (str): The ID.
            initial (str, optional): Optional initial value to use.
        """
        super().__init__( id=id )
        self._title   = title
        self._initial = initial
        self._cleaner = cleaner
        self._value   = Label( self._cleaner( self._initial ) )

    def compose( self ) -> ComposeResult:
        """Compose the widget.

        Returns:
            ComposeResult: The layout of the widget.
        """
        yield Label( f"{self._title}:", classes="title" )
        yield self._value

    def value( self, new_value: str ) -> None:
        """Set the value for the data pair.

        Args:
            new_value (str): The new value to set.
        """
        self._value.update( self._cleaner( new_value ) )

##############################################################################
class Card( Vertical ):
    """Card widget with title and content."""

    def __init__( self, caption: str, *args: Any, can_focus: bool=False, **kwargs: Any ) -> None:
        """Initialise a card display."""
        container = Container( *args, classes="data" )
        container.can_focus = can_focus
        super().__init__(
            Static( caption, classes="caption" ),
            container,
            **kwargs,
        )

    def show( self, data: dict[ str, str ] ) -> None:
        """Show the data within the given panel.

        Args:
            data (dict[ str, str ]): The data to show.
        """
        for key, value in data.items():
            try:
                self.query_one( f"#{key}", DataPair ).value( value )
            except NoMatches:
                pass

### card.py ends here
