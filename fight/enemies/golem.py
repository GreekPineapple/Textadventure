class Golem():
  name = "Erdgolem"
  lives = 140
  strength = 50
  drop = "golem überreste"
  active_effects = []

  def apply_effect(self, effect):
      self.active_effects.append(effect)
      
  def remove_effect(self, effect):
      self.active_effects.remove(effect)