class Template:
    def __call__(self):
        return self.render()

    def render(self) -> str:
        raise NotImplementedError()
