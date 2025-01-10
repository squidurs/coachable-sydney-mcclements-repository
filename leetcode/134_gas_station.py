from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Determines the starting gas station index from which a vehicle can
        complete a circular route around all gas stations.

        Args:
            gas (List[int]): A list where gas[i] represents the amount of gas
                             available at the ith gas station.
            cost (List[int]): A list where cost[i] represents the amount of gas
                              required to travel from the ith station to the
                              next station.

        Returns:
            int: The index of the starting gas station if a circular route
                 can be completed. Returns -1 if it is not possible.
        """

        if sum(gas) < sum(cost):
            return -1

        fuel = 0
        start = 0

        for i, (gas_amount, cost_amount) in enumerate(zip(gas,cost)):
            fuel += gas_amount - cost_amount
            if fuel < 0:
                start = i + 1
                fuel = 0

        return start
    