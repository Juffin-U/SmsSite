class SmsSerializer:
    def __init__(self,model):
        self.model = model

    def serialize(self):
        response = dict(content=self.model.content, message=self.model.message,)
        return response
