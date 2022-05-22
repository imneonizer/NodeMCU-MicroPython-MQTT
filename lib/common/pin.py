from machine import Pin as BoardPin

mapping = {
    'ESP8266': {
        "D0": 16,
        "D1": 5,
        "D2": 4,
        "D3": 0,
        "D4": 2,
        "D5": 14,
        "D6": 12,
        "D7": 13,
        "D8": 15,
    }    
}

class Pin(BoardPin):
    def __init__(self, name, board='ESP8266', init=False, *args, **kwargs):
        # initialize the pin based on pin number or
        # pin name as printed on node mcu board
        self.board = board
        if isinstance(name, str):
            self.id = mapping[board.upper()][name.upper()]
            self.name = name  
        elif isinstance(name, int):
            self.id = name
            self.name = self.get_name_by_id(self.id)

        if init:    
            super().__init__(self.id, *args, **kwargs)
     
    def init(self, *args, **kwargs):
        super().__init__(self.id, *args, **kwargs)
        return self
    
    def get_name_by_id(self, val):
        for key, value in mapping[self.board].items():
         if val == value:
             return key
         return 'unknown'