class Wizard():
  name = "Magier"
  lives = 135
  strength = 40
  drop = "wizard überreste"
  active_effects = []

  def apply_effect(self, effect):
      self.active_effects.append(effect)
      
  def remove_effect(self, effect):
      self.active_effects.remove(effect)