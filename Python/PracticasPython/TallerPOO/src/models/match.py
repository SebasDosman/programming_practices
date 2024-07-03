class Match:
    def __init__(self, id, date, id_home_team, id_away_team, id_stadium):
        self._id = id
        self._date = date
        self._id_home_team = id_home_team
        self._id_away_team = id_away_team
        self._id_stadium = id_stadium
    
    @property
    def id(self):
        return self._id
    
    @property
    def date(self):
        return self._date
    
    @property
    def id_home_team(self):
        return self._id_home_team
    
    @property
    def id_away_team(self):
        return self._id_away_team
    
    @property
    def id_stadium(self):
        return self._id_stadium
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @date.setter
    def date(self, date):
        self._date = date
    
    @id_home_team.setter
    def id_home_team(self, id_home_team):
        self._id_home_team = id_home_team
    
    @id_away_team.setter
    def id_away_team(self, id_away_team):
        self._id_away_team = id_away_team
    
    @id_stadium.setter
    def id_stadium(self, id_stadium):
        self._id_stadium = id_stadium
    
    def __str__(self):
        return f"{self._date} - {self._id_home_team} - {self._id_away_team} - {self._id_stadium}"