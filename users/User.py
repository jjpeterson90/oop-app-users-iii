class User:
    
    message_board = []
    
    def __init__(self, name, email_address, drivers_license_number):
        self.name = name
        self.email = email_address
        self.license = drivers_license_number
        
    def __str__(self):
        return f'{self.name}, {self.email}, {self.license}'
    
    def post(self, message):
        self.my_posts.append(message)
        User.message_board.append({self.name: message})
    
    def delete_my_last_post(self):
        for post in range(len(User.message_board), 0, -1):
            index = post-1
            if self.name in User.message_board[index]:
                del User.message_board[index]
                break
    
    def see_all_posts():
        return User.message_board