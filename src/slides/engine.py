"""Backend engine"""

class SlideEngine:
    def __init__(self):
        self.default_content="# Slides Webapp"

        self.content=""

        self.reset_content()

    def set_content(self, content):
        self.content = content
    def reset_content(self):
        self.content = self.default_content