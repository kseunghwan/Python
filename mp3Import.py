class MusigBox():
  Box1 = ['사신레코드', '쿤청레인', '상상포레스트', '소년 브레이브',
   '데드 앤드 시크', '해질녘 에프터데이', '아야노의 행복이론', '칠드러 레코드']
  
  Box2 = ['(상록수)바람이 되고 싶었던 아이', '(상록수)호랑수월가', '여래아', 
  '마지막 세계의 왈츠', '혜성', '나선의달', '한여름 밤의 회선곡', '(하나사키)천년의 꽃']

  def __init__(self):
    self._Boxbox = ""
  
  @property #프로펄티 어노테이션 getter setter x -> property setter 보완성을위해서
  def Boxbox(self): #getter
    return self._Boxbox
  
  @Boxbox.setter # setter
  def Boxbox(self, value):
    self._Boxbox = value
