---
grand_parent: Reference
parent: Headers Format
nav_order: 2
---
# Matching Rules

There are several general rules that Game Tables follow when searching for an object's property.

All the search process may be divided into two phases:
1. Look for a matching [Prefab](https://docs.unity3d.com/Manual/Prefabs.html) or [ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html) in Project tree. The only header element that's considered at this stage is *Prefab Name*.
2. Look for a matching property of some of components and game objects. *Game Object Name*, *Component Type* and *Property Path* are considered at this stage.

During any of the phases if Game Tables finds more than one matching entity, an error occurs and the update process interrupts.

## Case and Whitespace Insensitivity

All the path elements are both case- and whitespace insensitive. When looking for an object or its property, Game Tables converts both actual property name and the name, specified in a table, to lower registry and removes all the whitespace. After this comparison happen. So, all the following property paths actually refer the same property:
- Cluster Mine / \<Spreading Spawner\> Targets [ 0 ] . Offset . X
- ClusterMine/\<SpreadingSpawner\>Targets[0].Offset.X
- clustermine/\<spreadingspawner\>targets[0].offset.x

## Partial Matching

When looking for a property Game Tables performs partial matching. That means that the actual property path may be not exactly equal to the property path specified in row and column headers. It's enough if just a part of the property path matches while it's a unique match, i.e. exactly one property in the whole Prefab (or ScriptableObject) matches.

You may think of this process as if Game Tables collects all the paths of actual properties of the target object and then matches them all against the sought-for property. When matching a property it starts from the rightmost part of a property path. For example, consider that we have a Prefab with the following properties (across all the componented of all the game objects):

1. Root \<Transform\> Position
2. Weapon \<Shooter\> Pattern.Offset.X
3. Weapon \<Damageable\> HitPoints
4. Hull \<Damageable\> HitPoints

We can refer to the second property by any of these paths:

- Weapon \<Shooter\> Pattern.Offset.X
- \<Shooter\> Pattern.Offset.X
- Pattern.Offset.X
- Offset.X

Or even just X (but that'a a bad idea in real world because each game object has a Transform component with more than one X properties). But we cannot refer property 3 by just HitPoints because it's ambiguous: HitPoints may refer both the third of fourth property.

So, a general rule of partial matching is that you may omit the leftmost part of the property path until it's ambiguous.
