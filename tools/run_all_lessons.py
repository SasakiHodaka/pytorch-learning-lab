"""Execute every completed lesson in filename order."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"


def main() -> int:
    lesson_files = sorted(LESSONS.glob("[0-9][0-9]_*/*.py"))
    failures: list[Path] = []

    for lesson in lesson_files:
        relative = lesson.relative_to(ROOT)
        print(f"\n=== {relative} ===", flush=True)
        result = subprocess.run([sys.executable, str(lesson)], cwd=ROOT, check=False)
        if result.returncode != 0:
            failures.append(relative)

    print(f"\nExecuted {len(lesson_files)} lessons.")
    if failures:
        print("Failed lessons:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("All lessons passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
