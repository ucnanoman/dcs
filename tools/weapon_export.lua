-- to create the weapons.lua:
-- make sure db_weapons.lua and db_weapons_data.lua are correctly converted from Cyrilic(Windows 1251) encoding to UTF-8
-- copy db_weapons.lua to weapons.lua
-- comment the dofile call in weapons.lua

function _(s)
	return s
end

ed_path = "C:/Program Files/Eagle Dynamics/DCS World"
--ed_path = "/home/rp/dcs_data"

db = {}
dofile(ed_path.."/Scripts/Database/wsTypes.lua")
dofile('weapons.lua')
dofile(ed_path.."/Scripts/Database/db_weapons_data.lua")


-- mod functions
function declare_weapon(tbl) end
function mount_vfs_model_path() end
function mount_vfs_liveries_path() end
function mount_vfs_texture_path() end
function mount_vfs_sound_path() end
function makeAirplaneCanopyGeometry(a, b, c) end
function simple_aa_warhead() end
function pylon() end
function aircraft_task() end
function verbose_to_dmg_properties() end
function add_aircraft() end

function declare_loadout(tbl)
	if tbl.category ~= nil then
	   _WEAPON_(tbl.category,tbl)
	end
end

-- mod weapons
dofile(ed_path.."/CoreMods/WWII Units/Weapons.lua")

mod_weapons = {}
mod_weapons["M2KC_Weapons"] = ed_path.."/CoreMods/aircraft/M-2000C/Weapons"
mod_weapons["Bf-109K-4"] = ed_path.."/CoreMods/WWII Units"
mod_weapons["FW-190D9"] = ed_path.."/CoreMods/WWII Units"


for k,v in pairs(mod_weapons) do
    current_mod_path = v
    dofile(v.."/"..k..".lua")
end

weapons = {}
keys = {}
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
		weapons[key] = {clsid = v.CLSID, displayName = v.displayName, weight = w}
		table.insert(keys, key)
		-- print("    " .. key .. " = {\"clsid\": \"" .. v.CLSID .. "\", \"name\": \"" .. v.displayName .. "\"}")
	end
end

table.sort( keys )

if arg[1] then
print("-- lua helper file for plane_exporter")
print("weapons_map = {}")
i = 1
while i <= #keys do
	local x = keys[i]
	local s = 'weapons_map["' .. weapons[x].clsid .. '"] = "'..x..'"'
	i = i + 1
	print(s)
end
else
print('# This file is generated from weapon_export.lua')
print()
print()
print("class Weapons:")
local i = 1
while i <= #keys do
	local x = keys[i]
	print("    " .. x .. " = {\"clsid\": \"" .. weapons[x].clsid
		.. "\", \"name\": \"" .. weapons[x].displayName .. "\", \"weight\": " .. weapons[x].weight .. "}")
	i = i + 1
end

print()
print("weapon_ids = {")
i = 1
while i <= #keys do
	local x = keys[i]
	local s = "    \"" .. weapons[x].clsid .. "\": Weapons." .. x
	i = i + 1
	if i <= #keys then
		s = s .. ","
	end
	print(s)
end
print("}")

end -- arg[1]