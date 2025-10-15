import os
import sys

bdf_file = sys.argv[1] if len(sys.argv) > 1 else "compactty.bdf"


in_font = set()
with open("unicode.map", "r") as f:
	for line in f:
		if line.startswith("U+"):
			in_font.add(int(line[2:6], 16))

# def is_in_font(c):
# 	return (
# 		c == 0
# 		or 0x20 <= c < 0x7f
# 		# or 0xa1 <= c < 0xff
# 		or 0xb2 <= c < 0xb4
# 		or c == 0xb9
# 		or c == 0x2074
# 		or 0x2190 <= c < 0x2194
# 		or c == 0x21b5
# 		or 0x2500 <= c < 0x2504
# 		or 0x250c <= c < 0x254b
# 		or 0x2550 <= c < 0x25a1
# 		or c == 0x25b2
# 		or c == 0x25bc
# 		or 0x2800 <= c < 0x2900
# 	)

# with open("unicode.map", "r") as f:
# 	for c in range(0x10000):
# 		if is_in_font(c):
# 			f.write(f"U+{c:04X}\n")

if input("recompile font? (Y/n) ").lower() != "n":
	os.system(f"sudo bdf2psf --fb {bdf_file} /dev/null unicode.map 512 {bdf_file[:-4]}.psf")
if input("install font? (Y/n) ").lower() != "n":
	os.system(f"sudo setfont {bdf_file[:-4]}.psf")

for c in range(0x10000):
	if c in in_font:
		print(chr(c), end="")
print()



if input("\nrevert font? (y/N) ").lower() == "y":
	os.system("sudo setfont /usr/share/consolefonts/Lat2-Terminus16.psf.gz")