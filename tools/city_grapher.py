import dcs
import os


def main():
    basedir = os.path.dirname(__file__)
    for x in os.listdir(os.path.join(basedir, 'graph_missions')):
        split = x.split('_')
        terrainname = split[0]
        graph = dcs.terrain.Graph()
        graph.load_graph(os.path.join(basedir, 'graph_missions', x))
        graph.store_pickle(os.path.join(basedir, '..', 'dcs', 'terrain', '{name}.p'.format(name=terrainname)))

if __name__ == '__main__':
    main()
