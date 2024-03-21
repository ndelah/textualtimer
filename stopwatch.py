from textual.app import App, ComposeResult

class StopwatchApp(App):
    """A Textual app that displays a stopwatch."""

if __name__ == "__main__":
    app = StopwatchApp()
    app.run()