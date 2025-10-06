class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours = None, rest_days = None, email = None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        
        def get_hours(self):
        if self.hours is None:
            rd = 0 if self.rest_days is None else max(0, min(7, self.rest_days))
            self.hours = (7 - rd) * 8
        return self.hours

    
    def get_email(self):
        if not self.email:
            self.email = f"{self.name}@email.com"
        return self.email

    
    @classmethod
    def set_hourly_payment(cls, value):
        
        if value <= 0:
            raise ValueError("hourly_payment должен быть > 0")
        cls.hourly_payment = value

    
    def salary(self):
        hours = self.get_hours()          
        return hours * self.hourly_payment

