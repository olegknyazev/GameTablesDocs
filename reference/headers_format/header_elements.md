---
grand_parent: Reference
parent: Headers Format
nav_order: 1
---
# Header Elements

There are four types of elements that may be used in row and column headers: *Prefab Name*, *Game Object Name*, *Component Type* and *Property Path*.

An important thing is that these elements *always* go in the specified order, i.e. you cannot put *Component Type* after *Property Path*. This rule is applicable even when these elements are split between row and column headers. In this case the row header is considered a prefix for the column header.

It does not matter for Game Tables how exactly you split the required elements between row and column headers while all the restrictions listed in [Headers Format]({{ site.baseurl }}{% link reference/headers_format/index.md %}) are met. So, the following compositions actually refer the same property:

| Row Header                      | Column Header                       |
|--------------------------------:|:------------------------------------|
| Player / Gun \<Clip\> Bursts[0] | Pellet Count                        |
| Player / Gun \<Clip\>           | Bursts[0].Pellet Count              |
| Player                          | Gun \<Clip\> Bursts[0].Pellet Count |

| Keep in mind, that meaning of row and column headers may be flipped by setting [Orientation]({{ site.baseurl }}{% link reference/inspector.md %}#orientation) property of a GameTable to *Object Per Column*. |

The only required elements that any cell should contain are *Prefab Name* and *Property Path*.

## Prefab Name

*Prefab Name* locates a [Prefab](https://docs.unity3d.com/Manual/Prefabs.html) or a [ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html) inside the project. Game Tables searches for this name recursively starting from the directory specified in the [Search Path]({{ site.baseurl }}{% link reference/inspector.md %}#search-path) property of a GameTable object.

Requirements:
- Prefab Name should be a simple name, it cannot contain any hierarchy.
- Prefab Name must be specified in a [Row Header]({{ site.baseurl }}{% link reference/headers_format/index.md %}#row-headers).

Examples:
* Burst Rifle
* Level 1 AI Settings

## Game Object Name

*Game Object Name* path locates a [GameObject](https://docs.unity3d.com/Manual/GameObjects.html) inside a [Prefab](https://docs.unity3d.com/Manual/Prefabs.html). Game Tables searches for this name recursively starting from the Prefab's root GameObject.

Requirements:
- Game Object Name is only applicable to Prefabs, it should not be used in cells that target ScriptableObjects.
- Game Object Name should be a simple name, it cannot contain any hierarchy.
- Game Object Name is optional, you may omit it from both row and column headers.

Examples:
* Spawn Point 1
* Muzzle

## Component Type

*Component Type* locates a [Component](https://docs.unity3d.com/Manual/Components.html) inside a [GameObject](https://docs.unity3d.com/Manual/GameObjects.html). Because a GameObject may contain several Components, a simple property name may be ambiguous. So, *Component Type* allows you to specify the exact component type the property should be applied to. When *Game Object Name* is not specified, Game Tables searches for the required component and property combination across all the GameObjects inside a Prefab.

Requirements:
- Component Type is only applicable to Prefabs, it should not be used in cells that target ScriptableObjects.
- Component Type is optional, you may omit it from both row and column header.

*Component Type* should be enclosed in angular brackets:
* \<Rigid Body\>
* \<Enemy Brain\>

## Property Path

*Property Path* locates a specific [property](https://docs.unity3d.com/Manual/EditingValueProperties.html) inside a [Component](https://docs.unity3d.com/Manual/Components.html) or [ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html). *Property Path* may be hierarchical and contain [array]({{ site.baseurl }}{% link reference/headers_format/arrays.md %}) and [wildcard]({{ site.baseurl }}{% link reference/headers_format/arrays.md %}#wildcard-indexers) indexers.

Requirements:
- Property Path (or its suffix) must be specified in a [Column Header]({{ site.baseurl }}{% link reference/headers_format/index.md %}#column-headers).

Property Path may be combined from row and column headers. In this case content of a column header is added to the end of the row header:

| Row Header    | Column Header | Resulted Property Path
|--------------:|:--------------|:------------------------
| Position      | X             | Position.X
| Patterns[0]   | Spread.Power  | Patterns[0].Spread.Power

*You may notice that in some cases the **.** separator was added to the result to distinguish path elements.*

Examples:
* Position.X
* Waves[0].Enemies to Spawn
* Spawn Points[*].Position
