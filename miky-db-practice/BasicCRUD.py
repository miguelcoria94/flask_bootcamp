from BasicModelApp import db, Puppy

my_puppy = Puppy("Rufus", 5)
db.session.add(my_puppy)
db.session.commit()

## print(my_puppy)

# all_puppies = Puppy.query.all()
# print(all_puppies)

# puppy_one = Puppy.query.get(1)

# puppy_sam = Puppy.query.filter_by(name="Sammy")

# first_puppy = Puppy.query.get(1)
# first_puppy.age = 10
# db.session.add(first_puppy)
# db.session.commit()


second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()


