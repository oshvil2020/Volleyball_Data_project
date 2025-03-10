class Player:
    """Represents a volleyball player with attack and service stats."""
    def __init__(self, player_number: int):
        """
        :param player_number: Unique jersey number of the player
        """
        self.player_number = player_number
        self.attacks = []  # List of Attack objects
        self.services = []  # List of Service objects

    def add_attack(self, result: str, block_number: int, attack_type: str):
        """Adds an attack action for the player."""
        self.attacks.append(Attack(result, block_number, attack_type))

    def add_service(self, result: str, service_type: str):
        """Adds a service action for the player."""
        self.services.append(Service(result, service_type))

    def __str__(self):
        attack_summary = "\n".join(str(a) for a in self.attacks) if self.attacks else "No attacks recorded"
        service_summary = "\n".join(str(s) for s in self.services) if self.services else "No services recorded"
        return f"Player #{self.player_number}\nAttacks:\n{attack_summary}\n\nServices:\n{service_summary}"

