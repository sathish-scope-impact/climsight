#!/usr/bin/env python3
"""Render the ClimSight data sources Mermaid diagram to PNG using Playwright."""
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

SCRIPT_DIR = Path(__file__).parent
MMD_FILE = SCRIPT_DIR / "climsight_data_sources.mmd"
PNG_FILE = SCRIPT_DIR / "climsight_data_sources.png"

HTML_TEMPLATE = """<!DOCTYPE html>
<html><head>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<style>
  body {{ margin: 0; padding: 20px; background: white; }}
  #diagram {{ width: max-content; }}
</style>
</head><body>
<div id="diagram">
<pre class="mermaid">
{mermaid_code}
</pre>
</div>
<script>
  mermaid.initialize({{
    startOnLoad: true,
    theme: 'default',
    flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'basis' }},
    securityLevel: 'loose'
  }});
</script>
</body></html>"""


async def render():
    mmd_text = MMD_FILE.read_text()
    html = HTML_TEMPLATE.format(mermaid_code=mmd_text)
    html_file = SCRIPT_DIR / "_temp_mermaid.html"
    html_file.write_text(html)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/root/.cache/ms-playwright/chromium_headless_shell-1194/chrome-linux/headless_shell",
        )
        page = await browser.new_page(viewport={"width": 3200, "height": 2400})
        await page.goto(f"file://{html_file.resolve()}")
        # Wait for mermaid to render
        await page.wait_for_selector("svg.mermaid", timeout=30000)
        await page.wait_for_timeout(2000)  # extra time for rendering
        # Get the bounding box of the rendered SVG
        svg = await page.query_selector("svg.mermaid")
        box = await svg.bounding_box()
        # Add padding
        pad = 40
        await page.screenshot(
            path=str(PNG_FILE),
            clip={
                "x": max(0, box["x"] - pad),
                "y": max(0, box["y"] - pad),
                "width": box["width"] + 2 * pad,
                "height": box["height"] + 2 * pad,
            },
        )
        await browser.close()

    html_file.unlink()
    print(f"PNG saved to {PNG_FILE} ({PNG_FILE.stat().st_size / 1024:.0f} KB)")


asyncio.run(render())
