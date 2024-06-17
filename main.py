import datetime

#Create a dictionary of poker players
roster = {}

def print_roster():
    """Prints entire player roster"""
    print(f'current roster is: {roster}')

def roster_announcement():
    #code
    return


class Player:
    """Creates a player object to add to or remove from the roster"""
    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number
        roster[self._name] = self._phone_number

    def delete(self):
        if self._name in roster:
            roster.pop(self._name)
        else:
            print("No such player found.")

    def get_name(self):
        return self._name

    def get_phone_number(self):
        return self._phone_number


class Tournament:

    def __init__(self, date, time, host, address, buy_in, starting_stack, rebuy_period, add_on_price, add_on_stack, max_size):
        self._date = date
        self._time = time
        self._host = host
        self._address = address
        self._buy_in = buy_in
        self._starting_stack = starting_stack
        self._rebuy_period = rebuy_period
        self._add_on_price = add_on_price
        self._add_on_stack = add_on_stack
        self._max_size = max_size
        self._waitlist = []
        self._player_pool = []

    def the_invitation(self, starting_chip=True):
        '''Prompt the Twilio REST API and send the first message'''
        for player in roster:
            #call Twilio API
            if starting_chip==True:
                # Send the
                print(f"IT'S POKER TIME!! Our next tournament will be held on {self._date} and start at {self._time} and "
                      f"will be hosted by {self._host}.\n If you arrive before the start time you will receive an extra 1k " # Includes statement about bonus chip. removed "The address is {self._address}."
                      f"bonus chip.\nThis tournament's buy-in is set at {self._buy_in} for {self._starting_stack} chips. "
                      f"Rebuys will be available for the first {self._rebuy_period} at which point we take a break and offer"
                      f" add-ons for the low price of {self._add_on_price} for {self._add_on_stack} chips. \nIf you would "
                      f"like to join the tournament please reply 'YES' \nWe hope to see you there!\n\n\n For a list helpful "
                      f"commands reply 'HELP'\nTo opt of out the poker club and stop receiving invitations reply OPT OUT.")
            else:
                print(f"IT'S POKER TIME!! Our next tournament will be held on {self._date} at "
                  f"{self._time} and will be hosted by {self._host}.  "                                                     # Excludes statement about bonus chip. removed "The address is {self._address}."
                  f"\nThis tournament's buy-in is set at {self._buy_in} for "
                  f"{self._starting_stack} chips. Rebuys will be available for the first {self._rebuy_period} at which point"
                  f" we take a break and offer add-ons for the low price of {self._add_on_price} for {self._add_on_stack} "
                  f"chips. \nIf you would like to join the tournament please reply 'YES' \nWe hope to see you there! "
                  f"\n\n\n For a list helpful commands reply 'HELP'\nTo opt of out the poker club and stop receiving "
                  f"invitations reply 'OPT OUT'.")

    def cycle_to_pool(self):
        """
        Fills the player pool from the waitlist until the max size for the tournament is met.
        :return:
        """
        while len(self._player_pool) < self._max_size:
            if len(self._waitlist) == 0:
                return
                # Remove player from the waitlist
            player = self._waitlist.pop()
                # Add player to the player_pool
            self.add_player(player)#self._player_pool.append(other_player)
                # Print congrats message with event details. TEST
            print(player, "removed from waitlist and added to the player_pool. \n\nNew Player Pool:",             # TEST
                  self._player_pool, "\nNew Waitlist:", self._waitlist)                                                 # TEST

    def add_player(self, player):
        """
        Adds a player to player_pool if space is available. Otherwise, it adds the player to the waitlist.
        :param player:
        :return:
        """
        # code - code - code                                                                                            DO: Add Admin Authentication
        if len(self._player_pool) < self._max_size:
            self._player_pool.append(player)
            '''
            print(                                                                                                      #uncomment later
                "Congratulations, you are on the list for the next tournament! If, for any reason, you will not be "
                "able to make it to the tournament, please reply with 'Remove me'. This is very important so that "
                "those on the waitlist can take your spot. Any no shows will be taken seriously and are subject to "
                "expulsion from the poker club. Cheers and we can't wait to see you there!!!\n\n\n"
                f" Date: {self._date}\nStart Time: {self._time}\nHost: {self._host}\nAddress: {self._address}\nBuy in:"
                f" {self._buy_in} for {self._starting_stack} chips\nRebuys available for first: {self._rebuy_period}\n"
                f"Add Ons: {self._add_on_price} for {self._add_on_stack} chips\nConfirmed Players: "
                f"{[f"{player}" for player in self._player_pool]}\n{self._max_size - len(self._player_pool)} seats "
                f"vacant.\n\n\n\nFor a full list of commands reply HELP")
            '''
        else:
            self._waitlist.append(player)
            '''
            print(
                "Unfortunately the tournament is full but you have been added to the waitlist! Should a spot open up, "
                "you will be automatically bumped into the active player pool! If you cannot make it to the tournament"
                " please reply with 'Remove me' and you wil be taken off the waitlist. Cheers and we hope to see you "
                "there!\n\n\nFor a full list of commands reply HELP")
            '''

    def remove_player(self, player):
        """
        Removes a player from the tournament entirely and then calls cycle_to_pool to replace them.
        :param player:
        :return:
        """
        player_name = player.get_name()
        if player_name in self._waitlist:
            self._waitlist.remove(player_name)
        elif player_name in self._player_pool:
            self._player_pool.remove(player_name)
       # check if the player pool is less than the max size.
        self.cycle_to_pool()

    def announcement_player_pool(self, message):
        """Pushes a message to everyone in the player pool for the event."""
        #code
        return

    def announcement_all(self, message):
        """Pushes a message to everyone attending the event and on the waitlist."""
        #code
        return

    def set_reminder_schedule(self, schedule):                                                                          # Should the reminder schedule be a part of __init__ ?
        # sets the schedule for the reminders
        # send reminders as scheduled
        return

    def set_max_size(self, new_max):
        self._max_size = new_max
        self.cycle_to_pool()

    def get_max_size(self):
        return self._max_size

    def get_player_pool(self):
        if len(self._player_pool) == 0:
            print("The player pool is empty.")
            return
        else:
            return self._player_pool

    def get_waitlist(self):
        if len(self._waitlist) == 0:
            print("The waitlist is empty.")
            return
        else:
            return self._waitlist




#TESTS
Aaron = Player('Aaron Biderman' , '3105258146')
Alex = Player('Alex Slesers' , '8182376343')
Tom = Player('Tom Murphy' , '6462078201')
Martuan = Player('Martuan Cotton' , '3104985438')
Austin = Player('Austin Torelli' , '2036689902')
Buck = Player('Buck Ferguson' , '6035682381')
Elias = Player('Elias Cuevas' , '8312298200')
Jordan = Player('Jordan Pancer' , '8055513426')
Josh = Player('Josh Schauder' , '5403279526')
Lyle = Player('Lyle Feinberg' , '3104864487')
Christian = Player('Christian Marcial' , '3104031410')
Mark = Player('Mark Broadbent' , '2073187768')
Max = Player('Max Orlov' , '8188572532')
Miles = Player('Miles Hooper' , '3238935690')
Robert = Player('Robert Vardanian' , '8182074747')
Ron = Player('Ron Rosenberg' , '3107094682')


July = Tournament("2024-07-04", "18:00", "Aaron", "4238 Colbath Ave, Sherman Oaks, CA 91423", "$50", "5,000", "one hour", "$25", "3,000", 8)

#July.get_player_pool()

#July.get_waitlist()

def test_fill_players():
    for player in roster:
        July.add_player(player)

test_fill_players()

def test_empty_players(tourney):
    for player in tourney.get_waitlist():
        tourney.remove_player(player)
    for player in tourney.get_player_pool():
        tourney.remove_player(player)

test_empty_players(July)

July.cycle_to_pool()

print("Player pool is:",July.get_player_pool(), "And the number of players is:", len(July.get_player_pool()))
print("\n\n")
print("Waitlist is:", July.get_waitlist(), "And the number of players is:", len(July.get_waitlist()))

#July.set_max_size(16)

##FIX ME!!!!
July.remove_player(Robert)
print("\n\n",July.get_waitlist())

#July.the_invitation()

#print_roster()


