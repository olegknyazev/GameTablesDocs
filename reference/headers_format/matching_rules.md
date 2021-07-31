---
grand_parent: Reference
parent: Headers Format
title: Matching Rules
nav_order: 2
---
# Matching Rules

## Case- and Whitespace Sensitivity

All the path elements are both case- and whitespace insensitive. When looking for an object or its property, Game Tables converts both actual property name and the name, specified in a table, to lower registry and removes all the whitespace. After this comparison happen. So, all the following property paths actually refer to the same property:
- `Cluster Mine / <Spreading Spawner> Targets[0].Offset.X`
- `ClusterMine/<SpreadingSpawner>Targets[0].Offset.X`
- `clustermine/<spreadingspawner>targets[0].offset.x`

## Partial Matching

When matching a property path against an actual objects and properties ...

## Wildcard Indexers