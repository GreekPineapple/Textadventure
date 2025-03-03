class OpenState:

  def __init__(self):
    self.name = "open"
    self.next_state = ActiveState

  def update(self):
    return self.next_state

  def execute():
    pass

class ActiveState:

  def __init__(self):
    self.name = "active"
    self.next_state = DoneState

  def update(self):
    return self.next_state


  def execute():
    pass

class DoneState:

  def __init__(self):
    self.name = "done"
    self.next_state = None

  def update():
    print("No more Updates available")

  def execute():
    pass