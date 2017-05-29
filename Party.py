"""Party. We just invented the most lit data structure y'all.

The party data structure. FILO. First to the party, last out of the party. We
know how it rolls.

Created by Dipsikha Halder (@dipsikha), Sony Theakanath (@stheakanath), and
Aditya Chopra (@adichopra).

Authored on May 28, 2017.

TODO(adichopra): Add support for afterparties.
TODO(adichopra): Add unit tests. There ain't no party without unit tests.
"""

class Party(object):
    def __init__(self, max_people=10):
        """Let's initialize this party people!"""
        self.__attendees = []

        # The number of people that can be at the party before a noise
        # complaint is filed.
        self.__max_people = max_people

    def num_attendees(self):
        """How lit is the party?

        Returns:
        	An integer representing the number of people at the party.
        """
        return len(self.__attendees)

    def arrive(self, attendee):
        """First to the party? You'll be the last to leave. That's how we go.
        FILO algorithm.

        Args:
            attendee {[object]} -- the Human, Starfish, Zork.

        Returns:
        	True if successful, False otherwise.
        """
        if self.num_attendees() == self.__max_people:
        	self.party_is_over()
        	return False
        self.__attendees.add(attendee)
        return True

    def leave(self):
        """Took too many shots, time to call an Uber home.

        Returns:
            attendee {[object]} -- the Human, Starfish, Zork.
        """
        if self.num_attendees() == 0:
            print "Party is over people!"
            return None
        attendee = self.__attendees[self.num_attendees() - 1]
        del self.__attendees[self.num_attendees() - 1]
        return attendee

    def leave(self, attendee):
        """Your friend is gone, walk them home.

        Args:
            attendee {[object]} -- the Human, Starfish, Zork.

        Returns:
            attendee {[object]} -- the Human, Starfish, Zork.
        """
        if attendee not in self.__attendees:
            print attendee + " is not at the party, silly!"
            return None
        self.__attendees.remove(attendee)
        return attendee

    def tfti(self, attendee):
        """@adichopra. Google isn't that far from us.

        Args:
            attendee {[object]} -- the Human, Starfish, Zork.

        Returns:
            True if attendee is at the party, False otherwise.
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
        attendees = self.__attendees
        self.__attendees = []
        return attendees
