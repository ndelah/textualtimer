from textual.app import App, ComposeResult
from textual.widgets import Header

class StopwatchApp(App):
    """A Textual app that displays a stopwatch."""

    def compose(self) -> ComposeResult:
        """Create child widgets here."""

        yield Header()

if __name__ == "__main__":
    app = StopwatchApp()
    app.run()