import json
import sys
from collections import defaultdict

class MarkingPositionMonitor:
    # tracking information
    symbol_to_position = defaultdict(int)
    id_to_msg = {}

    def __init__(self):
        pass

    def init_event(self, msg, msg_type, msg_id):
        if msg_type == 'NEW':
            symbol = msg['symbol']
            self.id_to_msg[msg_id] = msg
        elif msg_id in self.id_to_msg:
            symbol = self.id_to_msg[msg_id]['symbol']
        order = self.id_to_msg[msg_id]
        return order, symbol
    
    def on_event(self, message):
        msg = json.loads(message)
        msg_id = msg['order_id']
        msg_type = msg['type']
        order, symbol = self.init_event(msg, msg_type, msg_id)

        # now perform specific actions for each type of message
        if msg_type == 'NEW':
            side = msg['side']
            quantity = msg['quantity']
            # when making a new sell, update right away
            if side == 'SELL':
                # update now
                self.symbol_to_position[symbol] -= int(quantity)
        elif msg_type == 'ORDER_REJECT':
            # revert the sell when rejected
            if order['side'] == 'SELL':
                self.symbol_to_position[symbol] += int(order['quantity'])
        elif msg_type == 'CANCEL_ACK':
            if order['side'] == 'SELL':
                # if a selling order is cancelled, revert to remaining quantity
                self.symbol_to_position[symbol] += order['quantity']
        elif msg_type == 'FILL':
            filled = msg['filled_quantity']
            remaining = msg['remaining_quantity']
            if order['side'] == 'BUY':
                # once the order has been filled, update a buying order (we don't have to worry about reverting here)
                self.symbol_to_position[symbol] += int(filled)
            elif order['side'] == 'SELL':
                # when selling, update the amount remain so we know how much to revert if the order is cancelled
                order['quantity'] = remaining
        elif msg_type == 'CANCEL_REJECT':
            # just ignore this one
            pass
        elif msg_type == 'CANCEL':
            # just ignore this one
            pass
        if msg_type == 'ORDER_ACK':
            # just ignore this one
            pass

        position = self.symbol_to_position[symbol]
        return position

monitor = MarkingPositionMonitor()
for line in sys.stdin:
    print(monitor.on_event(line.strip()))