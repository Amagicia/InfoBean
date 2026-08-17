import os
from collections import defaultdict

def generate_report(directory="."):
    folder_stats = defaultdict(int)
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith('.')]  # ignore hidden folders
        py_files = [f for f in files if f.endswith('.py')]
        if py_files:
            folder_stats[root] = len(py_files)
    
    return folder_stats

stats = generate_report(".")

print("\n" + "┌" + "─"*63 + "┐")
print(f"│ {'PYTHON FILES REPORT':^61} │")
print("├" + "─"*63 + "┤")
print(f"│ {'Folder':<48} {'Files':>8} │")
print("├" + "─"*63 + "┤")

total = 0
for folder, count in sorted(stats.items()):
    rel_path = os.path.relpath(folder, ".")
    if rel_path == ".":
        rel_path = "(root)"
    # Truncate long paths
    if len(rel_path) > 46:
        rel_path = "..." + rel_path[-43:]
    print(f"│ {rel_path:<48} {count:>8} │")
    total += count

print("├" + "─"*63 + "┤")
print(f"│ {'TOTAL':<48} {total:>8} │")
print("└" + "─"*63 + "┘")