from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer

class StopwatchApp(App):
    """A Textual app that displays a stopwatch."""

    BINDINGS = [
        ("d","toggle_dark","Toggle dark mode")
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets here."""

        yield Header()
        yield Footer()
        yield ScrollableContainer()

    def action_toggle_dark(self) -> None:
        """Toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()