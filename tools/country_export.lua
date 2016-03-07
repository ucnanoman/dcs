
db_path = "/home/rp/dcs_data/Scripts/Database/"

function _(s)
	return s
end

db = {}
dofile(db_path.."db_countries.lua")
dofile(db_path.."db_callnames.lua")

print('# This file is generated from country_export.lua')
print()
print('from .country import Country')

local categories = {
	'AWACS',
	'Tanker',
	'Air',
	'Helipad',
	'Ground Units'
}

local function safe_name(name)
	local safeName = name
	safeName = string.gsub(safeName, "[-()/., *']", "_")
	safeName = string.gsub(safeName,"^([0-9])", "_%1")
	return safeName
end

local i = 0
while i <= country.maxIndex do
	local c = country.by_idx[i]
	if c then
		local pyName = c.Name
		pyName = string.gsub(pyName, "[-()/., *']", "")
		print()
		print()
		print('class '..pyName..'(Country):')
		print('    id = '..i)
		print('    name = "'..c.Name..'"')
		print()

		print('    class Vehicle:')
		local cars = c.Units.Cars.Car
		for u in pairs(cars) do
			local safeName = safe_name(cars[u].Name)
			print('        '..safeName..' = "'..cars[u].Name..'"')
		end

		local planes = c.Units.Planes.Plane
		if #planes > 0 then
			print('')
			print('    class Plane:')
			for u in pairs(planes) do
				local safeName = safe_name(planes[u].Name)
				print('        '..safeName..' = "'..planes[u].Name..'"')
			end

			print('')
			print('    planes = [')
			for u in pairs(planes) do
				local safeName = safe_name(planes[u].Name)
				print('        Plane.'..safeName..',')
			end
			print('    ]')
		end

		local helis = c.Units.Helicopters.Helicopter
		if #helis > 0 then
			print('')
			print('    class Helicopter:')
			for u in pairs(helis) do
				local safeName = safe_name(helis[u].Name)
				print('        '..safeName..' = "'..helis[u].Name..'"')
			end

			print('')
			print('    helicopters = [')
			for u in pairs(helis) do
				local safeName = safe_name(helis[u].Name)
				print('        Helicopter.'..safeName..',')
			end
			print('    ]')
		end

		local ships = c.Units.Ships.Ship
		if #ships > 0 then
			print('')
			print('    class Ship:')
			for u in pairs(ships) do
				local safeName = safe_name(ships[u].Name)
				print('        '..safeName..' = "'..ships[u].Name..'"')
			end
		end

		local countrycall = db.Callnames[i]
		if countrycall then
			for cat in pairs(categories) do
				local call = db.Callnames[i][categories[cat]]
				if call then
					safeName = string.gsub(categories[cat], "[-()/., *']", "")
					print()
					print('    class Callsign'..safeName..':')
					for j in pairs(call) do
						print('        '..call[j].Name..' = "'..call[j].Name..'"')
					end
				end
			end

			print()
			print('    callsign = {')
			for cat in pairs(categories) do
				local call = db.Callnames[i][categories[cat]]
				if call then
					safeName = string.gsub(categories[cat], "[-()/., *']", "")
					print('        "'..safeName..'": [')
					local s = ''
					for j in pairs(call) do
						s = '            Callsign'..safeName..'.'..call[j].Name
						if j < #call then
							s = s..','
						end
						print(s)
					end
					print('        ],')
				end
			end
			print('    }')
		end

		print()
		print('    def __init__(self):')
		print('        super('..pyName..', self).__init__('..pyName..'.id, '..pyName..'.name)')
	end
	i = i + 1
end

print()
print('country_dict = {')
i = 0
while i <= country.maxIndex do
	local c = country.by_idx[i]
	if c then
		local pyName = c.Name
		pyName = string.gsub(pyName, "[-()/., *']", "")
		print('    '..pyName..'.id: '..pyName..'(),')
	end
	i = i + 1
end
print('}')

print([[


def get_by_id(_id: int):
    return country_dict[_id]
]])
