# Flight

## mutations : 

token_auth(user, password)

verify_token(token)

refresh_token(user,password)

create_user(user,password,email)

add_flight(
    departure = String
    arrival = String
    price = Int
    airline = String
    duration = Int
    book_link = String)

update_flight (same as add_flight + id)

delete_flight (id)

## queries : 

users()

me()

flight([id], search:(departure or price))