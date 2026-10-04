---
title: Physics and physical sciences research skills
description: Agent skills for astronomy, quantum computing, materials analysis and geospatial research.
---

# Physics and physical sciences research

Choose the skill that fits your data and computational model. Ask the agent to preserve units, coordinate systems, uncertainty and software versions in every analysis.

| Task | Skill | What to provide |
|---|---|---|
| Analyze astronomical data | [`astropy`](/skills/astropy) | Observation metadata, units and reference frame |
| Explore quantum circuits | [`qiskit`](/skills/qiskit) | Circuit, backend, shots and noise assumptions |
| Work with crystal structures | [`pymatgen`](/skills/pymatgen) | Structure file and calculation provenance |
| Analyze spatial data | [`geopandas`](/skills/geopandas) | Geometry, projection and measurement scale |

```bash
npx skills add KalarisLabs/research-agent-skills --skill astropy
```

Try: “Inspect these FITS files and outline a reproducible photometry workflow. Check units and coordinate frames before calculating results.” For manuscript preparation, see the [paper writing guide](/guides/write-a-research-paper).
