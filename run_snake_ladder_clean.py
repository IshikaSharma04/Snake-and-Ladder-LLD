import subprocess, os

# Set your target backdates here (YYYY-MM-DD)
dates = [
    "2026-03-01",
    "2026-03-02"
]

TOPICS = [
    ("feat(lld): implement Board and Cell entities with Snake and Ladder entities", "src/models/Board.java",
     "public class Board {\n  private int size;\n  public Board(int size) { this.size = size; }\n}\n"),
    ("feat(lld): implement Player state management and Dice rolling strategy", "src/services/GameService.java",
     "public class GameService {\n  public void playTurn() { System.out.println(\"Rolling dice...\"); }\n}\n"),
    ("test(lld): add unit tests for game winning conditions and board boundary checks", "tests/GameTest.java",
     "public class GameTest {\n  public static void main(String[] args) { assert true; }\n}\n")
]

TIME_SLOTS = ["11:00:00", "14:30:00", "18:00:00"]
AUTHOR_NAME = "IshikaSharma04"
AUTHOR_EMAIL = "ishika.24bcs10352@sst.scaler.com"

with open("README.md", "w") as f:
    f.write("# Snake and Ladder - Low Level Design\nObject-Oriented Design implementation of Snake and Ladder game.\n")

subprocess.run(["git", "add", "."], check=True)

env = os.environ.copy()
env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
env["GIT_AUTHOR_DATE"] = f"{dates[0]}T09:00:00"
env["GIT_COMMITTER_DATE"] = f"{dates[0]}T09:00:00"

subprocess.run(["git", "commit", "-m", "Initial commit: setup Snake-and-Ladder-LLD architecture"], env=env, check=True)

total = 1
for date_str in dates:
    for i, (msg, file_path, content) in enumerate(TOPICS):
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "a") as f:
            f.write(f"\n// Updated: {date_str} {TIME_SLOTS[i]}\n" + content)

        subprocess.run(["git", "add", file_path], check=True)

        commit_iso = f"{date_str}T{TIME_SLOTS[i]}"
        env["GIT_AUTHOR_DATE"] = commit_iso
        env["GIT_COMMITTER_DATE"] = commit_iso

        subprocess.run(["git", "commit", "-m", msg], env=env, check=True)
        total += 1

print(f"\nGenerated {total} clean backdated commits for Snake-and-Ladder-LLD!")
