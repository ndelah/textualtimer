from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer, Static, Button

class Stopwatch(Static):
    """A stopwatch widget"""

    def compose(self) -> ComposeResult:
        """Create child widget"""

        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        
        


class StopwatchApp(App):
    """A Textual app that displays a stopwatch."""

    BINDINGS = [
        ("d","toggle_dark","Toggle dark mode")
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets here."""

        yield Header()
        yield Footer()
        yield ScrollableContainer(Stopwatch(),Stopwatch(),Stopwatch())

    def action_toggle_dark(self) -> None:
        """Toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()