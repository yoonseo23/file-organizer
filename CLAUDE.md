# file-organizer

`~/Desktop`, `~/Downloads` 최상위 파일을 규칙에 따라 옮기는 macOS용 로컬 CLI 도구.
범위와 마일스톤의 기준 문서는 [docs/mvp.md](docs/mvp.md)다. 현재 단계: M0.

## 명령

```sh
uv sync                  # 개발 환경 설치
uv run pytest            # 테스트
uv run organize --help   # 개발 중 실행
uv tool install -e .     # 어디서나 쓸 수 있게 organize 명령 등록
```

## 구조

- `src/file_organizer/`: 패키지 코드. CLI 진입점은 `cli.py`의 `app`
- `tests/`: pytest 테스트
- `~/.config/file-organizer/`: 사용자의 `rules.yaml`과 `logs/moves.jsonl` (레포 밖)

## 안전 규칙

사용자의 실제 파일을 옮기는 도구이므로 아래 규칙은 예외 없이 지킨다.

- 삭제 코드를 두지 않는다. `unlink`, `rmtree`, `os.remove` 등을 쓰지 않고 이동만 한다.
- 테스트는 `tmp_path`에서만 돌린다. 실제 홈 디렉터리, `~/Desktop`, `~/Downloads`를 건드리지 않는다.
  경로는 코드에 고정하지 말고 인자로 주입해 테스트할 수 있게 한다.
- 덮어쓰지 않는다. `shutil.move`는 목적지에 같은 이름의 파일이 있으면 덮어쓸 수 있으므로,
  이동 전에 충돌을 직접 확인하고 `_1`을 붙인다.
- 이동하기 전에 로그를 먼저 기록한다.
- 정리 대상은 `sources` 폴더의 최상위 파일만이다. 하위 폴더, 디렉터리, 심볼릭 링크는 건드리지 않는다.
- 목적지 폴더가 없으면 만들지 말고 경고한다.

## 구현 시 주의

- macOS의 한글 파일명은 NFD 형식일 수 있다. 키워드와 접두사를 비교하기 전에 파일명과 규칙을
  모두 NFC로 정규화하고, NFD 파일명 테스트를 함께 작성한다. 실제 이동에는 원래 파일명을 쓴다.
- `organize`는 어느 폴더에서나 실행되므로 현재 작업 디렉터리 기준 상대 경로를 쓰지 않는다.

## 범위

`docs/mvp.md`의 Won't 항목(launchd, watchdog, LLM 분류, 리네이밍 등)은 요청 없이 구현하지 않는다.
