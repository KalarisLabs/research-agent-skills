---
title: "geopandas — AI agent skill for physical sciences"
description: "Guidance and local audit CLIs for Python workflows using GeoPandas 1.1.4 GeoSeries and GeoDataFrame for planar vector data: CRS handling, geometry validity…"
keywords: ["geospatial", "GIS", "vector data", "spatial analysis", "Python"]
---

# `geopandas`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** geospatial, GIS, vector data, spatial analysis, Python

## When to use it

Guidance and local audit CLIs for Python workflows using GeoPandas 1.1.4 GeoSeries and GeoDataFrame for planar vector data: CRS handling, geometry validity and repair, sjoin, overlay, clip, dissolve, union, GeoPackage, GeoParquet and PostGIS I/O, and plotting. Use when reprojecting or assigning a CRS, auditing invalid or empty geometries, running spatial joins and checking cardinality, exporting vector data with a reproducible contract, or migrating code from GeoPandas 0.14 to 1.x. Use when checking privacy risks in coordinate data. Do not use for raster data or geodesic-only calculations.

## Example requests

Ask your agent in plain language, for example:

- *"my shapefile has no .prj and I think it's in UTM somewhere, how do I get it into lat/lon for a web map?"*
- *"I'm running gpd.sjoin(parcels, flood_zones, how='left', predicate='within') on parcels.gpkg and flood_zones.gpkg in EPSG:4326. I get 2.3M rows from 1.8M parcels, and I'm also getting a warning about CRS mismatch. What's wrong, and how do I check it?"*
- *"I have GPS collar tracks for an endangered species and want to put the cleaned locations in a supplementary dataset for my paper. What should I check before I publish?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill geopandas

# Kalaris Labs installer with checksum verification
npx research-agent-skills install geopandas
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/geopandas/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
