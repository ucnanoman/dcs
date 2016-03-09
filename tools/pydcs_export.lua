local function writeln(file, text)
    file:write(text.."\n")
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

file = io.open("weapons_data.py", "w")
file:write([[# This file is generated from weapon_export.lua


class Weapons:]])
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

local function export_aircraft(file, aircrafts, export_type, exportplane)
    -- generate export output
    file:write([[
    # This file is generated from aircraft_export.lua

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
        if plane.singleInFlight then
            writeln(file, '    group_size_max = 1')
        end
        if plane.WingSpan ~= Nil and tonumber(plane.WingSpan) > 20 then
            writeln(file, '    large_parking_slot = True')
        end
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

file = io.open("planes.py", "w")
export_aircraft(file, db.Units.Planes.Plane, 'Plane', true)
file:close()

aircrafts = db.Units.Helicopters.Helicopter
file = io.open("helicopters.py", "w")
export_aircraft(file, db.Units.Helicopters.Helicopter, 'Helicopter', false)
file:close()
