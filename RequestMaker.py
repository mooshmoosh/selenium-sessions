import random

class RequestMaker:
    def __init__(self, character_list=None):
        if character_list is None:
            character_list = [chr(x) for x in range(ord('A'), ord('Z') + 1)] + [str(x) for x in range(0, 10)]
        self.search_terms = []
        for x in character_list:
            for y in character_list:
                for z in character_list:
                    self.search_terms.append(x + y + z)
        random.shuffle(self.search_terms)

    def __call__(self, cookies):
        pass
