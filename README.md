# CPSC 535 
## Project: Electric Car Traveler

### Project Statement:
We all know that electric cars do not have as large a range as gas cars, so they need periodic recharge. Assume that one needs to travel a large distance, that cannot be done in one charge, so one needs to stop to recharge and continue. But some of the chargers may not function, in case you need to drive back to the previous city and re-charge there. To simplify, let’s assume that you drive along I-10 from Santa Monica, CA to Tallahassee, FL Your stops are Phoenix, Tucson, Las Cruces, El Paso, San Antonio, Houston, Baton Rouge, New Orleans, Gulfport, Mobile, Tallahassee. You are in Tucson and the charge station doesn't work, so you need to go back to Phoenix to recharge.
Given a capacity C in miles that represents the maximum number of miles your electric car can drive, n cities and (n-1) distances between two consecutive cities, design an algorithm that outputs the list L of cities where one need to stop and charge the car such that:
L is if minimum length among all possible list of cities
the starting city, which is the first city, is the first element of L
The destination city, which is the last city, is the last element of L
If j and k are two consecutive cities in L, then when the car is in city j, the car is able to drive to city k and back to the city before city k, in case the charge station in city k is broken. 
The capacity C in miles is not fixed, but one can assume that is a positive integer between 250 and 350.
The number of cities n is not fixed, but you can assume that it is greater than 3 and less than 20. 
The distance between cities is a positive integer and always less than C/2 and greater than 10.

### Summary:

Electric cars needs to be charged periodically. Say if we want to travel long distance from Santa Monica, CA to Tallahassee,FL. If we charge the car at the starting city we don’t get it till our destination. It has to be recharged in some other stops on the way. If any of the charge station doesn’t work, we should be able to travel back to the previous station. Analgorithm to get the list of cities to be halted to get the car recharged till it reaches the destination can be found in the Report.

### Group members:
Jeevika Yarlagadda - jeevikayarlagadda@csu.fullerton.edu

Kevin Huang - kevin80710@csu.fullerton.edu
