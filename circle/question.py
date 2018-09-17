from sqlalchemy import Column, String, Integer
from circle.database import Base


class Question(Base):
  __tablename__ = 'questions'

  id = Column(Integer, primary_key=True)
  question = Column(String, nullable=False)

  def __str__(self):
    return '{}: {}'.format(self.id, self.question)
