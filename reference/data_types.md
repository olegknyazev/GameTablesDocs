---
parent: Reference
nav_order: 3
---
# Data Types
Game Tables can apply data to properties of various types: integer and floating point numbers, vectors, colors. This section describes format of all the supported data types.

| Game Tables uses underlying Unity's serialization to apply properties to Prefabs and ScriptableObjects. So all the types listen here have corresponding types in the underlying system. See [SerializedPropertyType](https://docs.unity3d.com/ScriptReference/SerializedPropertyType.html) for more details. |

## Regional Settings and Formatting
Format of some data, for example floating point numbers, may differ from one language to another. To simplify things and reduce chances for mistakes Game Tables requires that all the source data is formatted in USA locale (en_US). If you import from Google Sheets, the target spreadsheet should have according locale (you may check it out in the File / Spreadsheet Settings dialog). If you import from CSV, the CSV should be formatted in USA locale, i.e. it should use dot as decimal point separator.

## How Types Are Used
It's important to understand that Game Tables does not try to interpret table cells per se. When importing from either Google Sheets or CSV all the data is just strings. Actual type is determined by the type of the target property. When Game Tables applies a cell to a concrete property it tries to interpret the cell value as a value of the property's type. For example, if you are applying value "true" to a boolean property, then the property will get the truth value. But if you're applying the same cell to a string property, the resulting property will contain "true" string.

## Supported Types
### Strings
String is used as is, no trimming nor other transformations take place when applying a cell value to a string property.

### Booleans
Boolean has two values. "True" and "yes" are interpreted as true, "false" and "no" are interpreted as false. When checking values case and whitespace are ignored. Examples of booleans:
- Yes
-  no
- TRUE

### Integer Numbers
Integer number may contain comma as optional thousands separator. Examples of integer numbers:
- 24,700
- 56

### Floating Point Numbers
Floating point number use dot as decimal separator. It also may be written in exponential form also known as scientific notation. Examples of floating point numbers:
- 3.5
- 2,500.49
- 0.471E+2
- -2.6E-3

### Vectors
Vectors are collections of integer or floating point numbers. Game Tables expects semicolon or comma as a component separator. Semicolon is a safer option because it allows you to still use commas as thousand separators.

There are 5 combinations of vector types in Unity which differ by type of component (integer or floating point) and the number of components: Vector2, Vector2Int, Vector3, Vector3Int and Vector4. You may express any of them in Game Tables.

Vector may be optionally enclosed in brackets.

Examples of vectors:
- 1, 2, 3
- 4.5, -5, 17
- 4,500; 2,000; 16
- (0.567E+2; 15.6; -2; 0.0)

Vector properties are [compound properties](#compound-properties), so you may refer components of a vector separately. For example, if you have a Vector3 property named Position, you can use Position.X to set it's X component.

### Quaternions (Rotations)
Quaternion in Game Tables is expressed in the same way as in Unity Editor — as euler angles. It's a triplet of numbers each of which determines rotations around a specific axis: pitch, yaw, roll. As in Unity, rotation is specified in degrees. The format of a quaternion is equal to the format of three-component floating-point vector.

Examples of quaternions:
- 0, 45, 0
- (5.63; 120; -31.2)

Quaternion properties are [compound properties](#compound-properties), so you may also refer components of a quaternion separately. For example, if you have a Quaternion property named Rotation, you can use Rotation.Y to set it's Y component (yaw).

### Colors
There are several forms that colors in Game Tables may look like. 

1. First of all, a color may be expressed as either three or four component vector. Components are floating point numbers from 0 to 1 which define the value of red, green and blue channels. If fourth component is present, it defines the opacity of a color.

2. Alternatively, color may be expressed in hexademical form also known as web colors. It may contain optional alpha. Each color channel may be composed from either one or two digits. More detailed information about web color format you may find on [this page](https://docs.unity3d.com/ScriptReference/ColorUtility.TryParseHtmlString.html).

3. The last option is known color names like red, cyan, blue, etc. The full list of supported color names may found [here](https://docs.unity3d.com/ScriptReference/ColorUtility.TryParseHtmlString.html).

Examples of colors:
- 1, 0, 0
- (0.5; 1; 0; 0.75)
- #56FE20
- magenta

### Rectangles
Rectangle is determined by four integer or floating point numbers: x, y, width and height. To set a rectangle value from a table, write four numbers separated by a semicolon (or comma).

Examples of rectangles:
- 0, 0, 100, 50
- 15.2; 0; 57.92; 560

Rectangle properties are [compound properties](#compound-properties). Regular (floating-point) rectangles have properties Center and Extent. Integer rectangles have properties Position and Size. All these properties are two-component vectors on its own. So, supposing we have a floating point rectangle property Area, all the following property names are valid:
- Area
- Area.Center
- Area.Center.X

### Enumerations
Enumerated properties can have a value from a predefined set of values. To specify value for an enumerated property, just write the name of value. In Unity some enumerations also lets you to specify more than one value (`[Flags]` enums in C# terms). To specify several values for a flags property, separate names of these values by commas. Case and whitespace is ignored when comparing names. 

Examples of enumerations:
- Off
- Blend Probes
- Walk, Run, Swim

### Asset References
Sometimes one Prefab or Scriptable Object references another. To set up such a property from a table, just write the name of the prefab. The referenced prefab is looked in the same folder where Game Tables looks for the target object (to which we're applying properties). This folder is specified by [Search Path]({{ site.baseurl }}{% link reference/inspector.md %}#search-path) property.

| As with [Prefab Names]({{ site.baseurl }}{% link reference/headers_format/header_elements.md %}#prefab-name), asset references should be simple names without any hierarchy. It means that you cannot, for example, specify "Explosions / BigOne" as reference, you have write just "BigOne" which may be ambiguous. So you have to either give more specific names to assets or set a more restrictive Search Path. |

Examples of asset references:
- Big Explosion
- Level 1 Settings

### Layer Masks
[Layer](https://docs.unity3d.com/Manual/Layers.html) mask allows you to specify a set of layers which may be used to filter collisions, for example. To set a layer mask property from a table, write layers name in a list, using comma or semicolon separators:
- Water
- Enemy, EnemyProjectiles
- Terrain; Buildings

Empty cell means empty set—that's a set containing no elements.

| As in any other place in Game Tables, layer names are case and whitespace insensitive, so Water and waTER means the same layer. If your project contains layers whose names clash when comparing them in case and whitespace insensitive way, you will got an error during the table application. In this case you should either not use Game Tables to specify these layers, or rename layers in [Tags and Layers](https://docs.unity3d.com/Manual/class-TagManager.html) window. |

### Compound Properties
Compound properties are properties that consist of more than one child element. Standard vectors and quaternions are compound types, but there are more of them and your project is likely use many custom compound types. By default compounds are displayed as expandable fields in Inspector. With exception of built-in compounds described in this topic, you cannot specify value for the entire compound property in a single table cell. But you may specify values for components of a compound. To refer a compound's component, use **.** delimeter:
- AttackParameters.Damage
- AttackParameters.Spread.Y
- Rotation.Y

| In C# compound types are struct or classes that are marked with `[Serializable]`. Game Tables also supports polymorphic serialization that's activated by `[SerializeReference]` annotation. |

When speaking on built-in compounds (vectors, quaternions and rectables), keep in mind that you cannot specify both the entire vector and any of its components in tables that are applied together.