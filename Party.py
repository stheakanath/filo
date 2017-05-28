#
#   Party. We just invented the most lit data structure y'all.
#
#   The party data structure. FILO. First to the party, last out of the party.
#   We know how it rolls.
#   
#   Created by Dipsikha Halder (@dipsikha) and Sony Theakanath (@stheakanath)
#   Authored on May 28, 2017
#

class Party(object):
    def __init__(self):
        """Let's initialize this party people!
        """
        self.__attendees = []
        self.__size_of_party = 0

    def arrive(self, attendee):
        """First to the party? You'll be the last to leave. That's how we go.
        FILO algorithm. 
        
        Arguments:
            attendee {[object]} -- the Human, Starfish, Zork. 
        """
        self.__attendees.add(attendee)
        self.__size_of_party += 1

    def leave(self):
        """Took too many shots, time to call an Uber home. 
        
        [description]
        
        Returns:
            attendee {[object]} -- the Human, Starfish, Zork. 
        """
        if self.__size_of_party == 0:
            print "Party is over people!"
            return 
        attendee = self.__attendees[self.__size_of_party - 1]
        del self.__attendees[self.__size_of_party - 1]
        self.__size_of_party -= 1
        return attendee

    def tfti(self, attendee):
        """@Aditya Chopra. Google isn't that far from us. 
        
        Arguments:
            attendee {[object]} -- the Human, Starfish, Zork. 

        Returns:
            boolean -- whether you can complain or not. 
        """
        if attendee in self.__attendees:
            print "You have been invited."
            return True
        else:
            print "TFTI"
            # @Pranay Patni
            return False

    def party_is_over(self):
        """The popo came to shut your party down. 
        
        Returns:
            attendees {[list]} -- the Human, Starfish, Zork as a list.
        """
        self.__size_of_party = 0
        return self.__attendees 
