---
parent: Reference
nav_order: 3
---
# Data Types
Game Tables can apply data to properties of various types: integer and floating point numbers, vectors, color. This section describes format of all the supported data types.

| Game Tables uses underlying Unity's serialization to apply properties to Prefabs and ScriptableObjects. So all the types listen here have corresponding types in the underlying system. See [SerializedPropertyType](https://docs.unity3d.com/ScriptReference/SerializedPropertyType.html) for more details. |

## Localization Settings
Format of some data, for example floating point numbers, may differ from one language to another. To simplify things and reduce chances for mistakes Game Tables requires that all the source data is formatted in USA locale (en_US). If you import from Google Sheets, the target spreadsheet should have according locale (you may check it out in the File / Spreadsheet Settings dialog). If you import from CSV, the CSV should be formatted in USA locale, i.e. it should use dot as decimal point separator.

## Strings
String is used as is, no trimming nor other transformations take place when applying a cell value to a string property.

## Booleans
Boolean has two values. "True" and "yes" are interpreted as true, "false" and "no" are interpreted as false. When checking values case and whitespace is ignored. Examples of booleans:
- Yes
-  no
- TRUE

## Integer Numbers
Integer number may contain comma as optional thousands separator. Examples of integer numbers:
- 24,700
- 56

## Floating Point Numbers
Floating point number use dot as decimal separator. It also may be written in exponential form also known as scientific notation. Examples of floating point numbers:
- 3.5
- 2,500.49
- 0.471E+2
- -2.6E-3

## Vectors
Vectors are collections of integer or floating point numbers. Game Tables expects semicolon or comma as a component separator. Semicolon is a safer option because it allows you to still use commas as thousand separators.

There are 5 combinations of vector types in Unity which differ by type of component (integer or floating point) and the number of components: Vector2, Vector2Int, Vector3, Vector3Int and Vector4. You may express any of them in Game Tables.

Vector may be optionally enclosed in brackets.

Examples of vectors:
- 1, 2, 3
- 4.5, -5, 17
- 4,500; 2,000; 16
- (0.567E+2; 15.6; -2; 0.0)

## Quaternions (Rotations)
Quaternion in Game Tables is expressed in the same way as in Unity Editor — as euler angles. It's a triplet of numbers each of which determines rotations around a specific axis: pitch, yaw, roll. As in Unity, rotation is specified in degrees. The format of a quaternion is equal to the format of three-component floating-point vector.

Examples of quaternions:
- 0, 45, 0
- (5.63; 120; -31.2)

## Colors
There are several forms that colors in Game Tables may look like. 

1. First of all, a color may be expressed as either three or four component vector. Components are floating point numbers from 0 to 1 which define the value of red, green and blue channels. If fourth component is present, it defines the opacity of a color.

2. Alternatively, color may be expressed in hexademical form also known as web colors. It may contain optional alpha. Each color channel may be composed from either one or two digits. More detailed information about web color format you may find on [this page](https://docs.unity3d.com/ScriptReference/ColorUtility.TryParseHtmlString.html).

3. The last option is known color names like red, cyan, blue, etc. The full list of supported color names may found [here](https://docs.unity3d.com/ScriptReference/ColorUtility.TryParseHtmlString.html).

Examples of colors:
- 1, 0, 0
- (0.5; 1; 0; 0.75)
- #56FE20
- magenta

## Enumerations

## Asset References
