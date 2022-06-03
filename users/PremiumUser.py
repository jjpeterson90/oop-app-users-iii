from User import User
class PremiumUser(User):
    
    def __init__(self, name, email_address, drivers_license_number):
        super().__init__(name, email_address, drivers_license_number)
        self.my_posts = []
    
# Your PremiumUser class goes here