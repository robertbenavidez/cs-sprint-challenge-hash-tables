#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    route = []
    next_destination = cache["NONE"]
    route.append(next_destination)
    while next_destination != "NONE":
        next_destination = cache[next_destination]
        route.append(next_destination)

    return route


if __name__ == "__main__":
    tickets = [
        Ticket("NONE", "PDX"),
        Ticket("PDX", "DCA"),
        Ticket("DCA", "NONE"),
    ]

    locations = reconstruct_trip(tickets, len(tickets))
    print(locations)
