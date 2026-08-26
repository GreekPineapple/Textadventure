from textual.app import ComposeResult
from textual.widgets import Label, ProgressBar, Static
from textual.containers import Container

class VillainContainer(Container):
    
    def compose(self) -> ComposeResult:
        yield Label("Dauer bis Gegner angreift: ")
        yield ProgressBar(total=100, show_eta=False, id="progress_bar")
        yield Static("", id="villain")
        yield Static("Leben:", classes="live-sidebar")
