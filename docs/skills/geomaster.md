---
title: "geomaster — AI agent skill for physical sciences"
description: "Provides geospatial and Earth observation workflows using GeoPandas, Rasterio, GDAL, Xarray, Shapely, Laspy, PDAL, Google Earth Engine, and STAC/Planetary…"
keywords: ["geospatial", "remote sensing", "Earth observation", "satellite imagery", "GIS"]
---

# `geomaster`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** MIT · **Version:** 1.3

**Tags:** geospatial, remote sensing, Earth observation, satellite imagery, GIS

## When to use it

Provides geospatial and Earth observation workflows using GeoPandas, Rasterio, GDAL, Xarray, Shapely, Laspy, PDAL, Google Earth Engine, and STAC/Planetary Computer, covering Sentinel, Landsat, MODIS, SAR and hyperspectral imagery, spectral indices, terrain and network analysis, point clouds, COGs, CRS handling, and spatial ML, with code in Python, R, Julia, JavaScript, C++, Java, Go, and Rust. Use when computing NDVI or other indices from satellite imagery, when running vector overlays, reprojection, or spatial statistics on shapefiles, GeoJSON, or GeoPackage data, when searching STAC catalogs and reading cloud-optimized GeoTIFFs, when classifying land cover or training ML models on Earth observation data, or when doing terrain, hydrology, or point cloud analysis. Not for general non-spatial data analysis or tabular ML.

## Example requests

Ask your agent in plain language, for example:

- *"How do I compute NDVI from a Sentinel-2 scene?"*
- *"I have parcels.shp in EPSG:3857 and flood_zones.geojson in EPSG:4326. I need the area of each parcel in hectares that overlaps a flood zone, but my overlay gives a 'CRS mismatch' warning and some areas look way too large. What should I do?"*
- *"I want to map how much forest cover my study watershed lost between 2015 and 2023 using free satellite data, and I'd like to train a classifier to do it. Where do I start?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill geomaster

# Kalaris Labs installer with checksum verification
npx research-agent-skills install geomaster
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/geomaster/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
