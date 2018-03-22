#Warning, This Code has no been audited!
#SACCO

#Setup private variables (only callable from within the contract)
savers: {sender: address, value: wei_value}[int128]
nextFunderIndex: int128
beneficiary: address
deadline: timestamp
refundIndex: int128
timelimit: timedelta

# Setup global variables
@public
def __init__(_beneficiary: address, _goal: wei_value, _timelimit: timedelta):
    self.beneficiary = _beneficiary
    self.deadline = block.timestamp + _timelimit
    self.timelimit = _timelimit

# Collect money from savers.
@public
@payable
def participate():
    assert block.timestamp < self.deadline
    nfi: int128 = self.nextFunderIndex
    self.saver[nfi] = {sender: msg.sender, value: msg.value}
    self.nextFunderIndex = nfi + 1

@public
def payout():
    assert block.timestamp >= self.deadline and self.balance < self.goal
    ind: int128 = self.refundIndex
    for i in range(ind, ind + 30):
        if i >= self.nextFunderIndex:
            self.refundIndex = self.nextFunderIndex
            return
        send(self.saver[i].sender, self.saver[i].value)
        self.saver[i] = None
    self.refundIndex = ind + 30