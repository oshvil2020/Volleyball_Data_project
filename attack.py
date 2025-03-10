class Attack:
    """Represents an attack action in volleyball."""
    def __init__(self, result: str, block_number: int, attack_type: str):
        """
        :param result: Outcome of the attack (e.g., 'Point', 'Blocked', 'Out')
        :param block_number: Number of blockers during the attack
        :param attack_type: Type of attack (e.g., 'Spike', 'Tip', 'Dump')
        """
        self.result = result
        self.block_number = block_number
        self.attack_type = attack_type

    def __str__(self):
        return f"Attack: {self.attack_type} | Result: {self.result} | Blockers: {self.block_number}"

