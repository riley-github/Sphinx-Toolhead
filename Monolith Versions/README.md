# Monolith Versions

Sphinx **tLW** builds for the **Monolith** carriage, packaged one zip per hotend.

Each archive is self-contained — download the one matching your hotend and print everything inside it. There is no need to mix files between archives.

---

## 📦 Available Builds

| Hotend | File |
|---|---|
| Dragon Ace MZE | `monolith_sphinx_tLW_dragonAceMZE.zip` |
| Dragon Ace Volcano | `monolith_sphinx_tLW_dragonAceVolcano_sherpaMini.zip` |
| Goliath / CHC XL | `monolith_sphinx_tLW_goliath_chcxl_sherpaMini.zip` |
| Rapido X / Rapido UHF | `monolith_sphinx_tLW_rapidoXandUHF_sherpaMini.zip` |
| Tricorn | `monolith_sphinx_tLW_tricorn_sherpaMini.zip` |

All builds are for the **Sherpa Mini** extruder.

---

## 🧩 What's in Each Zip

Seven STEP files — six shared across every build, plus one hotend-specific main body:

| Part | Notes |
|---|---|
| `sphinx_main_body_<hotend>` | The only part that changes between archives |
| `left_clamp_monolith` | Monolith carriage mount |
| `right_clamp_monolith` | Monolith carriage mount |
| `extruder_mount` | Sherpa Mini |
| `sherpa_bracket` | Sherpa Mini |
| `mid_support` | Common part |
| `rear_duct` | Common Part |

The clamps are what make these Monolith-specific. If you are on a Voron-style carriage, use the [Voron Versions](../Voron%20Versions) folder instead — those ship `left_clamp_voron` / `right_clamp_voron` in place of these.

---

## 🖨️ Print Settings

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

Any filled ABS or better is recommended. Individuals have printed Sphinx out of anything from ABS-GF to PEEK

---

See the [main README](../README.md) for supported hardware, cooling notes, and input shaper results.
