from app import db

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text, nullable = False)

  def __repr__(self):
    return(f"Todo('{self.id}', '{self.content}')")


