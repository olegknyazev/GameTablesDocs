---
parent: Reference
nav_order: 3
---
# Arrays

Game Tables can apply values to array properties. In Unity, this includes both C# arrays (`T[]`) and `List<T>` fields. Both appear as expandable lists in the Inspector and are handled identically by Game Tables. This page describes how to reference array elements in headers and how Game Tables updates those arrays when a table is applied.

## Referencing Array Elements

To refer to an array element, use square brackets after the property name:

- DamageByLevel**[2]**
- FirePatterns**[1]**.Offset.X

Like in C#, arrays in Game Tables are zero-based.

Arrays can be nested up to any depth:

- Weapon**[0]**.Level**[1]**.Damage

Indices can appear in [row headers, column headers]({{ site.baseurl }}{% link reference/header_format.md %}), or both—see [Wildcard Indices](#wildcard-indices) for an example.

## Wildcard Indices

Specifying indices for every element of an array can be cumbersome and error-prone. This is why Game Tables provides a shortcut syntax for referencing multiple array elements at once. To do so, append the `*` symbol after the index number to form a *wildcard index*:

- DamageByLevel**[2*]**
- FirePatterns**[1*]**.Offset.X

The index number can be omitted entirely, in which case zero is assumed. So the following notations are equivalent:

- Level**[0*]**
- level**[*]**

When a wildcard index is used in either a row or a column header, all subsequent *empty* header cells are treated as a continuation of the same array:

|          | Flag Colors[*] |           |        | Primary Language |
|:---------|---------------:|----------:|-------:|-----------------:|
| Japan    | White          | Red       |      - | Japanese         |
| Germany  | Black          | Red       | Yellow | German           |

The above table is interpreted as follows:

- Japan / Flag Colors = [White, Red]
- Japan / Primary Language = Japanese
- Germany / Flag Colors = [Black, Red, Yellow]
- Germany / Primary Language = German

| The above assumes that the *No Value Marker* property is set to "**-**". |

Within a wildcard run, each cell's index is determined by its offset from the wildcard cell: the first cell takes the wildcard's base index, the second takes base + 1, and so on. A *No Value Marker* leaves the corresponding position unwritten. An empty cell, by contrast, is treated as a regular value, and its effect depends on the target [data type]({{ site.baseurl }}{% link reference/data_types.md %}).

You can use wildcards in both row and column headers simultaneously to express two-dimensional data:

|           | Enemies To Spawn[*] |           |          |
|:----------|--------------------:|----------:|---------:|
| Waves[*]  | Zombie              |           |          |
|           | Zombie              | Spider    |          |
|           | Zombie              | Spider    | Gargoyle |

The above example produces three elements in the *Waves* array, each of which contains up to three *Enemies To Spawn*.

## Array Update Policy

When applying a table, Game Tables needs to decide how to combine the values from the table with the existing contents of the target array. This behavior is controlled by the [Array Update Policy]({{ site.baseurl }}{% link reference/inspector.md %}#array-update-policy) property on the GameTable, which has two modes.

### Replace Whole Array

This is the default mode. Game Tables replaces the entire content of the referenced array. The array's size becomes equal to the maximum index used in the table. If the table does not contain values for some intermediate indices, those slots are filled with the default value for the property's [data type]({{ site.baseurl }}{% link reference/data_types.md %}).

Consider the following table:

|          | Array[1] | Array[3] |
|:---------|---------:|---------:|
| Prefab   | 8        | 9        |

After applying this table, Prefab's *Array* property will contain the following elements: **0**, **8**, **0**, **9**.

In *Replace Whole Array* mode, the result does not depend on the previous state of the property: applying the same table always produces the same array.

### Replace Specific Elements

In this mode, Game Tables replaces only the elements referenced in the spreadsheet. Suppose that, before applying the table above, Prefab's *Array* property contained the elements **1**, **2**, **3**, **4**, **5**. After applying the table, it will contain *1*, **8**, *3*, **9**, *5*.

If a referenced index lies beyond the current end of the array, the array grows to accommodate it. Any intermediate slots between the previous end and the new index are filled with the default value for the property's [data type]({{ site.baseurl }}{% link reference/data_types.md %}). For example, if the table above had also assigned **7** to Array[6], the resulting array would be *1*, **8**, *3*, **9**, *5*, **0**, **7**.
