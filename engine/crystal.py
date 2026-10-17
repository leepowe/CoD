class Crystal:

    def __init__(self, name, element, purity, threshold):
        self.name = name
        self.element = element
        self._purity = purity
        self.threshold = threshold

    @property
    def purity(self):
        return self._purity

    @purity.setter
    def purity(self, new_value):
        if new_value < 0:
            raise ValueError("Purity cannot be negative.")
        self.purity = new_value