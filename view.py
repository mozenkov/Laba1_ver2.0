class View:
    @staticmethod
    def main_menu():
        View.zabor()
        print "1)Choose tour operator"
        print "2)Choose country"
        print "3)Add tour operator"
        print "4)Delete tour operator"
        print "5)Add country"
        print "6)Delete country"
        View.zabor()

    @staticmethod
    def addTour():
        print "Add tour operator"
        print "Write name of tour operator"

    @staticmethod
    def deleteTour():
        print "Delete tour operator"
        print "Write name of tour operator"

    @staticmethod
    def addCountry():
        print "Add country"
        print "Write name of country"

    @staticmethod
    def deleteCountry():
        print "Delete country"
        print "Write name of country"

    @staticmethod
    def success_msg():
        print "All shit done"

    @staticmethod
    def zabor():
        print "|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|"

    @staticmethod
    def error_msg():
        print "Something is broken..."
        print " >:C "

