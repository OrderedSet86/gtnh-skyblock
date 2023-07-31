import pygraphviz as pgv


if __name__ == '__main__':
    # Color choices from https://github.com/terrastruct/d2/blob/master/d2themes/d2themescatalog/terminal.go

    G = pgv.AGraph(directed=True)

    G.node_attr['shape'] = 'box'
    G.node_attr['fontname'] = 'Source Sans Pro'
    G.node_attr['style'] = 'filled'
    G.node_attr['fillcolor'] = 'white'

    G.edge_attr['fontname'] = 'Source Sans Pro'
    G.edge_attr['fontcolor'] = 'blue'
    G.edge_attr['labeldistance'] = 0

    agedirt = G.add_subgraph(name='cluster_agedirt', label='DIRT AGE', fontname='Source Sans Pro', bgcolor='gray')

    agedirt.add_node('die', label='Die')
    agedirt.add_node('mobfarm', label='Make Mob Spawning Platform/Farm')
    agedirt.add_node('mdi', label='[Infernal Mobs] Infernal Mob Drops')
    agedirt.add_node('mdu', label='[Infernal Mobs] Ultra Mob Drops')
    agedirt.add_node('mde', label='[Infernal Mobs] Elite Mob Drops')
    agedirt.add_node('ctl', label='Common Thaumcraft Lootbag')
    agedirt.add_node('czv', label='Convert Zombie Villager')
    agedirt.add_node('sapling', label='Farmer or Lumberjack with Sapling Trade', color='forestgreen')
    agedirt.add_node('heretic', label='Heretic with Profane Wand Trade')
    agedirt.add_node('librarian', label='Librarian with Glass + Book Trade')
    agedirt.add_node('beekeeper', label='Beekeper with Simmering Comb Trade')

    agedirt.add_edge('die', 'mobfarm', label='dirt')
    agedirt.add_edge('mobfarm', 'mdi', label='infernal mobs')
    agedirt.add_edge('mobfarm', 'mdu', label='infernal mobs')
    agedirt.add_edge('mobfarm', 'mde', label='infernal mobs')
    agedirt.add_edge('mdi', 'ctl')
    agedirt.add_edge('mdu', 'ctl')
    agedirt.add_edge('mde', 'ctl')
    agedirt.add_edge('mobfarm', 'czv', label='zombie villager')
    agedirt.add_edge('mobfarm', 'czv', label='witch weakness potion entity', style='dashed')
    agedirt.add_edge('ctl', 'czv', label='splash weakness potion', style='dashed')
    agedirt.add_edge('mdu', 'czv', label='golden apple')
    agedirt.add_edge('czv', 'sapling', label='villager')
    agedirt.add_edge('czv', 'heretic', label='villager')
    agedirt.add_edge('czv', 'librarian', label='villager')
    agedirt.add_edge('czv', 'beekeeper', label='villager')

    agewood = G.add_subgraph(name='cluster_agewood', label='WOOD AGE')
    agewood.add_node('crops', label='Crossbreed Crops')

    G.add_edge("sapling", "crops", label="wood", color='tomato')

    # Capitalize to match "terminal" theme
    for node in G.nodes():
        existing_attr = node.attr.to_dict()
        node.attr.update({'label': str.upper(existing_attr['label'])})
    for edge in G.edges():
        existing_attr = edge.attr.to_dict()
        edge.attr.update({'label': str.upper(existing_attr['label'])})

    G.draw('test.png', prog='dot')

    # agedirt: Dirt Age {
    #     die: Die
    #     mobfarm: Make Mob Spawning Platform/Farm
    #     mdi: "[Infernal Mobs] Infernal Mob Drops"
    #     mdu: "[Infernal Mobs] Ultra Mob Drops"
    #     mde: "[Infernal Mobs] Elite Mob Drops"
    #     ctl: Common Thaumcraft Lootbag
    #     czv: Convert Zombie Villager
    #     sapling: Farmer or Lumberjack with Sapling Trade {
    #         style: { stroke: forestgreen }
    #     }
    #     heretic: Heretic with Profane Wand Trade
    #     librarian: Librarian with Glass + Book Trade
    #     beekeeper: Beekeper with Simmering Comb Trade

    #     die -> mobfarm: dirt
    #     mobfarm -> mdi: infernal mobs
    #     mobfarm -> mdu: infernal mobs
    #     mobfarm -> mde: infernal mobs
    #     mdi -> ctl
    #     mdu -> ctl
    #     mde -> ctl
    #     mobfarm -> czv: zombie villager
    #     mobfarm -> czv: witch weakness potion entity {
    #         style: { stroke-dash: 3 }
    #     }
    #     ctl -> czv: splash weakness potion {
    #         style: { stroke-dash: 3 }
    #     }
    #     mdu -> czv: golden apple
    #     czv -> sapling: villager
    #     czv -> heretic: villager
    #     czv -> librarian: villager
    #     czv -> beekeeper: villager
    # }

    # agewood: Wood Age {
    #     crops: Crossbreed Crops
    #     grass: Make Grass from IC2 Weeds
    #     passive: Passive Mob Spawning
    #     bed: Skip Night (Bed)
    #     copper: "[Crops] Copper Oreberry or Cyprium"
    #     tin: "[Crops] Tin Oreberry or Stagnium"
    #     craft: Crafting Table
    #     cobble: Mine Cobblestone
    #     drowning: Spawn Drowning Creeper
    #     furnace: Craft Furnace
    #     stone: Smelt Stone
    #     mortar: Craft Mortar
    #     bronze: Mix and Smelt Bronze
    #     tank: Craft XP Drain and Railcraft Iron Tank {
    #         style: { stroke: forestgreen }
    #     }
    #     researchtable: Craft Research Table
    #     gttools: Earliest GT Tools

    #     crops -> grass: weeds
    #     grass -> passive: grass
    #     passive -> bed: wool
    #     crops -> copper
    #     crops -> tin
    #     craft -> cobble: tools
    #     drowning -> cobble: cobblestone
    #     cobble -> furnace: cobblestone
    #     furnace -> stone: furnace
    #     cobble -> stone: cobblestone
    #     stone -> mortar: stone
    #     mortar -> bronze: mortar
    #     copper -> bronze: copper
    #     tin -> bronze: tin
    #     bronze -> tank: bronze
    #     gttools -> crops: tools
    #     stone -> gttools
    #     gttools -> researchtable
    # }
    # agedirt.sapling -> agewood.crops: wood {
    #     style: { stroke: tomato }
    # }
    # agedirt.sapling -> agewood.craft: wood {
    #     style: { stroke: tomato }
    # }
    # agedirt.mobfarm -> agewood.craft: flint {
    #     style: { stroke: tomato }
    # }
    # agedirt.mobfarm -> agewood.tank: iron {
    #     style: { stroke: tomato }
    # }
    # agedirt.heretic -> agewood.researchtable: profane wand {
    #     style: { stroke: tomato }
    # }

    # agexp: Pre-LV XP Bucket {
    #     xpbucket: XP Bucket Crafting
    #     alloysmelter: Steam Alloy Smelter
    #     bctank: Craft BC Tank
    #     piston: Craft Piston
    #     rubber: Craft Rubber Bar
    #     cokeoven: Coke Oven
    #     compressor: Steam Compressor
    #     scribing: Craft Scribing Tools
    #     research: Perform Thaumcraft Research
    #     lazullia: Research Lazullia
    #     lapisplates: Obtain Lapis Lazuli Plates
    #     bbf: Bricked Blast Furnace
    #     hobbyist: Hobbyist Steam Engine
    #     centrifuge: Forestry Centrifuge
    #     squeezer: Forestry Squeezer
    #     simmering: Process Simmering Combs
    #     lava: Process Phosphor into Lava
    #     smeltery: TC Smeltery {
    #         style: { stroke: forestgreen }
    #     }
    #     lvmotor: Craft LV Motors

    #     xpbucket -> alloysmelter: redstone
    #     alloysmelter -> bctank: obsidian glass
    #     xpbucket -> bctank: obsidian
    #     alloysmelter -> piston: red alloy
    #     xpbucket -> cokeoven: clay dust
    #     cobble -> cokeoven: sand
    #     xpbucket -> rubber: sulfur\nrubber
    #     piston -> compressor: piston
    #     rubber -> scribing: rubber
    #     scribing -> research: scribing tools
    #     research -> lazullia
    #     lazullia -> lapisplates: lapis dust
    #     compressor -> lapisplates: compressor
    #     xpbucket -> bbf: gypsum\ncalcite\nquartz sand\nclay dust\nstonedust
    #     compressor -> bbf: firebrick
    #     bbf -> hobbyist: steel
    #     bbf -> centrifuge: steel
    #     bbf -> squeezer: steel
    #     lapisplates -> hobbyist: lapis plate
    #     hobbyist -> simmering: RF
    #     hobbyist -> lava: RF
    #     simmering -> lava: phosphor
    #     centrifuge -> simmering: centrifuge
    #     squeezer -> lava: squeezer
    #     lava -> smeltery: lava
    #     rubber -> lvmotor: rubber
    #     xpbucket -> lvmotor: copper\niron\nredstone
    #     lvmotor -> centrifuge: motor
    #     lvmotor -> squeezer: motor
    # }
    # agewood.tank -> agexp.xpbucket: filled XP bucket {
    #     style: { stroke: tomato }
    # }
    # agedirt.mobfarm -> agexp.scribing: glass bottle (witch, rare drops)\nfeather (sniper skeleton)\nink sac (various mobs) {
    #     style: { stroke: tomato }
    # }
    # agewood.researchtable -> agexp.research: research table {
    #     style: { stroke: tomato }
    # }
    # agedirt.librarian -> agexp.research: bookshelf {
    #     style: { stroke: tomato }
    # }
    # agewood.drowning -> agexp.bbf: water {
    #     style: { stroke: tomato }
    # }
    # agedirt.beekeeper -> agexp.lava: simmering comb {
    #     style: { stroke: tomato }
    # }

    # agelv: LV Age {
    #     ball: Ball Mold
    # }
    # agexp.smeltery -> agelv.ball: smeltery {
    #     style: { stroke: tomato }
    # }