import sys 
import os
import random
import itertools 
import time
from datetime import datetime

import typer

from .util import parse_numbers, repr_numbers, graceful

app = typer.Typer()


@graceful
def ask(x, y):
    try:
        a = int(input(f"{x} × {y} = "))
    except ValueError:
        print("数字で答えよう\n")
        a = ask(x, y)
    return a


@graceful
def kuku(left, right, ordered):

    combi = list(itertools.product(left, right))
    mistake = 0  
    while combi:
        if not ordered:
            random.shuffle(combi)
        wrong = []
        for _x, _y in combi:
            a = ask(_x, _y)

            if a == _x * _y:
                print("正解!!\n")
            else:
                print("不正解 (T_T)\n")
                wrong.append((_x, _y))
    
        mistake += len(wrong)
        combi = wrong

    return mistake

def write_record(record, path):
    path = os.path.expanduser(path)
    if os.path.exists(path) and os.path.isdir(path):
        raise FileExistsError # Is this appropriate?

    create_new = False if os.path.isfile(path) else True
    
    with open(path, mode='a') as f:
        if create_new:
            f.write("start,mistake,elapsed,left,right\n")
        f.write(",".join([str(_) for _  in record]) + "\n")


@app.command()
def log():
    """
    Show records
    """
    typer.echo("Show records. Not implemented yet.")
    


@app.command()
def graph():
    """
    Show graph
    """
    typer.echo("Show graph. Not implemented yet.")


@app.command()
@graceful
def start(left: str = typer.Argument("1-9", 
            help="left operand. (Eg.) Single integer 1, Range 2-5, or Combined 3-4/8/7"),
          right: str = typer.Argument("1-9", 
            help="right operand. (Eg.) Single integer 1, Range 2-5, or Combined 3-4/8/7"),
          ordered: bool = typer.Option(False, "--order", "-o", 
            help="Do not shuffle."),
          file: str = typer.Option("~/.kuku_record", "--file", "-f", 
            help="File to save records.")):
    """
    掛け算ドリル
    """
    left = parse_numbers(left)
    right = parse_numbers(right)

    # Main part
    typer.echo("-" * 20)
    typer.echo("掛け算ドリル".center(15))
    typer.echo("-" * 20 + "\n")
    typer.echo(f"🎬 はんいは {left} ✕ {right}、全部で{len(left) * len(right)}問です。")
    
    while True:
        key = input("😁 準備ができたらエンターキーをおしてください。\n😣 やめるときは Ctrl をおしながらエンター\n") 
        if key == "":
            typer.echo("Start!! \n")
            break

    # For logging. 
    begin_time = datetime.now().strftime("%Y-%m-%d %H:%m")        
    
    # Stopwatch starts.
    start = time.time()

    # Main kuku drill.
    mistake = kuku(left, right, ordered)

    # Stopwatch stops.
    elapsed = time.time() - start

    print("おわり!")
    if mistake == 0:
        print("全問正解です！ 🏆")
    else:
        print(f"{mistake}回まちがえました。 😩")

    print(f"{round(elapsed, 1)}秒かかりました。")

    # Write records
    left = repr_numbers(left)
    right = repr_numbers(right)
    write_record((begin_time, mistake, elapsed, left, right), file)

    return sys.exit(0)


if __name__ == "__main__":
    app()