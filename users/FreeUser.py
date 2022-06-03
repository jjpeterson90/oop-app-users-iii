from User import User
class FreeUser(User):
    
    def __init__(self, name, email_address, drivers_license_number):
        super().__init__(name, email_address, drivers_license_number)
        self.post_count = 0
        self.max_post_count = 2
        self.my_posts = []
        
    def count_posts(self):
        return len(self.my_posts)
    
    def post(self, message):
        if (self.post_count < self.max_post_count):
            super().post(message)
            self.post_count += 1
        else:
            # prompt('please upgrade to premium to post more messages')
            pass
