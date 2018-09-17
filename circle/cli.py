import click
import circle.database
import circle.question


@click.group(invoke_without_command=False)
def cli():
  pass


@cli.command(help='edit question')
@click.option('--list', is_flag=True, help='show question list')
@click.option('--add', '-a', help='add question')
@click.option('--delete', '-d', help='remove question')
def question(list, add, delete):
  if list:
    click.echo('list questions.')
  elif add:
    click.echo('question added: ' + add)
  elif delete:
    click.echo('question deleted: ' + delete)
  else:
    click.help


@cli.command(help='circleの初期設定を行う')
def init():
  circle.database.Base.metadata.create_all()
