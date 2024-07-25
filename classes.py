import random

class Message:
    # The message that each process node creates is a tuple of the form (address, time-step, value)
    def __init__(self, address, value):
        self.time_step = 0
        self.address = address
        self.value = value
    
    def __str__(self) -> str:
        return f'Address: {self.address}, Time Step: {self.time_step}, Value: {self.value}'
    
    def update(self, last_broadcast):
        self.time_step += 1 # Increment the time step

        current_value = self.value

        if self.value < last_broadcast.value:
            # trying to push the values gradually to the maximum value
            self.value = random.randint(current_value, 100) # Randomly generate a new value between the old value and maximum value
        
        if self.value == last_broadcast.value:
            # If the values are the same, then increment the value by 1
            self.value += 1


class ProcessNode:
    # The message that each process node creates is a tuple of the form (address, time-step, value)
    def __init__(self, address):
        self.address = address
        self.message = None
    
    def set_first_message(self):
        self.value = random.randint(0, 20)
        self.message = Message(self.address, self.value)

    def update_node(self, broadcast):
        self.message.update(broadcast)


class UpTreeCompetition:
    # This class recieves the messages from the process nodes and then determines the winner of the competition
    def __init__(self):
        self.all_messages = []
        self.winner = None

    def get_winner(self):
        # The winner is determined by the message with the highest value
        if self.all_messages:
            winner = max(self.all_messages, key=lambda x: x.value)
            self.winner = winner
            return winner
    
    def add_message(self, message):
        self.all_messages.append(message)
    
    def get_all_messages(self):
        return self.all_messages
    
    def clear(self):
        self.all_messages = []
        self.winner = None