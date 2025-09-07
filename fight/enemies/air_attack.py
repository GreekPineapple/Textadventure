class AirEnemy():
  name = "Luftgegner"
  lives = 110
  strength = 30
  drop = "vogel überreste"
  active_effects = []

  def apply_effect(self, effect):
      self.active_effects.append(effect)
      
  def remove_effect(self, effect):
      self.active_effects.remove(effect)