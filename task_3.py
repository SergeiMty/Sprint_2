class PointsForPlace:
    
    def __init__(self):
        self.points = 0

    def get_points_for_place(self, place: int) -> float:
        self.points = 0
        if place > 100:
            print("Баллы начисляются только первым 100 участникам")
        elif place < 1:
            print("Спортсмен не может занять нулевое или отрицательное место")
        else:
            self.points = 101 - place
        return self.points


class PointsForMeters:
    
    def __init__(self):
        self.points = 0  

    def get_points_for_meters(self, meters: int) -> float:
        self.points = 0
        if meters < 0:
            print("Количество метров не может быть отрицательным")
        else:
            self.points = meters * 0.5
        return self.points


class TotalPoints(PointsForPlace, PointsForMeters):
    """Итоговые очки = за место + за метры."""
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)
        self.total = 0 

    def get_total_points(self, place: int, meters: int) -> float:
        place_pts = self.get_points_for_place(place)
        meters_pts = self.get_points_for_meters(meters)
        self.total = place_pts + meters_pts
        return self.total



