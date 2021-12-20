# """the file is for practicing dataclass function"""
# class ManualCommont:
#     def __init__(self, id:int, text:str):
#         self.id: int = id
#         self.text: str = text
    
#     def __repr__(self):
#         return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)

#     def __eq__(self, other):
#         if other.__class__ is self.__class__:
#             return (self.id, self.text) == (other.id, other.text)
#         else:
#             return NotImplemented

#     def __ne__(self, other):
#         result = self.__eq__(other)
#         if result is NotImplemented:
#             return NotImplemented
#         else:
#             return not result
    
#     def __hash__(self):
#         return hash((self.__class__, self.id, self.text))

from dataclasses import dataclass, astuple, asdict
import inspect

@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str

def main():
    comment = Comment(1, "I just subscribed!")
    print(comment)

if __name__ == '__main__':
    main()

