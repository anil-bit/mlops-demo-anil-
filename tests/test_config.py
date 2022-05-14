import pytest

class notinrange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 5
    with pytest.raises(notinrange):
       if a not in range(10,20):
          raise notinrange
    
