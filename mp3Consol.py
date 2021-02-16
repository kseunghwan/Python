import puls

if __name__ == "__main__":
  
  setting = puls.MusigBox()

  while(1):

    print('앨범을 선택해주세요 (1집/2집/종료).\n')

    User = input()

    if (User == '1집'):
      
      setting.Boxbox = '1집'

      print(setting.Boxbox,'을 불러냅니다.\n')

      print(setting.Box1,'중 원하는곡을 입력해주세요 :)\n')

      User = input()

      for i in range(0, int((setting.Box1.__len__()-1))):
        
        if (User == setting.Box1[i]):  

          print(setting.Box1[i],'곡이 지금 실행중입니다 :)\n')

          print('곡을 중지하시겠습니까? (Yes/No)\n')

          User = input()

          if ('Yes' == User):

            print('곡을 중지했습니다 :)\n')
            
            break

          elif ('No' == User): 

            print('다른곡을 실행하겠습니다 :)\n')

    elif (User == '2집'):
      
      setting.Boxbox = '2집'

      print(setting.Boxbox,'을 불러냅니다.\n')

      print(setting.Box2,'중 원하는곡을 입력해주세요 :)\n')
      
      User = input()
      
      for i in range(0, int((setting.Box2.__len__()-1))):

        if (User == setting.Box2[i]):

          print(setting.Box2[i],'곡이 지금 실행중입니다 :)\n')

          print('곡을 중지하시겠습니까? (Yes/No)\n')

          User = input()

          if ('Yes' == User):

            print('곡을 중지했습니다 :)\n')
            
            break

          elif ('No' == User): 

            print('다른곡을 실행하겠습니다 :)\n')

        else:
          print('다시입력해주세요 :) \n')

    elif (User == '종료'):

      print('종료했습니다 :)\n')

      break

    else:

      print('다시입력해주세요 :) \n')

    continue
