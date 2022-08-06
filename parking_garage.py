class ParkingGarage():
    def __init__(self, tickets, parkingSpaces, currentTicket =''):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.paid = ''
        
    def takeTicket(self, new_ticket):
        ticket = list(new_ticket.keys())[0]
        space = list(new_ticket.values())[0]
        if isinstance(new_ticket, dict) == False or ticket not in self.tickets or space not in self.parkingSpaces:
            print('Invalid Ticket')
        else:
            self.currentTicket = new_ticket
            self.tickets.remove(ticket)
            self.parkingSpaces.remove(space)
            
    def payForParking(self):
            self.paid = input('How much are you paying?')
            if self.paid:
                print('\nThank you, your ticket has been paid. \nPlease make sure to leave within 15 minutes to avoid further charges.')
                
    def leaveGarage(self):
        while self.paid == '':
            print('\nI am sorry, you have not paid for your ticket.')
            self.payForParking()
        else:
            print('\nThank You, have a nice day!')
            self.tickets.append(self.currentTicket.keys())
            self.parkingSpaces.append(self.currentTicket.values())
            self.currentTicket = ''
            
            
garage = ParkingGarage(['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4, 5])
garage.takeTicket({'a': 4})
garage.payForParking()
garage.leaveGarage()