---
grand_parent: Reference
parent: Headers Format
nav_order: 3
---
# Arrays

Game Tables lets you to apply properties to arrays. To refer an array element square brackets are used:

- DamageByLevel**[2]**
- FirePatterns**[1]**.Offset.X

Array may be nested up to any depth:

- Weapon**[0]**.Level**[1]**.Damage

You may use arrays in both [row and column headers]() and even in both row and column headers simultaneously:

|             | EnemiesToSpawn[0]  | EnemiesToSpawn[1]   |
|:------------|-------------------:|--------------------:|
| Level[0]    |             Zombie |              Spider |
| Level[1]    |             Spider |            Gargoyle |

After applying the upper table the following property values will be applied:

- Level[0].EnemiesToSpawn[0] = Zombie
- Level[0].EnemiesToSpawn[1] = Spider
- Level[1].EnemiesToSpawn[0] = Spider
- Level[1].EnemiesToSpawn[1] = Gargoyle

This feature works especially good with [Wildcard Indexes](#wildcard-indexes).

Like in Unity, arrays in Game Tables are zero-based.

## Array Update Modes

By default, when applying table, Game Tables replaces the whole content of the referenced array. It does mean that after the update the array contains only the values specified in the table. The size of array is equal to the maximum index used in a table. If the table does not contain values for some of intermediate values, they are filled with default value appropriate for property's [data type]().

Consider the following table:

|          | Array[1] | Array[3] |
|:---------|---------:|---------:|
| Prefab   | 8        | 9        |

After applying, Prefab's Array property will contain the following elements: **0**, **8**, **0**, **9**. 

This behaviour may be overriden by the *Array Update Policy* property. The described above behaviour coressponds to *Replace Whole Array* mode which is set by default.

The alternative mode is *Replace Specific Elements*. In this mode Game Tables replaces only those elements that are referenced from a table. Suppose that Prefab's Array property had value **1**, **2**, **3**, **4**, **5** before applying the table. Then after applying the table it will have value *1*, **8**, *3*, **9**, *5*.

One important thing that you should know about these update modes is that applying property in *Replace Whole Array* mode is stable: it does not depend on the previous state of the property and the result is always the same.

## Wildcard Indices

Specifying indices for every element of array may be cumbersome and error-prone. So Game Tables provides a shortcut syntax for referring a bunch of array elements at once. To do so, append **\*** symbol after index number in array property:

- DamageByLevel**[2*]**
- FirePatterns**[1*]**.Offset.X

The index number may be ommited entirely, in this case zero will be used. So the following notations are equivalent:

- Level**[0*]**
- level**[*]**

These indices are named wildcard indices. When a wildcard index is used in either row or column header, all the following *empty* header cells are considered as a continuation of this array:

|          | Flag Colors[*] |           |        | Primary Language |
|:---------|---------------:|----------:|-------:|-----------------:|
| Japan    | White          | Red       |      - | Japanesse        |
| Germany  | Black          | Red       | Yellow | German           |

The above table is interpreted as following:

- Japan / Flag Colors = [While, Red]
- Japan / Primary Language = Japanesse
- Germany / Flag Colors = [Black, Red, Yellow]
- Germany / Primary Language = German

| The above supposes that the *No Value Marked* property is set to  "**-**". |

You may use wildcards in both column and row headers in a single table to express two-dimensional data:

|           | Enemies To Spawn[*] |           |          |
|:----------|--------------------:|----------:|---------:|
| Waves[*]  | Zombie              |           |          |
|           | Zombie              | Spider    |          |
|           | Zombie              | Spider    | Gorgoyle |

The above example produces three elements in *Waves* array each of which contains up to three *Enemies To Spawn*.