import random
import json
import operator


class Car:

    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return "{} {} with max speed of: {}".format(self.car, self.model, self.max_speed)

    def __int__(self):
        return int(self.max_speed)


class Driver:

    def __init__(self, name, car):
        self.name = name
        self.car = car
        self.crashed = False

    def crash(self, crash_chance):
        num = random.randint(1, 10)
        if crash_chance * 10 > num:
            self.crashed = True
            return True
        return False

    def __str__(self):
        return "{} drives {} {}".format(self.name, self.car.car, self.car.model)

    def __repr__(self):
        return self.__str__()


class Race():

    def __init__(self, drivers, crash_chance):
        self.drivers = drivers
        self.crash_chance = crash_chance
        self.race_results = {}

    def start_race(self):
        crashed_drivers = []
        finished_drivers = []
        for driver in self.drivers:
            if driver.crash(self.crash_chance):
                crashed_drivers.append(driver)
            else:
                finished_drivers.append(driver)
        finished_drivers_sorted = sorted(
            finished_drivers,
            key=lambda driver: driver.car.max_speed,
            reverse=True
        )
        for crashed_driver in crashed_drivers:
            self.race_results[crashed_driver.name] = 0
        for index in range(len(finished_drivers_sorted)):
            if index == 0:
                self.race_results[finished_drivers_sorted[index].name] = 8
            elif index == 1:
                self.race_results[finished_drivers_sorted[index].name] = 6
            elif index == 2:
                self.race_results[finished_drivers_sorted[index].name] = 4
            else:
                self.race_results[finished_drivers_sorted[index].name] = 0
        return self.race_results


class Championship:

    def __init__(self, name, races_count, drivers):
        self.name = name
        self.races_count = races_count
        self.drivers = drivers
        self.championship_results = {}

    def __str__(self):
        return 'Starting a new championship called {0} with {1} races. \nRunning {1} races ...'.format(
            self.name, self.races_count
        )

    def __repr__(self):
        return self.__str__()

    def print_race_results(self, results, race_number):
        print('Race #{}\n##### START #####'.format(race_number))
        for result in results:
            if result[1] != 0:
                print('{} - {}'.format(result[0], result[1]))
        print()
        for result in results:
            if result[1] == 0:
                print("Unfortunately, {} has crashed.".format(result[0]))
        print()

    def start_championship(self):
        for index in range(1, self.races_count + 1):
            race = Race(self.drivers, random.random())
            results = race.start_race()
            if index == 1:
                self.championship_results = results
            else:
                for driver in results:
                    self.championship_results[driver] += results[driver]
            sorted_results = sorted(results.items(), key=operator.itemgetter(1))
            sorted_results.reverse()
            self.print_race_results(sorted_results, index)
        return self.championship_results

    def print_championship_results(self, results):
        print('Total championship standings:\n')
        for result in results:
            if result[1] != 0:
                print('{} - {}'.format(result[0], result[1]))

    def top_3(self):
        sorted_championship_results = sorted(self.championship_results.items(), key=operator.itemgetter(1))
        sorted_championship_results.reverse()
        self.print_championship_results(sorted_championship_results)


class CLI:

    def __init__(self, drivers):
        self.drivers = drivers

    def start(self):
        print('Hello, PyRacer')
        print('Please, call command with the proper argument:')
        print('> start <name> <races_count>')
        print('> standings')
        print('> Exit')
        while True:
            command = input('>')
            command = command.split(' ')
            if command[0] == 'start':
                name = command[1]
                races_count = int(command[2])
                championship = Championship(name, races_count, self.drivers)
                print(championship)
                championship.start_championship()
                championship.top_3()
            elif command[0] == 'standing':
                pass
            elif command[0] == 'Exit':
                break


def main():
    with open('cars.json', 'r') as f:
        data = json.load(f)
    driver_car_data = data['people']
    drivers = []
    for driver_car in driver_car_data:
        car = Car(driver_car['car'], driver_car['model'], int(driver_car['max_speed']))
        driver = Driver(driver_car['name'], car)
        drivers.append(driver)
    cli = CLI(drivers)
    cli.start()

    # name = 'Ivo'
    # car_ = 'Opel'
    # model = 'Astra'
    # max_speed = 1800
    # car = Car(car_, model, max_speed)
    # driver = Driver(name, car)

    # name2 = 'Ivo2'
    # car2_ = 'Opel2'
    # model2 = 'Astra2'
    # max_speed2 = 1123
    # car2 = Car(car2_, model2, max_speed2)
    # driver2 = Driver(name2, car2)

    # name3 = 'Ivo3'
    # car3_ = 'Opel3'
    # model3 = 'Astra3'
    # max_speed3 = 111
    # car3 = Car(car3_, model3, max_speed3)
    # driver3 = Driver(name3, car3)

    # name4 = 'Ivo4'
    # car4_ = 'Opel4'
    # model4 = 'Astra4'
    # max_speed4 = 1156
    # car4 = Car(car4_, model4, max_speed4)
    # driver4 = Driver(name4, car4)

    # name5 = 'Ivo5'
    # car5_ = 'Opel5'
    # model5 = 'Astra5'
    # max_speed5 = 1122
    # car5 = Car(car5_, model5, max_speed5)
    # driver5 = Driver(name5, car5)

    # name6 = 'Ivo6'
    # car6_ = 'Opel6'
    # model6 = 'Astra6'
    # max_speed6 = 1129
    # car6 = Car(car6_, model6, max_speed6)
    # driver6 = Driver(name6, car6)

    # race = Race([driver, driver2, driver3, driver4, driver5, driver6], 0.2)
    # print(race.result())

if __name__ == '__main__':
    main()
