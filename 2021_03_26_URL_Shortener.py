import random, string

class URL_Shortener:
    def __init__(self, length):
        self.length = length
        self.lookup = {}
        self.lookup_url = {}

    def shorten(self, url):
        if url in self.lookup_url:
            return self.lookup_url[url]
        else:
            mini_url = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(self.length)) 
            self.lookup[mini_url] = url
            self.lookup_url[url] = mini_url
            return mini_url

    def expand(self, mini_url):
        return self.lookup[mini_url] if mini_url in self.lookup else None
                
if __name__ == "__main__":
    minifier = URL_Shortener(6)

    drizly_url = minifier.shorten('www.drizly.com/home')
    print(drizly_url)
    assert minifier.shorten('www.drizly.com/home') == drizly_url
    print(minifier.expand(drizly_url))
