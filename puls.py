def __init__(self):
    self._Boxbox = ""
  
  @property #프로펄티 어노테이션 getter setter x -> property setter 보완성을위해서
  def Boxbox(self): #getter
    return self._Boxbox
  
  @Boxbox.setter # setter
  def Boxbox(self, value):
    self._Boxbox = value
