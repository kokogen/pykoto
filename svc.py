messages = {
    1: {"from": "Kostya", "to": "Sveta", "body": "Hi!"},
    2: {"from": "Andrew", "to": "Sveta", "body": "Hello"},
    3: {"from": "Kostya", "to": "Andrew", "body": "Privet!"},
}


class MessageSvc:
    def get_by_id(self, id):
        return messages[id]

    def get_by_from(self, from_txt):
        return filter(lambda e: e[1] == from_txt, messages.items())

    def get_by_to(self, to_txt):
        return filter(lambda e: e[2] == to_txt, messages.items())

    def get_all(self):
        return list(messages.values())

    def put(self, msg):
        print(msg)
        max_id = max(messages.keys()) + 1
        print(max_id)
        messages[max_id] = msg
        return max_id

    def delete(self, id):
        m = messages[id].copy()
        del messages[id]
        return m

message_service = MessageSvc()
