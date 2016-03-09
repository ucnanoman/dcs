-- append this file to 'DCS World\Scripts\Database\db_main.lua'
-- edit export_path to your export folder
local export_path = "C:\\Users\\peint\\Documents\\dcs-cs\\dcs\\"

local function writeln(file, text)
    file:write(text.."\r\n")
end

local function safe_name(name)
    local safeName = name
    safeName = string.gsub(safeName, "[-()/., *']", "_")
    safeName = string.gsub(safeName,"^([0-9])", "_%1")
    return safeName
end

local function safe_name(name)
    local safeName = name
    safeName = string.gsub(safeName, "[-()/., *']", "_")
    safeName = string.gsub(safeName,"^([0-9])", "_%1")
    return safeName
end

-- prepare weapons data

local weapons = {}
local keys = {}
for j in pairs({CAT_BOMBS,CAT_MISSILES,CAT_ROCKETS,CAT_AIR_TO_AIR,CAT_FUEL_TANKS,CAT_PODS}) do
	for i, v in ipairs(db.Weapons.Categories[j].Launchers) do
		local pyName = v.displayName
		if string.sub(v.CLSID, 0, 1) ~= "{" then
			pyName = v.CLSID
		end
		pyName = string.gsub(pyName, "[-()/., *']", "_")
		pyName = string.gsub(pyName,"^([0-9])", "_%1")
		key = pyName
		if weapons[key] ~= nil then
			key = pyName .. "_"
		end
		local w = "None"
		if v["Weight"] ~= nil then
			w = v["Weight"]
		end
		while weapons[key] ~= nil do
			key = key..'_'
		end
		weapons[key] = {clsid = v.CLSID, displayName = v.displayName, weight = w}
		table.insert(keys, key)
		-- print("    " .. key .. " = {\"clsid\": \"" .. v.CLSID .. "\", \"name\": \"" .. v.displayName .. "\"}")
	end
end

table.sort( keys )

local weapons_map = {}
local i = 1
while i <= #keys do
	local x = keys[i]
	weapons_map[weapons[x].clsid] = x
	i = i + 1
end

file = io.open(export_path.."weapons_data.py", "w")
file:write([[# This file is generated from pydcs_export.lua


class Weapons:
]])
local i = 1
while i <= #keys do
	local x = keys[i]
	writeln(file, "    " .. x .. " = {\"clsid\": \"" .. weapons[x].clsid
		.. "\", \"name\": \"" .. weapons[x].displayName .. "\", \"weight\": " .. weapons[x].weight .. "}")
	i = i + 1
end

writeln(file, '')
writeln(file, "weapon_ids = {")
i = 1
while i <= #keys do
	local x = keys[i]
	local s = "    \"" .. weapons[x].clsid .. "\": Weapons." .. x
	i = i + 1
	if i <= #keys then
		s = s .. ","
	end
	writeln(file, s)
end
writeln(file, "}")
file:close()

-- aircraft export planes and helicopters
local flyable = {}
flyable["A-10A"] = true
flyable["A-10C"] = true
flyable["Su-27"] = true
flyable["Su-33"] = true
flyable["Su-25"] = true
flyable["Su-25T"] = true
flyable["M-2000C"] = true
flyable["F-15C"] = true
flyable["MiG-29A"] = true
flyable["MiG-29S"] = true
flyable["P-51D"] = true
flyable["TF-51D"] = true
flyable["FW-190D9"] = true
flyable["Bf-109K-4"] = true
flyable["C-101EB"] = true
flyable["F-86F Sabre"] = true
flyable["Hawk"] = true
flyable["L-39C"] = true
flyable["L-39ZA"] = true
flyable["MiG-15bis"] = true
flyable["MiG-21Bis"] = true
flyable["Ka-50"] = true
flyable["Mi-8MT"] = true
flyable["UH-1H"] = true


local function export_aircraft(file, aircrafts, export_type, exportplane)
    -- generate export output
    file:write(
[[# This file is generated from pydcs_export.lua

from .weapons_data import Weapons
from . import task
from .flyingtype import FlyingType


]])
    writeln(file, 'class '..export_type..'Type(FlyingType):')
    if exportplane then
        writeln(file, '    pass')
    else
        writeln(file, '    helicopter = True')
    end
    writeln(file, '')
    writeln(file, '')

    for i in pairs(aircrafts) do
        local plane = aircrafts[i];
        local safename = plane.Name
        safename = string.gsub(safename, "[-()/., *']", "_")
        safename = string.gsub(safename,"^([0-9])", "_%1")
        writeln(file, "class "..safename.."("..export_type.."Type):")
        writeln(file, '    id = "'..plane.Name..'"')
        if plane.HumanCockpit or flyable[plane.Name] ~= nil then
            writeln(file, '    flyable = True')
        end
        if plane.singleInFlight then
            writeln(file, '    group_size_max = 1')
        end
        if plane.bigParkingRamp then
            writeln(file, '    large_parking_slot = True')
        end
        writeln(file, '    height = '..plane.height)
        if exportplane then
            writeln(file, '    width = '..plane.wing_span or plane.rotor_diameter)
        else
            writeln(file, '    width = '..plane.rotor_diameter)
        end
        writeln(file, '    length = '..plane.length)
        writeln(file, '    fuel_max = '..plane.MaxFuelWeight)
        writeln(file, '    max_speed = '..plane.MaxSpeed)
        --writeln(file, '    ammo_type = '..plane.MaxFuelWeight)
        --writeln(file, '    gun_max = '..)
        if plane.passivCounterm then
            writeln(file, '    chaff = '..plane.passivCounterm.chaff.default)
            writeln(file, '    flare = '..plane.passivCounterm.flare.default)
            writeln(file, '    charge_total = '..plane.passivCounterm.SingleChargeTotal)
            writeln(file, '    chaff_charge_size = '..plane.passivCounterm.chaff.chargeSz)
            writeln(file, '    flare_charge_size = '..plane.passivCounterm.flare.chargeSz)
        end

        if plane.TACAN then
            writeln(file, '    tacan = True')
        end

        if plane.EPLRS then
            writeln(file, '    eplrs = True')
        end

        if plane.Categories and plane.Categories[1] then
            local s = '    category = "'
            if plane.Categories[1].CLSID == "{D2BC159C-5B7D-40cf-92CD-44DF3E99FAA9}" then
                s = s..'AWACS'
            elseif plane.Categories[1].CLSID == "{8A302789-A55D-4897-B647-66493FA6826F}" then
                s = s..'Tanker'
            elseif plane.Categories[1].CLSID == "{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}" then
                s = s..'Interceptor'
            else
                s = s..'Air'
            end
            writeln(file, s..'"')  -- category
        end

        -- panel radio
        if plane.HumanRadio then
            local bwritefreq = false
            if exportplane and plane.HumanRadio.frequency ~= 251 then
                bwritefreq = true
            end
            if not exportplane and plane.HumanRadio.frequency ~= 127.5 then
                bwritefreq = true
            end
            if bwritefreq then
                writeln(file, '    radio_frequency = '..plane.HumanRadio.frequency)
            end
            -- modulation seems always to be nil
            -- if plane.HumanRadio.modulation ~= nil then
            --     writeln(file, '    radio_modulation = '..plane.HumanRadio.modulation)
            -- end
        end
        if plane.panelRadio then
            writeln(file, '')
            writeln(file, '    panel_radio = {')
            for j in pairs(plane.panelRadio) do
                cnt = 0
                writeln(file, '        '..j..': {')
                writeln(file, '            "channels": {')
                for c in pairs(plane.panelRadio[j]["channels"]) do
                    channel = plane.panelRadio[j]["channels"][c]
                    local s = '                '..c..': '..channel.default
                    if cnt + 1 < #plane.panelRadio[j]["channels"] then
                       s = s..','
                    end
                    writeln(file, s)
                    cnt = cnt + 1
                end
                writeln(file, '            },')
                writeln(file, '        },')
            end
            writeln(file, '    }')
        end

        if plane.SpecificCallnames then
            writeln(file, '')
            writeln(file, '    callnames = {')
            for c in pairs(plane.SpecificCallnames) do
                writeln(file, '        "'..country.by_idx[c].Name..'": [')
                for n in pairs(plane.SpecificCallnames[c]) do
                    writeln(file, '            "'..plane.SpecificCallnames[c][n][1]..'",')
                end
                writeln(file, '        ]')
            end
            writeln(file, '    }')
        end

        local pylons = {}

        for j in pairs(plane.Pylons) do
            if #plane.Pylons[j].Launchers > 0 then
                writeln(file, "")
                table.insert(pylons, j)
                writeln(file, '    class Pylon'..j..':')
                for k in pairs(plane.Pylons[j].Launchers) do
                    if weapons_map[plane.Pylons[j].Launchers[k].CLSID] then
                        local name = weapons_map[plane.Pylons[j].Launchers[k].CLSID]
                        writeln(file, '        '..name..' = ('..j..', Weapons.'..name..')')
                    else
                        writeln(file, '#ERRR '..plane.Pylons[j].Launchers[k].CLSID)
                    end
                end
            end
        end

        writeln(file, "")
        local s = ''
        for j in pairs(pylons) do
            s = s..tostring(pylons[j])
            if j < #pylons then
                s = s..', '
            end
        end
        writeln(file, '    pylons = {'..s..'}')

        -- tasks
        writeln(file, "")
        s = ''
        j = 1
        while j <= #plane.Tasks do
            local objname = string.gsub(plane.Tasks[j].Name, "[-()/., *']", "")
            s = s..'task.'..objname..''
            j = j + 1
            if j <= #plane.Tasks then
                s = s..', '
            end
        end
        writeln(file, '    tasks = ['..s..']')
        local objname = string.gsub(plane.DefaultTask.Name, "[-()/., *']", "")
        writeln(file, '    task_default = task.'..objname..'')
        -- writeln(file, safename..'.load_payloads()')
        writeln(file, "")
        writeln(file, "")
    end


    writeln(file, string.lower(export_type).."_map = {")
    for i in pairs(aircrafts) do
        local plane = aircrafts[i];
        local safename = plane.Name
        safename = string.gsub(safename, "[-()/., *']", "_")
        safename = string.gsub(safename,"^([0-9])", "_%1")
        writeln(file, '    "'..plane.Name..'": '..safename..',')
    end
    writeln(file, "}")
end

file = io.open(export_path.."planes.py", "w")
export_aircraft(file, db.Units.Planes.Plane, 'Plane', true)
file:close()

aircrafts = db.Units.Helicopters.Helicopter
file = io.open(export_path.."helicopters.py", "w")
export_aircraft(file, db.Units.Helicopters.Helicopter, 'Helicopter', false)
file:close()

-- ground units
file = io.open(export_path.."vehicles.py", "w")

file:write(
[[# This file is generated from pydcs_export.lua

from . import unittype
]])

-- sort by categories
local unit_categories = {}
unit_categories["Unarmed"] = {}
unit_categories["AirDefence"] = {}
unit_categories["Armor"] = {}
unit_categories["Fortification"] = {}
unit_categories["Artillery"] = {}
unit_categories["Infantry"] = {}

for i in pairs(db.Units.Cars.Car) do
    local unit = db.Units.Cars.Car[i]
    if unit.category == 'Air Defence' then
        table.insert(unit_categories["AirDefence"], unit)
    else
        table.insert(unit_categories[unit.category], unit)
    end
end

for i in pairs(unit_categories) do
    writeln(file, '')
    writeln(file, '')
    writeln(file, 'class '..i..':')
    for j in pairs(unit_categories[i]) do
        local unit = unit_categories[i][j]
        local safename = safe_name(unit.DisplayName)
        writeln(file, '')
        writeln(file, '    class '..safename..'(unittype.VehicleType):')
        writeln(file, '        id = "'..unit.Name..'"')
        writeln(file, '        name = "'..unit.DisplayName..'"')
        --writeln(file, '        category = '..i)
    end
end

writeln(file, '')
writeln(file, "vehicle_map = {")
for i in pairs(db.Units.Cars.Car) do
    local unit = db.Units.Cars.Car[i];
    local safename = safe_name(unit.DisplayName)
    local cat = "AirDefence"
    if unit.category ~= "Air Defence" then
        cat = unit.category
    end
    writeln(file, '    "'..unit.Name..'": '..cat..'.'..safename..',')
end
writeln(file, "}")
file:close()

-- export country data
file = io.open(export_path.."countries.py", "w")

local categories = {
    'AWACS',
    'Tanker',
    'Air',
    'Helipad',
    'Ground Units'
}

writeln(file, '# This file is generated from pydcs_export.lua')
writeln(file, '')
writeln(file, 'from .country import Country')
writeln(file, 'from . import vehicles')
local i = 0
while i <= country.maxIndex do
    local c = country.by_idx[i]
    if c then
        local pyName = c.Name
        pyName = string.gsub(pyName, "[-()/., *']", "")
        writeln(file, '')
        writeln(file, '')
        writeln(file, 'class '..pyName..'(Country):')
        writeln(file, '    id = '..i)
        writeln(file, '    name = "'..c.Name..'"')
        writeln(file, '')

        writeln(file, '    class Vehicle:')

        -- sort country vehicles by category
        local unit_categories = {}
        unit_categories["Unarmed"] = {}
        unit_categories["AirDefence"] = {}
        unit_categories["Armor"] = {}
        unit_categories["Fortification"] = {}
        unit_categories["Artillery"] = {}
        unit_categories["Infantry"] = {}

        local cars = c.Units.Cars.Car
        for u in pairs(cars) do
            local unit = {}
            for i in pairs(db.Units.Cars.Car) do
                unit = db.Units.Cars.Car[i]
                if unit.Name == cars[u].Name then
                    break
                end
            end

            if unit.category == 'Air Defence' then
                table.insert(unit_categories["AirDefence"], unit)
            else
                table.insert(unit_categories[unit.category], unit)
            end
        end

        for i in pairs(unit_categories) do
            if #unit_categories[i] > 0 then
                writeln(file, '')
                writeln(file, '')
                writeln(file, '        class '..i..':')
                for j in pairs(unit_categories[i]) do
                    local unit = unit_categories[i][j]
                    local safename = safe_name(unit.DisplayName)
                    writeln(file, '            '..safename..' = vehicles.'..i..'.'..safename)
                end
            end
        end

        local planes = c.Units.Planes.Plane
        if #planes > 0 then
            writeln(file, '')
            writeln(file, '    class Plane:')
            for u in pairs(planes) do
                local safeName = safe_name(planes[u].Name)
                writeln(file, '        '..safeName..' = "'..planes[u].Name..'"')
            end

            writeln(file, '')
            writeln(file, '    planes = [')
            for u in pairs(planes) do
                local safeName = safe_name(planes[u].Name)
                writeln(file, '        Plane.'..safeName..',')
            end
            writeln(file, '    ]')
        end

        local helis = c.Units.Helicopters.Helicopter
        if #helis > 0 then
            writeln(file, '')
            writeln(file, '    class Helicopter:')
            for u in pairs(helis) do
                local safeName = safe_name(helis[u].Name)
                writeln(file, '        '..safeName..' = "'..helis[u].Name..'"')
            end

            writeln(file, '')
            writeln(file, '    helicopters = [')
            for u in pairs(helis) do
                local safeName = safe_name(helis[u].Name)
                writeln(file, '        Helicopter.'..safeName..',')
            end
            writeln(file, '    ]')
        end

        local ships = c.Units.Ships.Ship
        if #ships > 0 then
            writeln(file, '')
            writeln(file, '    class Ship:')
            for u in pairs(ships) do
                local safeName = safe_name(ships[u].Name)
                writeln(file, '        '..safeName..' = "'..ships[u].Name..'"')
            end
        end

        local countrycall = db.Callnames[i]
        if countrycall then
            for cat in pairs(categories) do
                local call = db.Callnames[i][categories[cat]]
                if call then
                    safeName = string.gsub(categories[cat], "[-()/., *']", "")
                    writeln(file, '')
                    writeln(file, '    class Callsign'..safeName..':')
                    for j in pairs(call) do
                        writeln(file, '        '..call[j].Name..' = "'..call[j].Name..'"')
                    end
                end
            end

            writeln(file, '')
            writeln(file, '    callsign = {')
            for cat in pairs(categories) do
                local call = db.Callnames[i][categories[cat]]
                if call then
                    safeName = string.gsub(categories[cat], "[-()/., *']", "")
                    writeln(file, '        "'..safeName..'": [')
                    local s = ''
                    for j in pairs(call) do
                        s = '            Callsign'..safeName..'.'..call[j].Name
                        if j < #call then
                            s = s..','
                        end
                        writeln(file, s)
                    end
                    writeln(file, '        ],')
                end
            end
            writeln(file, '    }')
        end

        writeln(file, '')
        writeln(file, '    def __init__(self):')
        writeln(file, '        super('..pyName..', self).__init__('..pyName..'.id, '..pyName..'.name)')
    end
    i = i + 1
end

writeln(file, '')
writeln(file, 'country_dict = {')
i = 0
while i <= country.maxIndex do
    local c = country.by_idx[i]
    if c then
        local pyName = c.Name
        pyName = string.gsub(pyName, "[-()/., *']", "")
        writeln(file, '    '..pyName..'.id: '..pyName..'(),')
    end
    i = i + 1
end
writeln(file, '}')

writeln(file, [[


def get_by_id(_id: int):
    return country_dict[_id]
]])
file:close()
