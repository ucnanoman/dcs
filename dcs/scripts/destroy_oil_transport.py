import dcs
import sys
import os
import random
import argparse


def main():
    aircrafts = [x for x in dcs.planes.plane_map.values() if x.flyable]
    aircrafts += [x for x in dcs.helicopters.helicopter_map.values() if x.flyable]
    aircraft_types = [x.id for x in aircrafts]

    parser = argparse.ArgumentParser(description="DCS WWII dogfight generator")
    parser.add_argument("-a", "--aircrafttype", default=dcs.planes.A_10C.id,
                        choices=aircraft_types,
                        help="Player aircraft type")
    parser.add_argument("-u", "--unhide", action="store_true", default=False, help="Show enemy pre mission")
    parser.add_argument("-t", "--terrain", choices=["caucasus", "nevada"], default='caucasus')
    parser.add_argument("-o", "--output", help="Name and path of the generated mission", default=None)

    args = parser.parse_args()
    print(args)
    terrain_map = {
        "caucasus": dcs.terrain.Caucasus,
        "nevada": dcs.terrain.Nevada
    }

    if args.output is None:
        if args.terrain == "caucasus":
            args.output = os.path.join(os.path.expanduser("~"), "Saved Games\\DCS\\Missions\\oil_transport.miz")
        else:
            args.output = os.path.join(os.path.expanduser("~"),
                                       "Saved Games\\DCS.openalpha\\Missions\\oil_transport.miz")

    m = dcs.Mission(terrain_map[args.terrain]())

    city_graph = m.terrain.city_graph
    distance, path = city_graph.shortest_path('Gali', 'Gudauta')

    print(path)
    start_node = city_graph.node(random.choice(path))
    print(start_node)

    # create the oil convoy
    abkhazia = m.country(dcs.countries.Abkhazia.name)
    convoy_vehicles = []
    for i in range(0, random.randrange(3, 8)):
        convoy_vehicles.append(dcs.vehicles.Unarmed.Fuel_Truck_ATZ_10)
    airdef = [
        dcs.countries.Abkhazia.Vehicle.AirDefence.AAA_ZU_23_on_Ural_375,
        dcs.countries.Abkhazia.Vehicle.AirDefence.SPAAA_ZSU_23_4_Shilka
    ]
    if random.getrandbits(1):
        convoy_vehicles.append(random.choice(airdef))

    destination_node = city_graph.node('Adler')
    oil_convoy = m.vehicle_group_platoon(
        abkhazia,
        "Oil Convoy",
        convoy_vehicles,
        start_node.position)
    city_graph.travel(oil_convoy, start_node, destination_node, 60)

    # add light air defence around and in cities on path

    # place player
    aircraft_type = [x for x in aircrafts if x.id == args.aircrafttype][0]
    fg = m.flight_group_from_airport(m.country('USA'), "Player", aircraft_type, m.terrain.senaki(), dcs.task.CAS)
    fg.add_runway_waypoint(m.terrain.senaki())
    fg.units[0].set_player()

    _, path = city_graph.shortest_path(start_node.name, destination_node.name)
    notifier_node = city_graph.node(random.choice(path[:6]))
    notify_zone = m.triggers.add_triggerzone(notifier_node.position, 500, hidden=False, name='notify_zone')
    trig_notify = dcs.triggers.TriggerOnce(comment='NotifyConvoyPosition')
    trig_notify.rules.append(dcs.condition.PartOfGroupInZone(oil_convoy.id, notify_zone.id))
    trig_notify.actions.append(dcs.action.MessageToGroup(
        fg.id, m.string('An agent just reported that the convoy just arrived at ' + notifier_node.name)))
    m.triggerrules.triggers.append(trig_notify)
    print(trig_notify)
    print(len(path))


    m.forced_options.civil_traffic = dcs.forcedoptions.ForcedOptions.CivilTraffic.Low

    m.set_sortie_text("Search and destroy the oil convoy")
    m.set_description_text("""Abkhazia is selling oil to Russia to silently finance their military investments.

US and Georgia forces decided to prevent these oil transports.""")
    m.set_description_bluetask_text("""You are tasked to search and destroy a current oil convoy.

The position of the convoy is unknown, but we have several agents in Abkhazia that will look out
for the current route of the oil convoy.
Last known position will be transmitted to you while in flight.
Keep in mind that there are man pads and several AAA air defences around cities in Abkazia that are just waiting
to shoot down an American or Georgian aircraft.

Mission objectives:
  * Find the convoy
  * Destroy the convoy
  * Head back in one piece to Senaki airport.""")

    #m.save(args.output)

    return 0

if __name__ == '__main__':
    sys.exit(main())
