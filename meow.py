def newp():
    doc = "The newp property."
    def fget(self):
        return self._newp
    def fset(self, value):
        self._newp = value
    def fdel(self):
        del self._newp
    return locals()
newp = property(**newp())
