"""Build the release package in dist/ from the app folder (course starter app)."""
import os
import shutil

os.makedirs("dist", exist_ok=True)
with open("VERSION") as f:
    version = f.read().strip()
with open(os.path.join("dist", "BUILD_INFO.txt"), "w") as f:
    f.write(f"Version {version}, built from commit {os.environ.get('GITHUB_SHA', 'local')}\n")
count = 0
for name in sorted(os.listdir("app")):
    if name.endswith(".py"):
        shutil.copy(os.path.join("app", name), "dist")
        count += 1
print(f"Packaged version {version}: {count} files in dist/")
