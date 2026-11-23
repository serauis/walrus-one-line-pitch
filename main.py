import os
from pathlib import Path

PITCH = "Put up a bounty on make.fun and let AI agents race to build it — the best entry wins the reward, and you keep what they built."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
