class Browser:
    def __init__(self):
        self.history = []
        self.layout = []

    def go(self, url):
        self.history.append(url)
        self.layout.clear()

    def back(self):
        if len(self.history) > 1:
            self.layout.append(self.history.pop())
            return self.history[-1]

    def forward(self):
        if self.layout:
            self.history.append(self.layout.pop())
            return self.history[-1]

    def printAll(self):
        print(*self.history)


browser = Browser()
browser.go("https://google.com")
browser.go("https://ukdw.ac.id")
browser.go("https://facebook.com")
print(browser.back()) #output: https://ukdw.ac.id
print(browser.back()) #output: https://google.com
print(browser.forward()) #output: https://ukdw.ac.id
browser.go("https://twitter.com") 
browser.printAll() #output: https://google.com https://ukdw.ac.id https://twitter.com