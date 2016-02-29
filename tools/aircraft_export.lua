db = {}
db.Units = {}
mech_timing = {}
SFM_Data = {}
planes_dmg_properties = {}
planes_dmg_parts = {}
lights_prototypes = {}
exhaust_data = {}
guns_by_wstype = {}
country = {}
country["USA"] = {}


function _(s)
	return s
end

function get_aircraft_ammo_mass(_type)
	return 1
end

function makeAirplaneCanopyGeometry(a, b, c)
	return 1
end

function makeHelicopterCanopyGeometry(a, b, c)
    return 1
end

ed_path = "C:/Program Files/Eagle Dynamics/DCS World"
--ed_path = "/home/rp/dcs_data"
db_path = ed_path.."/Scripts/Database/"

dofile(db_path.."PlaneConst.lua")
dofile(db_path.."HelicopterConst.lua")
dofile(db_path.."db_units_planes.lua")
dofile(db_path.."db_units_helicopters.lua")
dofile(db_path.."wsTypes.lua")
dofile("weapons_map.lua")

-- functions for mods
function simple_warhead() end
function fire_effect() end
function smoke_effect() end

local function form_helicopter(t)
    t.MaxSpeed  = t.V_max
end

local function form_plane(t)
    t.WingSpan  = t.wing_span
    t.MaxSpeed  = t.V_max_h * 3.6
end

function add_aircraft(t)

	if  t.attribute[2] == wsType_Airplane then
        form_plane(t)
        table.insert(db.Units.Planes.Plane,t);
    else -- helicopter
        form_helicopter(t)
        table.insert(db.Units.Helicopters.Helicopter,t)
    end

	t.attribute[4]  	= t.WorldID
    t.stores_number     = #t.Pylons
    t.EmptyWeight       = t.M_empty
    t.MaxFuelWeight     = t.M_fuel_max
    t.MaxTakeOffWeight  = t.M_max
    t.MaxHeight         = t.H_max
	if t.HumanRadio   == nil then
       t.HumanRadio = {
            frequency = 251.0,
            editable = true,
            minFrequency = 225.000,
            maxFrequency = 399.975,
            modulation = MODULATION_AM
            }
    end

	t.AmmoWeight = get_aircraft_ammo_mass(t.Guns);

	if #t.Tasks == 0 then
		t.Tasks = {
					aircraft_task(Reconnaissance)
				  }
	end
end

-- dummy functions
function mount_vfs_model_path() end
function mount_vfs_liveries_path() end
function mount_vfs_texture_path() end
function mount_vfs_sound_path() end
function declare_loadout() end
function simple_aa_warhead() end
function declare_weapon() end
function gun_mount() end
function verbose_to_dmg_properties() end

-- load mods
dofile(ed_path.."/CoreMods/WWII Units/Weapons.lua")

mod_aircraft = {}
mod_aircraft["M-2000C"] = ed_path.."/CoreMods/aircraft/M-2000C"
mod_aircraft["L-39C"] = ed_path.."/CoreMods/aircraft/L-39"
mod_aircraft["L-39ZA"] = ed_path.."/CoreMods/aircraft/L-39"
mod_aircraft["Hawk"] = ed_path.."/CoreMods/aircraft/Hawk"
mod_aircraft["entry"] = ed_path.."/CoreMods/aircraft/MQ-9 Reaper"
mod_aircraft["Bf-109K-4"] = ed_path.."/CoreMods/WWII Units"
mod_aircraft["FW-190D9"] = ed_path.."/CoreMods/WWII Units"
mod_aircraft["MiG-15bis"] = ed_path.."/CoreMods/aircraft/MiG-15bis"

-- make sure output is stable
aircraft_keys = {}
for n in pairs(mod_aircraft) do table.insert(aircraft_keys, n) end
table.sort(aircraft_keys)

for i,k in pairs(aircraft_keys) do
    local v = mod_aircraft[k]
    current_mod_path = v
    dofile(v.."/"..k..".lua")
end
current_mod_path = ed_path.."/CoreMods/aircraft/MiG-21BIS"
dofile(current_mod_path.."/Entry/Aw")
dofile(current_mod_path.."/Entry/Am")

local export_type = 'Plane'
local exportplane = true
aircrafts = db.Units.Planes.Plane
if arg[1] == "heli" then
    export_type = 'Helicopter'
    exportplane = false
    aircrafts = db.Units.Helicopters.Helicopter
end

-- generate export output
print([[
# This file is generated from aircraft_export.lua

from .weapons_data import Weapons
from . import task
from .flyingtype import FlyingType

]])
print('class '..export_type..'Type(FlyingType):')
if exportplane then
    print('    pass')
else
    print('    helicopter = True')
end
print('')
print('')

for i in pairs(aircrafts) do
    local plane = aircrafts[i];
    local safename = plane.Name
    safename = string.gsub(safename, "[-()/., *']", "_")
    safename = string.gsub(safename,"^([0-9])", "_%1")
    print("class "..safename.."("..export_type.."Type):")
    print('    id = "'..plane.Name..'"')
    if plane.singleInFlight then
        print('    group_size_max = 1')
    end
    if plane.WingSpan ~= Nil and tonumber(plane.WingSpan) > 30 then
        print('    large_parking_slot = True')
    end
    print('    fuel_max = '..plane.MaxFuelWeight)
    print('    max_speed = '..plane.MaxSpeed)
    --print('    ammo_type = '..plane.MaxFuelWeight)
    --print('    gun_max = '..)
    if plane.passivCounterm then
        print('    chaff = '..plane.passivCounterm.chaff.default)
        print('    flare = '..plane.passivCounterm.flare.default)
        print('    charge_total = '..plane.passivCounterm.SingleChargeTotal)
        print('    chaff_charge_size = '..plane.passivCounterm.chaff.chargeSz)
        print('    flare_charge_size = '..plane.passivCounterm.flare.chargeSz)
    end

    if plane.TACAN then
        print('    tacan = True')
    end

    if plane.EPLRS then
        print('    eplrs = True')
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
        print(s..'"')  -- category
    end

    -- panel radio
    if plane.panelRadio then
        print('')
        print('    panel_radio = {')
        for j in pairs(plane.panelRadio) do
            cnt = 0
            print('        '..j..': {')
            print('            "channels": {')
            for c in pairs(plane.panelRadio[j]["channels"]) do
                channel = plane.panelRadio[j]["channels"][c]
                local s = '                '..c..': '..channel.default
                if cnt + 1 < #plane.panelRadio[j]["channels"] then
                   s = s..','
                end
                print(s)
                cnt = cnt + 1
            end
            print('            },')
            print('        },')
        end
        print('    }')
    end

    local pylons = {}

    for j in pairs(plane.Pylons) do
        if #plane.Pylons[j].Launchers > 0 then
            print("")
            table.insert(pylons, j)
            print('    class Pylon'..j..':')
            for k in pairs(plane.Pylons[j].Launchers) do
                if weapons_map[plane.Pylons[j].Launchers[k].CLSID] then
                    local name = weapons_map[plane.Pylons[j].Launchers[k].CLSID]
                    print('        '..name..' = ('..j..', Weapons.'..name..')')
                else
                    print('#ERRR '..plane.Pylons[j].Launchers[k].CLSID)
                end
            end
        end
    end

    print("")
    local s = ''
    for j in pairs(pylons) do
        s = s..tostring(pylons[j])
        if j < #pylons then
            s = s..', '
        end
    end
    print('    pylons = {'..s..'}')

    -- tasks
    print("")
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
    print('    tasks = ['..s..']')
    local objname = string.gsub(plane.DefaultTask.Name, "[-()/., *']", "")
    print('    task_default = task.'..objname..'')
    -- print(safename..'.load_payloads()')
    print("")
    print("")
end


print(string.lower(export_type).."_map = {")
for i in pairs(aircrafts) do
    local plane = aircrafts[i];
    local safename = plane.Name
    safename = string.gsub(safename, "[-()/., *']", "_")
    safename = string.gsub(safename,"^([0-9])", "_%1")
    print('    "'..plane.Name..'": '..safename..',')
end
print("}")
