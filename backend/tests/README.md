# Testing

## 라이브러리

- 테스트 프레임워크 [pytest](https://docs.pytest.org/)
- django pytest 플러그인 [pytest-django](https://pytest-django.readthedocs.io/en/latest/)
- 테스트 커버리지 툴 [pytest-cov](https://pytest-cov.readthedocs.io/en/latest)

## 테스트

테스트를 실행하기 전 pytest, pytest-django, pytest-cov 패키지가 설치되어 있어야합니다. `backend` 디렉터리에서 `poetry install` 명령을 입력하여 설치해주세요.

### pytest

아래 명령어로 테스트를 실행할 수 있습니다.

```bash
pytest
```

### coverage

[커버리지](https://coverage.readthedocs.io/) - 현재 프로젝트에서 작성한 테스트 코드가 프로젝트 코드를 얼마나 커버하는지 측정할 수 있는 도구.

아래 명령어로 커버리지 결과를 생성할 수 있습니다.

```bash
# 테스트 실행
pytest --cov=apps

# 커버리지 측정 결과를 보여줍니다.
coverage report

Name                           Stmts   Miss  Cover
--------------------------------------------------
apps/__init__.py                   0      0   100%
apps/bookmark/__init__.py          0      0   100%
...
...

# 커버리지 측정 결과를 html파일로 저장합니다. ( htmlcov 폴더 생성됨 )
coverage html

Wrote HTML report to htmlcov/index.html
```
