from fastapi import FastAPI

from Models.ClassifiedTicket import ClassifiedTicketModel
from Models.Ticket import TicketModel
from AI.classifier import classify

app = FastAPI()


@app.post("/classify_ticket")
async def classify_ticket(ticket: TicketModel) -> ClassifiedTicketModel:
    return classify(ticket)