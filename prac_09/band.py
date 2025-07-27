class Band:
    """Band class for managing a list of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band, including its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band's list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument or needing one."""
        return "\n".join(musician.play() for musician in self.musicians)