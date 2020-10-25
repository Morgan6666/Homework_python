#Задание №1
class TraficLight:
    def __init__(self):
        color_res = ["Красный", "Жёлтый", "Зелёный"]
        self.color_res = color_res
    def running(self):            
        import time
        for colors in self.color_res:
            if colors == "Красный":
                time.sleep(7)
                print("\033[31m {}".format(colors))
            elif colors == "Жёлтый":
                time.sleep(2)
                print("\033[33m {}".format(colors))
            elif colors == "Зелёный":
                time.sleep(5)
                print("\033[32m {}".format(colors))
                
    
    Svetofor_1 = TraficLight()
Svetofor_1.running()



#Задание №2
class Road:
    def __init__(self,lenght,width, mass_1, sm):
        self.__lenght = lenght
        self.__width = width
        self.__mass_1 = mass_1
        self.__sm = sm
    def mass(self):
        print(f"Масса асфальта необходимая для покрытия жд полтна равна:{(self.__width * self.__lenght * self.__mass_1 * self.__sm)//1000}.т")
        
 road = Road(20,5000,25,5)
road.mass()
road._Road__lenght


#Задание №3:
class Worker:
    def __init__(self,name,surname,position):
        self.name = name
        self.surname = surname
        self.position = position
        income = {"wage":200000, "bonus":30000}
        self.income = income
        
    
class Position(Worker):
    def get_full_name(self):
        print(f"Ваше полное имя-{self.name} {self.surname}\nДолжность-{self.position}")
     
    def get_total_income(self):
        total = 0
        for val in self.income.values():
            total += val
        print(f"Ваш полный зарабаток составляет-{total}")
            
            
worker_1 = Position("Денис","Байрамкулов","Биоинформатик")
worker_1.get_full_name()
worker_1.get_total_income()




#Задание №4
class Car:
    def __init__(self, speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        if self.name == "Mazda":
            print("Машина тронулась-","\033[32m{}".format(self.name))
        elif self.name == "Lamborhini":
            print("Машина тронулась-","\033[31m{}".format(self.name))
        elif self.name == "Mustang":
            print("Машина тронулась-","\033[37m{}".format(self.name))
        elif self.is_police == True:
            print("Машина тронулась-","\033[34m{}".format("Police!"))
        
    def stop(self):
        print(f"{self.name} остановилась!")
        
    def turn(self):
        turn_1 = ["Право","Лево"]
        for t in turn_1:
            print(f"{self.name} повернула на {t}")
    
    def show_speed(self):
        if self.speed > 60:
            print(f"Ай-ай-ай ваша скорость {self.speed}.км/ч,что выше положенной")
        else:
            print(f"Ваша скорость соcтавляет {self.speed}.км/ч")
    def i_am_pilice(self):
        if is_police == True:
            print("Я здесь закон!")
        else:
            print("Я не полиция!")

class TownCar(Car):
    pass

class WorkCar(Car):
    pass

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass  
    
                  
                  

car_1 = TownCar(70, "Black", "Mazda", False)
car_1.go()
car_1.show_speed()
car_1.turn()
car_1.stop()
car_1 = PoliceCar(40, "Blue-Red", "Police", True)
car_1.go()
car_1.turn()
car_1.show_speed()
car_1 = WorkCar(70, "Black", "Mazda", False)
car_1.go()
car_1.show_speed()




#Задание №5
class Stetionery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print("Запус отрисовки")
        
    def my_title(self):
        print(f"Привет,меня зовут {title}")

        
class Pen(Stetionery):
    pass


class Handle(Stetionery):
    pass

class Pencill(Stetionery):
    pass
    
