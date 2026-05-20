# Documentation Style

| Element | Style |
|---|---|
| Inspector property names (e.g., Source, Search Path) | **Bold** on first mention per page; plain afterward; `[Property](...)` link when cross-referencing |
| Inspector enum/option values (e.g., Object Per Row, Islands) | *Italic* |
| Buttons, menu items, menu paths (e.g., Apply Game Table, File / Save Project) | *Italic* |
| Asset paths (`Assets/Prefabs/Units`, `Packages/Game Tables/Editor`) | `` `code` `` |
| Asset names referenced in prose (`Balance_Original`, `Example` scene) | `` `code` `` |
| Unity concept names (Prefab, GameObject, ScriptableObject, Inspector, Console window) | Linked on first mention per page, plain afterward |
| Unity API types (`Vector3`, `Quaternion`, `Rect`) | `` `code` `` always; linked on first mention as `` [`Vector3`](...) `` |
| C# code symbols (`T[]`, `[Flags]`, `enum`, `string`) | `` `code` ``; link C# stdlib types as `` [`string`](...) `` |
| Cell values shown in prose (`12.5`, `yes`) | `` `code` `` (no surrounding quotes) |
| Property path — literal example (`Position.X`, `Player / Gun / <Clip> Bursts[0]`) | `` `code` `` |
| Header-component placeholder in syntax (Prefab Name, Component Type, Property Path) | *Italic*, capitalized |

To highlight a fragment inside any `` `code` `` span, fall back to a single inline `<code>` with `<strong>` inside, e.g. `<code>DamageByLevel<strong>[2]</strong></code>` — backtick spans can't be broken without splitting the pill.

Inside example tables whose cells are themselves header or path fragments, leave cells as plain text — the table structure already provides the separation, and per-cell `` `code` `` formatting turns the table into a wall of pills.

Em-dashes have no surrounding spaces.
