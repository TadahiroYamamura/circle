import os
import os.path
import click
import circle


@click.group(invoke_without_command=False)
def cli():
  pass


@cli.command(help='edit question')
@click.option('--list', '-l', is_flag=True, help='show question list')
@click.option('--add', '-a', help='add question')
@click.option('--delete', '-d', help='remove question')
def question(list, add, delete):
  if list:
<<<<<<< HEAD
    session = circle.database.session()
    questions = session.query(circle.question.Question).all()
    for q in questions:
      print(str(q))
  elif add:
    q = circle.question.Question(question=add)
    session = circle.database.session()
    session.add(q)
    session.commit()
  elif delete:
    session = circle.database.session()
    q = session.query(circle.question.Question)\
               .filter(circle.question.Question.id == delete)\
               .first()
    if q:
      session.delete(q)
      session.commit()
=======
    session = circle.session()
    questions = session.query(circle.Question).all()
    for q in questions:
      print(str(q))
  elif add:
    q = circle.Question(question=add)
    session = circle.session()
    session.add(q)
    session.commit()
  elif delete:
    session = circle.session()
    session.query(circle.Question)\
           .filter(circle.Question.id == delete)\
           .delete()
    session.commit()
>>>>>>> master
  else:
    click.help


@cli.command(help='circleの初期設定を行う')
def init():
  # データベースが存在した場合に削除
  if os.path.exists('database.sqlite'): os.remove('database.sqlite')
  circle.database.Base.metadata.create_all()
