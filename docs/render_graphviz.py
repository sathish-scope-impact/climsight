#!/usr/bin/env python3
"""Render ClimSight data sources diagram as high-res PNG using Graphviz."""
import graphviz
import os

dot = graphviz.Digraph(
    "ClimSight",
    format="png",
    engine="dot",
    graph_attr={
        "rankdir": "LR",
        "fontname": "Helvetica",
        "fontsize": "14",
        "bgcolor": "white",
        "pad": "0.5",
        "nodesep": "0.20",
        "ranksep": "0.8",
        "dpi": "200",
        "compound": "true",
        "newrank": "true",
    },
    node_attr={
        "fontname": "Helvetica",
        "fontsize": "9",
        "shape": "box",
        "style": "rounded,filled",
        "margin": "0.10,0.05",
    },
    edge_attr={
        "fontname": "Helvetica",
        "fontsize": "7",
        "color": "#888888",
        "arrowsize": "0.5",
    },
)

# ═══════ COLUMN 1: DATA SOURCES (stacked vertically) ═══════

with dot.subgraph(name="cluster_col1") as col:
    col.attr(label="Data Sources", style="rounded,bold", color="#37474F",
             fontcolor="#263238", bgcolor="#FAFAFA", fontsize="13")

    with col.subgraph(name="cluster_apis") as c:
        c.attr(label="External APIs (Live)", style="dashed,rounded", color="#0288D1",
               fontcolor="#01579B", bgcolor="#E1F5FE", fontsize="10")
        c.node("NOM", "Nominatim\nGeocoding", fillcolor="#B3E5FC")
        c.node("ETOPO", "ETOPO1\nElevation", fillcolor="#B3E5FC")
        c.node("ISRIC", "SoilGrids\nSoil", fillcolor="#B3E5FC")
        c.node("OSM", "Overpass\nLand Use", fillcolor="#B3E5FC")
        c.node("GBIF", "GBIF\nBiodiversity", fillcolor="#B3E5FC")

    with col.subgraph(name="cluster_static") as c:
        c.attr(label="Static Files", style="dashed,rounded", color="#7B1FA2",
               fontcolor="#4A148C", bgcolor="#F3E5F5", fontsize="10")
        c.node("NE_GEO", "Natural Earth\nShapefiles", fillcolor="#E1BEE7")
        c.node("HAZ_CSV", "GDIS Disasters\n1960-2018", fillcolor="#CE93D8")
        c.node("POP_CSV", "UN WPP 2022\nPopulation", fillcolor="#CE93D8")
        c.node("ECOCROP", "EcoCrop DB\nCrop Suitability", fillcolor="#CE93D8")

    with col.subgraph(name="cluster_climate") as c:
        c.attr(label="Climate Models (NetCDF)", style="dashed,rounded", color="#EF6C00",
               fontcolor="#E65100", bgcolor="#FFF3E0", fontsize="10")
        c.node("NGEMS", "nextGEMS\nHEALPix\n2020-2049", fillcolor="#FFE0B2")
        c.node("ICCP", "ICCP\nRegular\n2020-2099", fillcolor="#FFE0B2")
        c.node("AWI", "AWI-CM\nCMIP6\nHist+SSP585", fillcolor="#FFE0B2")
        c.node("DESTNE", "DestinE\nUnstruct.\nSSP3-7.0", fillcolor="#FFE0B2")

    with col.subgraph(name="cluster_era5") as c:
        c.attr(label="ERA5 (Ground Truth)", style="dashed,rounded", color="#2E7D32",
               fontcolor="#1B5E20", bgcolor="#E8F5E9", fontsize="10")
        c.node("ERA5_CLIM", "ERA5 Climatology\nZarr 2015-2025", fillcolor="#C8E6C9")
        c.node("ERA5_RET", "ERA5 Retrieval\n1979-2024", fillcolor="#C8E6C9")

    with col.subgraph(name="cluster_rag") as c:
        c.attr(label="RAG Stores (Chroma)", style="dashed,rounded", color="#C62828",
               fontcolor="#B71C1C", bgcolor="#FCE4EC", fontsize="10")
        c.node("IPCC_RAG", "IPCC AR6\nRAG", fillcolor="#F8BBD0")
        c.node("GEN_RAG", "General Reports\nRAG", fillcolor="#F8BBD0")
        c.node("DEST_RAG", "DestinE Params\nRAG", fillcolor="#F8BBD0")
        c.node("DEST_POLY", "DestinE Polytope\nAPI", fillcolor="#F8BBD0")

# ═══════ COLUMN 2: USER + AGENTS ═══════

dot.node("UQ", "User Query\n(lat, lon, question)", fillcolor="#C8E6C9", color="#2E7D32",
         penwidth="2", fontsize="11")

with dot.subgraph(name="cluster_agents") as c:
    c.attr(label="LangGraph Agent Pipeline", style="bold,rounded", color="#F9A825",
           fontcolor="#F57F17", bgcolor="#FFFDE7", fontsize="12")

    c.node("INTRO", "intro_agent\nRelevance\nfilter", fillcolor="#FFF9C4", shape="diamond")

    c.node("ZERO_AG", "zero_rag_agent\nlocation, elevation, soil,\nland use, coast, hazards", fillcolor="#FFE082")
    c.node("DATA_AG", "data_agent\n12-month DataFrame\nTemp, Precip, Wind", fillcolor="#FFE082")
    c.node("IPCC_AG", "ipcc_rag_agent\nIPCC context", fillcolor="#FFE082")
    c.node("GEN_AG", "general_rag_agent\nLiterature context", fillcolor="#FFE082")
    c.node("SMART_AG", "smart_agent (opt.)\nWikipedia, ECOCROP", fillcolor="#FFE082", style="rounded,filled,dashed")

    c.node("STATE", "AgentState\n(Shared State Bus)",
           fillcolor="#E0E0E0", color="#616161", penwidth="2", shape="cylinder")

    c.node("PREPARE", "prepare_predefined_data\nERA5 + 3 plots", fillcolor="#FFF9C4")
    c.node("DA_AG", "data_analysis_agent\n(opt.) REPL + tools",
           fillcolor="#FFF9C4", style="rounded,filled,dashed")
    c.node("COMBINE", "combine_agent\nSynthesize → Report", fillcolor="#FFF9C4", fontsize="10")

# ═══════ COLUMN 3: OUTPUTS ═══════

with dot.subgraph(name="cluster_outputs") as c:
    c.attr(label="Outputs", style="dashed,rounded", color="#00695C",
           fontcolor="#004D40", bgcolor="#E0F2F1", fontsize="11")
    c.node("CLIM_PLOT", "Climate\nComparison", fillcolor="#B2DFDB")
    c.node("DIS_PLOT", "Disaster\nSummary", fillcolor="#B2DFDB")
    c.node("POP_PLOT", "Population\nProjection", fillcolor="#B2DFDB")
    c.node("CUSTOM_VIZ", "Custom\nViz", fillcolor="#B2DFDB", style="rounded,filled,dashed")
    c.node("REPORT", "Final Report\n800-1500 words\n7 sections", fillcolor="#80CBC4",
           color="#00695C", penwidth="2.5", fontsize="10")

# ═══════ RANK HINTS ═══════
# Force vertical ordering within agent pipeline
dot.edge("INTRO", "ZERO_AG", color="#2E7D32", weight="5")
dot.edge("INTRO", "DATA_AG", color="#2E7D32", weight="5")
dot.edge("INTRO", "IPCC_AG", color="#2E7D32", weight="5")
dot.edge("INTRO", "GEN_AG", color="#2E7D32", weight="5")
dot.edge("INTRO", "SMART_AG", color="#2E7D32", style="dashed", weight="5")

# ═══════ EDGES: Data Sources → Agents ═══════

# APIs/Static → zero_agent
for src in ["NOM", "ETOPO", "ISRIC", "OSM", "GBIF", "NE_GEO", "HAZ_CSV", "POP_CSV"]:
    dot.edge(src, "ZERO_AG")

# Climate → data_agent
for src in ["NGEMS", "ICCP", "AWI", "DESTNE"]:
    dot.edge(src, "DATA_AG")

# RAG → agents
dot.edge("IPCC_RAG", "IPCC_AG")
dot.edge("GEN_RAG", "GEN_AG")
dot.edge("ECOCROP", "SMART_AG")
dot.edge("GEN_RAG", "SMART_AG", style="dashed")

# ═══════ EDGES: Agent Pipeline ═══════

dot.edge("UQ", "INTRO", weight="10")
dot.edge("INTRO", "REPORT", label="FINISH", color="#C62828", style="dashed")

# Parallel → State
for ag in ["ZERO_AG", "DATA_AG", "IPCC_AG", "GEN_AG", "SMART_AG"]:
    dot.edge(ag, "STATE", weight="5")

dot.edge("STATE", "PREPARE", weight="10")
dot.edge("ERA5_CLIM", "PREPARE", label="baseline")

dot.edge("PREPARE", "CLIM_PLOT")
dot.edge("PREPARE", "DIS_PLOT")
dot.edge("PREPARE", "POP_PLOT")

dot.edge("PREPARE", "DA_AG", style="dashed", label="if enabled")
dot.edge("PREPARE", "COMBINE", weight="10")

dot.edge("ERA5_RET", "DA_AG")
dot.edge("DEST_POLY", "DA_AG")
dot.edge("DEST_RAG", "DA_AG")

dot.edge("DA_AG", "CUSTOM_VIZ")
dot.edge("DA_AG", "COMBINE", style="dashed")

for p in ["CLIM_PLOT", "DIS_PLOT", "POP_PLOT", "CUSTOM_VIZ"]:
    dot.edge(p, "COMBINE")
dot.edge("COMBINE", "REPORT", penwidth="2", color="#00695C", weight="10")

# Render
output_path = "docs/climsight_data_sources"
dot.render(output_path, cleanup=True)
size_kb = os.path.getsize(f"{output_path}.png") / 1024
print(f"PNG saved to {output_path}.png ({size_kb:.0f} KB)")
