'''
1845. Seat Reservation Manager
Medium

180

15

Add to List

Share
Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

'''


class SeatManager(object):
    from heapq import heappush, heappop, heapify

    def __init__(self, n):
        """
        :type n: int
        """
        self.seat = list(range(1, n + 1))

    def reserve(self):
        """
        :rtype: int
        """
        if self.seat:
            return self.heappop(self.seat)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        self.heappush(self.seat, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)