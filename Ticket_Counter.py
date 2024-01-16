class Hall:
    def __init__(self, row, col, hall_no) -> None:
        self.__row = row+1
        self.__col = col+1
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

    def entry_show(self, id, movieName, time):
        show = (id, movieName, time)
        self.__show_list.append(show)

        self.__seats[id] = []
        for i in range(self.__row):
            col = []
            for j in range(self.__col):
                col.append(0)
            self.__seats[id].append(col)

    def view_show_list(self):
        print(".................................................................................")
        print('Present  movie show running')
      
        for show in self.__show_list:
            print(f'Movie ID: {show[0]} Movie Name: {show[1]} Time: {show[2]}')
        print(".................................................................................")
    def view_available_seats(self, id):
        ck = 0
        for show in self.__show_list:
            if show[0] == id:
                ck = 1
                for i in range(self.__row):
                    if i != 0:
                        for j in range(self.__col):
                            if j != 0:
                                print(self.__seats[id][i][j], end = ' ')
                        print()
        if ck == 0:
            print(f'Your ID is invalid, Please Enter vaild ID')

    def book_seats(self, id, ticket_list):
        ck = 0
        for show in self.__show_list:
            if show[0] == id:
                ck = 1
                for i in range(len(ticket_list)):
                    x = ticket_list[i][0]
                    y = ticket_list[i][1]
                    if x >= self.__row or y >= self.__col:
                        print('sorry seat no is invalid')
                    elif x <= 0 or y <= 0:
                        print('sorry seat no is invalid')
                    else:
                        if(self.__seats[id][x][y] == 0):
                            self.__seats[id][x][y] = 1
                            print(f'Your seat {x, y} is successfully booked for the show {id}')
                        else:
                            print(f'seat {x, y} is already booked')
        if ck == 0:
            print(f'ID: {id} is invalid, Please Enter correct ID')


class  Star_Cinema(Hall):
    __hall_list = []

    def __init__(self) -> None:
        pass
    
    def entry_hall(self, hall):
        self.__hall_list.append(hall)
    @property
    def hall_list(self):
        return self.__hall_list
    
x = 6
y = 6
hall = Hall(x, y, 1)
star_cinema = Star_Cinema()
star_cinema.entry_hall(hall)

hall.entry_show(1, 'kabi khushi kabi gham', '10:00 AM Date: 16.1.2024 ')
hall.entry_show(2, 'Jawan', '7:00 PM Date: 16.1.2024 ')


while True:
    print()
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SETS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    n = int(input("\nENTER OPTION: "))
    if n < 0 or n > 4:
        print("\nSorry! Please Enter valid option: ")
    elif n == 4:
        break
    elif n == 1:
        for show in star_cinema.hall_list:
            show.view_show_list()
    elif n == 2:
        id = int(input("Enter show ID: "))
        hall.view_available_seats(id)
    elif n == 3:
        id = int(input("Enter show ID: "))
        no = int(input("Enter number of ticket: "))
        ticket_list = []

        for i in range(no):
            R = int(input('Enter row: '))
            C = int(input('Enter col: '))
            print()
            ticket_list.append((R, C))
        hall.book_seats(id, ticket_list)
        
        
            