import socks

s = socks.socksocket() # Same API as socket.socket in the standard lib

# s.set_proxy(socks.SOCKS5, "localhost") # SOCKS4 and SOCKS5 use port 1080 by default
# Or
# s.set_proxy(socks.SOCKS4, "localhost", 4444)
# Or
s.set_proxy(socks.HTTP, "", 8000, True, "6LYUxQ", "")

# Can be treated like a regular socket object
s.connect(("www.google.com.com", 80))
s.sendall("HTTP")
print(s.recv(4096))