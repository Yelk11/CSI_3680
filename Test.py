import webbrowser

class FoodSwitch:
    
    def day(self, dayOfWeek):

        default = "Invalid Website"

        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return webbrowser.open('https://www.allrecipes.com/')

 

    def case_2(self):
        return webbrowser.open('https://www.foodnetwork.com/')

 

    def case_3(self):
        return webbrowser.open('https://www.thekitchn.com/')

   

    def case_4(self):
       return webbrowser.open('https://www.food.com/')

 

    def case_5(self):
        return webbrowser.open('https://www.seriouseats.com/')

   
my_switch = FoodSwitch()

print (my_switch.day(1))

print (my_switch.day(3))

