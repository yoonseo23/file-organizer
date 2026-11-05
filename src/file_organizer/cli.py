import typer

app = typer.Typer(add_completion=False)


@app.callback(invoke_without_command=True)
def main() -> None:
    """바탕화면과 다운로드 폴더의 파일을 규칙에 따라 정리합니다."""
    typer.echo("아직 정리 기능이 구현되지 않았습니다. 파일을 옮기지 않았습니다.")
