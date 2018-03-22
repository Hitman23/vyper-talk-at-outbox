#Warning, This Code has no been audited!
#Crowd fund

owner: public(address)
earned: public(wei_value)
phrase: bytes <= 100

# The constructor is only called on deployment
@public
def __init__():
    self.owner = msg.sender # The sender is the owner
    self.phrase = 'Hello World'

# A read only method. Reading from the EVM is free. Writing costs Gas
@public
@constant
def speak() -> bytes <= 100:
    return self.phrase

# Here we charge the sender to update the phrase
@public
@payable
def train(new_phrase: bytes <= 100):
    self.earned += msg.value
    self.phrase = new_phrase