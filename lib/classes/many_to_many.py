import re

class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise ValueError(
                'Name cannot be re-assigned.'
            )
        elif isinstance(name, str) and len(name) > 2:
            self._name = name
        else:
            raise TypeError(
                'Name must be a string of 3 or more characters.'
            )

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        people_and_visits = {}

        for visitor in self.visitors():
            people_and_visits[visitor] = visitor.total_visits_at_park(self)
        
        if people_and_visits:
            top_visits = max(people_and_visits.values())
            top_list = [person for person, visits in people_and_visits.items() if visits == top_visits]
            return top_list[0] if len(top_list) == 1 else top_list
        else:
            return None

    @classmethod
    def most_visited(cls):
        parks_and_visits = {}

        for park in cls.all:
            if park.total_visits() > 0:
                parks_and_visits[park] = park.total_visits()
        
        if parks_and_visits:
            top_visits = max(parks_and_visits.values())
            top_list = [park for park in cls.all if park.total_visits() == top_visits]
            return top_list[0] 
            # if len(top_list) == 1 else top_list
        else:
            return None
        

class Trip:
    all = []
    date_pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s(0?[1-9]|[12]\d|3[01])(st|nd|rd|th)$"
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        
        if isinstance(start_date, str) and re.match(type(self).date_pattern, start_date):
            self._start_date = start_date
        else:
            raise ValueError(
                'Start date must be in the format "Month Day", such as "January 1st" or "April 4th".'
                )
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and re.match(type(self).date_pattern, end_date):
            self._end_date = end_date
        else:
            raise ValueError(
                'End date must be in the format "Month Day", such as "January 1st" or "April 4th".'
                )
    
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise TypeError(
                'Visitor must be of the Visitor class.'
            )
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise TypeError(
                'National Park must be of the NationalPark class.'
            )

class Visitor:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and len(name) < 16:
            self._name = name
        else:
            raise TypeError(
                'Namer must be a string between 1 and 15 characters.'
            )
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])