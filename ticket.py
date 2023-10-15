import random


def generate_ticket(src, dest, passenger_count):
    tickets = []
    for i in range(1, passenger_count + 1):
        ticket = "AL1" + ":" + src[0:3] + ":" + dest[0:3] + ":" + f"{100 + i}"
        tickets.append(ticket)
    return tickets


print(generate_ticket("Denver", "Phoenix", 5))
