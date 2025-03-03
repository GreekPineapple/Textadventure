class OpenState:

  def __init__(self):
    self.name = "open"
    self.next_state = ActiveState

  def update(self):
    return self.next_state()

class ActiveState:

  def __init__(self):
    self.name = "active"
    self.next_state = DoneState

  def update(self):
    return self.next_state()

class DoneState:

  def __init__(self):
    self.name = "done"
    self.next_state = None

  def update():
    print("No more Updates available")
    