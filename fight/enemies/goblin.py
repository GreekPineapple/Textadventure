class Goblin():
  name = "Goblin"
  lives = 90
  strength = 35
  drop = "goblin überreste"
  active_effects = []

  def apply_effect(self, effect):
      self.active_effects.append(effect)
      
  def remove_effect(self, effect):
      self.active_effects.remove(effect)
