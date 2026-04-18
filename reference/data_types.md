---
parent: Reference
nav_order: 2
---
# Data Types
Game Tables can apply data to properties of various types: integer and floating point numbers, vectors, colors, and so on. This page describes the format of all supported data types and explains how types are processed.

| Game Tables relies on Unity's serialization to apply properties to Prefabs and ScriptableObjects. So all the types listed here have corresponding types in the underlying system. See [SerializedPropertyType](https://docs.unity3d.com/ScriptReference/SerializedPropertyType.html) for more details. |

## Cell Values Interpretation
When importing data, Game Tables treats the input as string data, regardless of any metadata that might be available from the source (e.g. if a cell has a numeric type in Google Sheets). The string value of each cell is interpreted based on the target property type:

![Data Types Conversion]({{ site.baseurl }}{% link reference/data_types_conversion.png %})

As illustrated above, the cell value "12.5" can be applied to a float or string property, but applying it to a boolean property would be an error.

This approach normalizes different types of data sources, makes it possible to store compound values in a single cell (e.g. vectors), and avoids a certain class of error (when a number is stored in a text cell). The drawback is that it depends on locale-specific formatting settings; see [Regional Settings and Formatting](#regional-settings-and-formatting) for details.

## Regional Settings and Formatting
Because Game Tables interprets the source data as strings, it is important to take regional settings into account when authoring data for import. The textual representation of some data, for example floating point numbers, can differ from one language to another. For simplicity and to reduce the chance of mistakes, Game Tables requires that all source data is formatted in the USA locale (`en_US`). If you import from Google Sheets, the target spreadsheet should be set to the corresponding locale (you can check it in *File / Settings*). If you import from CSV, the CSV should be formatted according to the USA formatting rules, e.g. it should use the dot as a decimal point separator.

## Compound Properties
Compound properties are properties that consist of more than one child element. Vectors and quaternions are examples of compound types, but there are more of them defined in Unity and, most likely, in your project. By default, compound properties are displayed as expandable fields in the Inspector. With the exception of the built-in compounds described on this page, you cannot specify a value for the entire compound property in a single table cell, but you can specify values for its components. To refer to a component of a compound property, use a dot delimiter:
- AttackParameters.Damage
- AttackParameters.Spread.Y
- Rotation.Y

| Keep in mind that you cannot specify both the entire vector (or another built-in compound) and any of its components in the same spreadsheet. |

C# types: structs or classes marked with the [Serializable](https://docs.unity3d.com/ScriptReference/Serializable.html) or [SerializeReference](https://docs.unity3d.com/ScriptReference/SerializeReference.html) attribute.

## Supported Types
### Strings
A string value is used as-is; no trimming or other transformations take place.

C# type: [string](https://docs.microsoft.com/en-us/dotnet/api/system.string).

### Booleans
The boolean type has two values. "True" and "yes" are interpreted as true, "false" and "no" are interpreted as false. Case and whitespace are ignored. Examples of booleans:
- Yes
- no
- TRUE

C# type: [bool](https://docs.microsoft.com/en-us/dotnet/api/system.boolean).

### Integer Numbers
An integer number can contain a comma as an optional thousands separator. Examples of integer numbers:
- 24,700
- 56

C# types: [int](https://docs.microsoft.com/en-us/dotnet/api/system.int32), [long](https://docs.microsoft.com/en-us/dotnet/api/system.int64). If the value is too large for the target type, an error occurs.

### Floating Point Numbers
Floating point numbers use the dot as a decimal separator. They can also be written in exponential form, also known as scientific notation. Examples of floating point numbers:
- 3.5
- 2,500.49
- 0.471E+2
- -2.6E-3

C# types: [float](https://docs.microsoft.com/en-us/dotnet/api/system.single), [double](https://docs.microsoft.com/en-us/dotnet/api/system.double). If the value cannot be represented in the target type without loss, it is clamped.

### Vectors
Vectors are collections of integer or floating point numbers. Game Tables expects a semicolon or comma as a component separator.

| A semicolon must be used if any vector component includes a thousands separator. |

There are 5 vector types in Unity that differ by the component type (integer or floating point) and the number of components: Vector2, Vector2Int, Vector3, Vector3Int and Vector4. You can express any of them in Game Tables.

A vector can optionally be enclosed in parentheses.

Examples of vectors:
- 1, 2, 3
- 4.5, -5, 17
- 4,500; 2,000; 16
- (0.567E+2; 15.6; -2; 0.0)

Vector properties are [compound properties](#compound-properties), which means that you can refer to components of a vector separately. For example, if you have a Vector3 property named Position, you can use Position.X to set its X component.

C# types: [Vector2](https://docs.unity3d.com/ScriptReference/Vector2.html), [Vector2Int](https://docs.unity3d.com/ScriptReference/Vector2Int.html), [Vector3](https://docs.unity3d.com/ScriptReference/Vector3.html), [Vector3Int](https://docs.unity3d.com/ScriptReference/Vector3Int.html), [Vector4](https://docs.unity3d.com/ScriptReference/Vector4.html).

### Quaternions (Rotations)
A quaternion is expressed in Game Tables the same way as in the Unity Editor—as Euler angles. It is a triplet of numbers describing the rotation around each of the three axes: pitch (X), yaw (Y), roll (Z). As in Unity, the rotation is specified in degrees. The format of a quaternion is the same as that of a three-component floating-point vector.

Examples of quaternions:
- 0, 45, 0
- (5.63; 120; -31.2)

Quaternion properties are [compound properties](#compound-properties), which means that you can refer to components of a quaternion separately. For example, if you have a Quaternion property named Rotation, you can use Rotation.Y to set its Y component (yaw).

C# type: [Quaternion](https://docs.unity3d.com/ScriptReference/Quaternion.html).

### Colors
There are several forms that can represent colors in Game Tables.

1. First of all, a color can be expressed as a three- or four-component vector. The components are floating point numbers from 0 to 1 which define the value of red, green and blue channels respectively. If the fourth component is present, it defines the alpha (opacity) component of the color.

2. Alternatively, a color can be expressed in hexadecimal form, also known as web colors. It can contain an optional alpha value. Each color channel can be represented by either one or two hexadecimal digits. More detailed information about the web color format can be found on [this page](https://docs.unity3d.com/ScriptReference/ColorUtility.TryParseHtmlString.html).

3. The last option is to use well-known color names like "red", "cyan", "blue", etc. The full list of supported color names can be found [here](https://docs.unity3d.com/ScriptReference/ColorUtility.TryParseHtmlString.html).

Examples of colors:
- 1, 0, 0
- (0.5; 1; 0; 0.75)
- #56FE20
- magenta

C# types: [Color](https://docs.unity3d.com/ScriptReference/Color.html), [Color32](https://docs.unity3d.com/ScriptReference/Color32.html). If the floating-point value cannot be represented in the target type without loss, it will be clamped.

### Rectangles
A rectangle is determined by four integer or floating point numbers: x, y, width and height. To set a rectangle value from a table, write four numbers separated by a semicolon or comma.

Examples of rectangles:
- 0, 0, 100, 50
- 15.2; 0; 57.92; 560

Rectangle properties are [compound properties](#compound-properties). Floating point rectangles have properties Center and Extent. Integer rectangles have properties Position and Size. Each of these properties is itself a two-component vector. So, given a floating-point rectangle property named Area, all of the following property names are valid:
- Area
- Area.Center
- Area.Center.X

C# types: [Rect](https://docs.unity3d.com/ScriptReference/Rect.html), [RectInt](https://docs.unity3d.com/ScriptReference/RectInt.html).

### Enumerations
Enumerated properties accept values from a predefined set. To specify the value for an enumerated property, just write the name of the value. Some enumerations can have multiple values (`[Flags]` enums in C# terms). To specify several values for a flags property, list the values separated by commas. Case and whitespace are ignored when comparing names.

Examples of enumerations:
- Off
- Blend Probes
- Walk, Run, Swim

C# types: [Enum](https://docs.microsoft.com/en-us/dotnet/api/system.enum) and derived classes. Usually declared using the `enum` keyword.

### Asset References
Sometimes one Prefab or Scriptable Object references another. To set up such a property from a spreadsheet, just write the name of the referenced Prefab. The referenced Prefab is searched for in the same folder where Game Tables looks for the target object (the object whose property is being processed). This folder is controlled by [Search Path]({{ site.baseurl }}{% link reference/inspector.md %}#search-path).

| As with [Prefab Names]({{ site.baseurl }}{% link reference/header_format.md %}#prefab-name), asset references should be simple names without any hierarchy. It means that you cannot, for example, specify "Explosions / BigOne" as reference, you have to write just "BigOne" (which may be ambiguous). So you have to either give more specific names to assets or set a more restrictive *Search Path*. |

Examples of asset references:
- Big Explosion
- Level 1 Settings

C# types: [UnityEngine.Object](https://docs.unity3d.com/ScriptReference/Object.html) and derived classes.

### Layer Masks
A [layer](https://docs.unity3d.com/Manual/Layers.html) mask allows you to specify a set of layers that can be used to filter physics collisions and raycasts, among other things. To set a layer mask property from a spreadsheet, list the layer names separated by commas or semicolons:
- Water
- Enemy, EnemyProjectiles
- Terrain; Buildings

An empty cell means an empty set—a set containing no elements.

| As in any other place in Game Tables, layer names are case- and whitespace-insensitive, so Water and waTER refer to the same layer. If your project contains layers whose names clash when compared in a case- and whitespace-insensitive way, you will get an error when applying the table. In this case you should either not use Game Tables to specify these layers, or rename layers in the [Tags and Layers](https://docs.unity3d.com/Manual/class-TagManager.html) window. |

C# type: [LayerMask](https://docs.unity3d.com/ScriptReference/LayerMask.html).
