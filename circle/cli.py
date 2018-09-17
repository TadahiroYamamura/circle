import os
import os.path
import click
import circle


@click.group(invoke_without_command=False)
def cli():
  pass


@cli.command(help='edit question')
@click.argument('command', nargs=1)
@click.argument('values', nargs=-1)
def question(command, values):
  if command == 'list':
    session = circle.session()
    questions = session.query(circle.Question).all()
    for q in questions:
      print(str(q))
  elif command == 'add':
    questions = [circle.Question(question=x) for x in values]
    session = circle.session()
    session.add_all(questions)
    session.commit()
  elif command == 'delete':
    session = circle.session()
    session.query(circle.Question)\
           .filter(circle.Question.id.in_(values))\
           .delete(synchronize_session=False)
    session.commit()


@cli.command(help='circleの初期設定を行う')
def init():
  # データベースが存在した場合に削除
  if os.path.exists('database.sqlite'): os.remove('database.sqlite')
  circle.database.Base.metadata.create_all()
