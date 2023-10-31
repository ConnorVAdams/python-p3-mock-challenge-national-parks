#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

p_1 = NationalPark("Yosemite")
p_2 = NationalPark("Rocky Mountain")
vis_1 = Visitor("Steve")
t_1 = Trip(vis_1, p_1, "May 5th", "May 9th")
t_2 = Trip(vis_1, p_1, "May 20th", "May 27th")
t_3 = Trip(vis_1, p_2, "January 5th", "January 20th")

vis_2 = Visitor("Bill")
t_1 = Trip(vis_2, p_1, "May 1st", "May 9th")
t_2 = Trip(vis_2, p_1, "June 20th", "August 27th")
t_3 = Trip(vis_2, p_1, "January 5th", "January 20th")

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    ipdb.set_trace()
