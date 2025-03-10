class Service:
    """Represents a service action in volleyball."""
    def __init__(self, result: str, service_type: str):
        """
        :param result: Outcome of the service (e.g., 'Ace', 'Fault', 'In Play')
        :param service_type: Type of service (e.g., 'Jump Serve', 'Float', 'Topspin')
        """
        self.result = result
        self.service_type = service_type

    def __str__(self):
        return f"Service: {self.service_type} | Result: {self.result}"

