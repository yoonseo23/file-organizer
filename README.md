# file-organizer

`~/Desktop`, `~/Downloads`의 최상위 파일을 명령 한 번으로, 규칙에 따라, 되돌릴 수 있게 정리하는 macOS용 CLI 도구입니다.

> **현재 상태: 개발 초기(M0).** 프로젝트 뼈대만 있으며, `organize`를 실행해도 아직 파일을 옮기지 않습니다. 진행 계획은 [docs/mvp.md](docs/mvp.md)에 있습니다.

## 요구 사항

- macOS
- [uv](https://docs.astral.sh/uv/) (`brew install uv`로 설치)

iCloud의 "데스크탑 및 문서" 동기화를 켠 환경에서는 테스트하지 않았습니다.

## 설치

```sh
git clone https://github.com/yoonseo23/file-organizer.git
cd file-organizer
uv tool install -e .
organize --help
```

`organize`를 찾을 수 없다고 나오면 `uv tool update-shell`을 실행한 뒤 터미널을 다시 여세요.

## 개발

```sh
uv sync
uv run pytest
uv run organize --help
```
