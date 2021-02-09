from BasicModelApp import db, Puppy

my_puppy = Puppy("Rufus", 5)
db.session.add(my_puppy)
db.session.commit()

## print(my_puppy)

