"""
Parses the db_weapons_data.lua to provide weapon defines.
"""
import sys
import re


def main(weopfile):
    weapons = {}
    disp_names = []
    with open(weopfile, 'r') as f:
        startparse = False
        clsid = None
        displayname = None
        cnt = 0
        clsid_cnt = 0
        for rawline in f:
            if rawline.startswith("db.Weapons.Categories"):
                startparse = True

            if rawline.startswith("} -- end of db.Weapons.Categories"):
                startparse = False

            if startparse:
                line = rawline.strip()
                match = re.match('CLSID\W*=\W*"(.*)"', line)
                if match:
                    if clsid and displayname:
                        weapons[clsid] = {"clsid": clsid, "name": displayname}
                    clsid = match.group(1)
                    displayname = None

                match = re.match('displayName\W*=\W*_\("(.*)"', line)
                if match:
                    displayname = match.group(1)
                    disp_names.append(displayname)

                if line.startswith('CLSID'):
                    clsid_cnt += 1

                if line.startswith('displayName'):
                    cnt += 1
                    print(clsid, displayname)

        for clsid in weapons:
            print(clsid, "=", weapons[clsid]["name"])
        print(len(weapons), cnt, clsid_cnt)
        names = [weapons[x]["name"] for x in weapons]
        for x in disp_names:
            if x not in names:
                print(x)


if __name__ == "__main__":
    main(sys.argv[1])