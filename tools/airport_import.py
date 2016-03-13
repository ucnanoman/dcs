"""
This script imports airport data, that was previously exported by a lua function.

The lua function to export is just beneath this comment block, insert it somewhere in the mission editor
and call it somewhere
"""

"""
function dumpairportdata()
    local S	= require('Serializer')
    local airdromedump = {}
    for k, v in pairs(MapWindow.listAirdromes) do
        --MapWindow.listAirdromes[unit.boss.route.points[1].airdromeId].roadnet
        local sList = Terrain.getStandList(v.roadnet, {"SHELTER","FOR_HELICOPTERS","FOR_AIRPLANES","WIDTH","LENGTH","HEIGHT"})
        info = {}
        info["airport"] = v
        info["standlist"] = sList
        airdromedump[k] = info
    end
    local f = base.io.open("C:\\tmp\\standlist.lua", 'w')
    if f then
            local s = S.new(f)
            s:serialize_simple2('airports', airdromedump)
            f:close()
    else
        showWarningMessageBox(_('Error saving standlist'))
    end
end
"""

import argparse
import dcs.lua
import codecs


def nevada_airports_base_info(airports):
    airports[1] = {'id': 1, 'name': 'Creech', 'tacan':None, 'runways': []}
    airports[1]['runways'].append(80)
    airports[1]['runways'].append(130)

    airports[2] = {'id': 2, 'name': 'Groom', 'tacan':None, 'runways': []}
    airports[2]['runways'].append(320)

    airports[3] = {'id': 3, 'name': 'McCarran', 'tacan':None, 'runways': []}
    airports[3]['runways'].append(70)
    airports[3]['runways'].append(70)

    airports[4] = {'id': 4, 'name': 'Nellis', 'tacan':None, 'runways': []}
    airports[4]['runways'].append(30)
    airports[4]['runways'].append(30)
    return airports


def caucasus_airports_base_info(airports):
    airports[12] = {'id': 12, 'name': 'Anapa', 'tacan':None, 'runways': []}
    airports[12]['runways'].append(40)
    airports[13] = {'id': 13, 'name': 'Krasnodar-Center', 'tacan':None, 'runways': []}
    airports[13]['runways'].append(270)
    airports[14] = {'id': 14, 'name': 'Novorossiysk', 'tacan':None, 'runways': []}
    airports[14]['runways'].append(220)
    airports[15] = {'id': 15, 'name': 'Krymsk', 'tacan':None, 'runways': []}
    airports[15]['runways'].append(220)
    airports[16] = {'id': 16, 'name': 'Maykop', 'tacan':None, 'runways': []}
    airports[16]['runways'].append(220)
    airports[17] = {'id': 17, 'name': 'Gelendzhik', 'tacan':None, 'runways': []}
    airports[17]['runways'].append(220)
    airports[18] = {'id': 18, 'name': 'Sochi', 'tacan':None, 'runways': []}
    airports[18]['runways'].append(240)
    airports[19] = {'id': 19, 'name': 'Krasnodar-Pashkovsky', 'tacan':None, 'runways': []}
    airports[19]['runways'].append(40)
    airports[20] = {'id': 20, 'name': 'Sukhumi', 'tacan':None, 'runways': []}
    airports[20]['runways'].append(300)
    airports[21] = {'id': 21, 'name': 'Gudauta', 'tacan':None, 'runways': []}
    airports[21]['runways'].append(330)
    airports[22] = {'id': 22, 'name': 'Batumi', 'tacan':"16X", 'runways': []}
    airports[22]['runways'].append(300)
    airports[23] = {'id': 23, 'name': 'Senaki', 'tacan':"31X", 'runways': []}
    airports[23]['runways'].append(90)
    airports[24] = {'id': 24, 'name': 'Kobuleti', 'tacan':"67X", 'runways': []}
    airports[24]['runways'].append(70)
    airports[25] = {'id': 25, 'name': 'Kutaisi', 'tacan':None, 'runways': []}
    airports[25]['runways'].append(70)
    airports[26] = {'id': 26, 'name': 'Mineralnye', 'tacan':None, 'runways': []}
    airports[26]['runways'].append(290)
    airports[27] = {'id': 27, 'name': 'Nalchik', 'tacan':None, 'runways': []}
    airports[27]['runways'].append(60)
    airports[28] = {'id': 28, 'name': 'Mozdok', 'tacan':None, 'runways': []}
    airports[28]['runways'].append(80)
    airports[29] = {'id': 29, 'name': 'Lochini', 'tacan':None, 'runways': []}
    airports[29]['runways'].append(300)
    airports[30] = {'id': 30, 'name': 'Soganlug', 'tacan':None, 'runways': []}
    airports[30]['runways'].append(130)
    airports[31] = {'id': 31, 'name': 'Vaziani', 'tacan':None, 'runways': []}
    airports[31]['runways'].append(140)
    airports[32] = {'id': 32, 'name': 'Beslan', 'tacan':None, 'runways': []}
    airports[32]['runways'].append(90)

    return airports


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--terrain", choices=["caucasus", "nevada"], default="caucasus")
    parser.add_argument("airportinfofile")

    args = parser.parse_args()

    with codecs.open(args.airportinfofile, "r", "utf-8") as f:
        data = dcs.lua.loads(f.read())

        airports = {}
        terrain_map = {
            "caucasus": caucasus_airports_base_info,
            "nevada": nevada_airports_base_info
        }

        terrain_map[args.terrain](airports)

        for id in sorted(data["airports"]):
            airport = data["airports"][id]
            tacan = airports[id]["tacan"]
            tacan = '"' + tacan + '"' if tacan else None
            print(
"""

class {sname}(Airport):
    id = {id}
    name = "{name}"
    position = mapping.Point({x}, {y})
    tacan = {tacan}
    frequencies = [{freq}]
    unit_zones = []
    civilian = {civ}
    slot_version = {slot_version}

    def __init__(self):
        super({sname}, self).__init__()
""".format(sname=airports[id]["name"].replace('-',''), name=airports[id]["name"], id=id, x=airport["airport"]["reference_point"]["x"],
           y=airport["airport"]["reference_point"]["y"], tacan=tacan,
           freq=", ".join(map(str, airport["airport"]["frequency"].values())),
           civ=airport["airport"].get("civilian", True),
           slot_version=2 if args.terrain=="nevada" else 1)
            )

            for runway in airports[id]["runways"]:
                print("        self.runways.append(Runway({hdg}))".format(hdg=runway))

            for standid in sorted(airport["standlist"]):
                slot = airport["standlist"][standid]
                large_bit = 1 << 3
                large = slot["flag"] & large_bit == large_bit
                height = float(slot["params"]["HEIGHT"]) if slot["params"]["HEIGHT"] else None
                print("""        self.parking_slots.append(ParkingSlot(
                crossroad_idx={crossidx}, position=mapping.Point({x}, {y}), large={large}, heli={heli},
                airplanes={airplanes}, slot_name='{name}', length={length}, width={width}, height={height}, shelter={shelter}))""".format(
                    crossidx=slot["crossroad_index"], x=slot["x"], y=slot["y"],
                    large=large, heli=slot["params"]["FOR_HELICOPTERS"] == "1", airplanes=slot["params"]["FOR_AIRPLANES"] == "1",
                    name=slot["name"],
                    length=float(slot["params"]["LENGTH"]), width=float(slot["params"]["WIDTH"]), height=height,
                    shelter=slot["params"]["SHELTER"] == "1"
                ))

        for id in sorted(data["airports"]):
            airport = data["airports"][id]
            sname = airports[id]["name"].replace('-', '')
            keyname = airports[id]["name"]
            print("self.airports['{keyname}'] = {name}()".format(keyname=keyname, name=sname))

        for id in sorted(data["airports"]):
            airport = data["airports"][id]
            sname = airports[id]["name"].replace('-', '').lower()
            keyname = airports[id]["name"]
            print("""
    def {name}(self) -> Airport:
        return self.airports["{keyname}"]""".format(keyname=keyname, name=sname))


if __name__ == "__main__":
    main()
