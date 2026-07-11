#!/usr/bin/env python3
"""Known high-stakes fact-status contradictions must not coexist in the master document."""
from pathlib import Path
import sys

MASTER = Path(__file__).resolve().parents[1] / "반영구_문신_법령_모니터링_마스터.md"

def main():
    text = MASTER.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if "무작위표본검사" in line]
    unverified = [
        line for line in lines
        if any(term in line for term in ("교차확인되지", "사실 단정 보류", "미확정"))
    ]
    confirmed = [
        line for line in lines
        if any(term in line for term in ("교차확인 완료", "확정", "추가 시행", "시행]"))
    ]
    if unverified and confirmed:
        print("ERROR: 문신용 염료 무작위표본검사의 미확인/확정 상태가 동시에 존재합니다.")
        for line in unverified + confirmed:
            print(" -", line[:240])
        return 1
    print("fact consistency check passed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
