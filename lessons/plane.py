class PlaneTicket:

    depart_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float):
        self.depart_city = city_a
        self.arrival_city = city_b
        self.departure_time = depart
        self.ticket_cost = cost

    def __str__(self) -> str:
        info: str = f"From {self.depart_city} to {self.arrival_city} at {self.departure_time} costs ${self.ticket_cost}."
        return info
    
    def delay(self, delay_hours: int) -> None:
        self.departure_time += (delay_hours * 100)
        self.departure_time = self.departure_time % 24

    def discount(self, discount: float) -> None:
        self.ticket_cost = self.ticket_cost * (1 - discount)

def find_cheapest_ticket(tickets: list[PlaneTicket]) -> PlaneTicket:
    min_ticket: PlaneTicket = tickets[0]
    for t in tickets:
        if t.ticket_cost < min_ticket.ticket_cost:
            min_ticket = t
    return t