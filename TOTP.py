import hmac, time, struct, hashlib

# generating a TOTP without pyotp

# via https://datatracker.ietf.org/doc/html/rfc6238 -> tysm IETF
def generate_totp(email):
    key = (email + "HENNGECHALLENGE003").encode()
    # print("bruh ", key)
    interval = int(time.time()) // 30
    # print(interval)
    msg = struct.pack(">Q", interval) # (format, interval) -> big endian (>) and 64-bits (Q) 
    # print(msg)
    h = hmac.new(key, msg, hashlib.sha512).digest() # HMAC-SHA-512 object fingerprint ready to get hashed -> digest() creates the hash value in ASCII hex -> 'trigger'
    # print(h)
    o = h[-1] & 0x0F # dynamic truncation -> ty stack overflow and forums
    # print(o)
    code = (struct.unpack(">I", h[o:o+4])[0] & 0x7FFFFFFF) % (10 ** 10) # we want it unsigned and 10 digits long
    return f"{code:010d}"

email = "your_email_here"
print(generate_totp(email))
