from typer.testing import CliRunner

from file_organizer.cli import app

runner = CliRunner()


def test_help_runs() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "정리" in result.output
