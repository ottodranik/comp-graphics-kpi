from graphics import GraphicsObject

class GraphicsGroup(GraphicsObject):
  def __init__(self):
    super().__init__(options=[])
    self.components = []

  def draw(self, graphwin):
    for component in self.components:
      component.draw(graphwin)
    return self

  def move(self, dx, dy):
    for component in self.components:
      component.move(dx, dy)

  def add_in_group(self, component):
    if isinstance(component, GraphicsObject):
      self.components.append(component)
