from transformers import pipeline

from Models.ClassifiedTicket import ClassifiedTicketModel
from Models.Ticket import TicketModel

classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')


def classify(ticket: TicketModel) -> ClassifiedTicketModel:
    classification = classifier(ticket.description, ticket.candidates)
    return ClassifiedTicketModel(
        title=ticket.title,
        description=ticket.description,
        classification=dict(zip(classification['labels'], classification['scores']))
    )