from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def sandbox(ctx):
    ctx.run("python3 src/sandbox.py", pty=True)

@task
def apikey(ctx):
    ctx.run("python3 src/apikey.py", pty=True)
