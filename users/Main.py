from FreeUser import FreeUser
from PremiumUser import PremiumUser
from User import User


Alice = PremiumUser('Alice', 'email@address.com', '111-222-3333')
Dale = FreeUser('Dale', 'Dale123@email.com', '111-555-1234')

Alice.post("Alice post 1")
Dale.post("Dale post 1")
Alice.post("Alice post 2")
Dale.post("Dale post 2")
Alice.post("Alice post 3")
Dale.post("Dale post 3")

print(User.message_board)