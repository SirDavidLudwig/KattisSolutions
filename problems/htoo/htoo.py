import collections, re

atoms = collections.defaultdict(int)

molecule, n = input().strip().split()
n = int(n)
for atom in re.findall(r"[A-Z](?:\d+)?", molecule):
	atoms[atom[0]] += n*int(atom[1:] or '1')

new_atoms = collections.defaultdict(int)
for atom in re.findall(r"[A-Z](?:\d+)?", input().strip()):
	new_atoms[atom[0]] += int(atom[1:] or '1')

print(min(atoms[a]//new_atoms[a] for a in new_atoms))
