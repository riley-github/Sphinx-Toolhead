# Voron Versions

Sphinx **tLW** builds for **Voron**-style carriages, packaged one zip per hotend.

Each archive is self-contained — download the one matching your hotend and print everything inside it. There is no need to mix files between archives.

---

## 📦 Available Builds

| Hotend | File |
|---|---|
| Dragon Ace MZE | `voron_sphinx_tLW_dragonAceMZE_sherpaMini.zip` |
| Dragon Ace Volcano | `voron_sphinx_tLW_DragonAceVolcano_sherpaMini.zip` |
| Goliath / CHC XL | `voron_sphinx_tLW_goliath_chcXL_sherpaMini.zip` |
| Rapido X / Rapido UHF | `voron_sphinx_tLW_rapidoXandUHF_sherpaMini.zip` |
| Tricorn | `voron_sphinx_tLW_tricorn_sherpa_mini.zip` |

All builds are for the **Sherpa Mini** extruder.

---

## 🧩 What's in Each Zip

Seven STEP files — six shared across every build, plus one hotend-specific main body:

| Part | Notes |
|---|---|
| `sphinx_main_body_<hotend>` | The only part that changes between archives |
| `left_clamp_voron` | Voron carriage mount |
| `right_clamp_voron` | Voron carriage mount |
| `extruder_mount` | Sherpa Mini |
| `sherpa_bracket` | Sherpa Mini |
| `mid_support` | |
| `rear_duct` | Part cooling |

The clamps are what make these Voron-specific. If you are on a Monolith carriage, use the [Monolith Versions](../Monolith%20Versions) folder instead — those ship `left_clamp_monolith` / `right_clamp_monolith` in place of these.

---

Generally Settings
- 8 walls
- 8 top / bottom layers
- 40% infill

For best COM results try to have slicer masses for each part close to what is listed below:
| Part | Slicer Mass Estimates |
|---|---|
| `sphinx_main_body_<hotend>` | 90g |
| `left_clamp_monolith` | 1-2g |
| `right_clamp_monolith` | 1-2g |
| `extruder_mount` | 20g |
| `sherpa_bracket` | 17g |
| `mid_support` | 6-7g |
| `rear_duct` | 34g |

Any filled ABS or better is recommended.  

---

See the [main README](../README.md) for supported hardware, cooling notes, and input shaper results.
