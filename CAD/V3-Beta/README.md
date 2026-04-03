# V3 Beta Naming Convention

To facilitate a future toolhead configurator, all parts in this directory follow a strict naming convention.

## File Format
`[Component]_[Hotend]_[Extruder]_[Blower]_[Detail]_[Version].step`

## Components
- **Bodies**: The main integrated frame of the toolhead.
- **Ducts**: Cooling ducts specific to the blower type (7040 or 9290).
- **Mounts**: Gantry and rail interface parts (e.g., belt clips for MGN12 or MGN9).
- **Fan-Mounts**: Mounts for the hotend cooling fan (e.g., 2510 fans).
- **Supports**: Structural supports for ducts or other hardware.

## Example
`body_goliath-chcxl_sherpa-mini_9290_v3.step`
- **Component**: body
- **Hotend**: goliath-chcxl
- **Extruder**: sherpa-mini
- **Blower**: 9290
- **Version**: v3

---
Refer to `HARDWARE_NOTES.md` for specific compatibility details.
