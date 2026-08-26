from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Container

class PlayerContainer(Container):
    
    def compose(self) -> ComposeResult:
        yield Static("Wähle einen Angriff", id="player")
        yield Static("Leben:", classes="live-sidebar")
