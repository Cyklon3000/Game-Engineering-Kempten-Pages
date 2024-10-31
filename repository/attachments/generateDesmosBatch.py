# Define the function-integral pairs
function_integral_pairs = [
    ("x^2", "\\frac{x^{2+1}}{2+1}"),
    ("\\frac{1}{x}", "\\ln{x}"),
    ("e^x", "e^x"),
    ("\\ln x", "x \\ln x - x"),
    ("\\sin x", "-\\cos x"),
    ("\\cos x", "\\sin x"),
    ("\\tan x", "-\\ln (\\cos x)"),
    ("\\sinh x", "\\cosh x"),
    ("\\cosh x", "\\sinh x"),
    ("\\arcsin x", "x \\arcsin x + \\sqrt{1-x^2}"),
    ("\\arccos x", "x \\arccos x - \\sqrt{1-x^2}"),
    ("\\frac{1}{\\sqrt{1-x^2}}", "\\arcsin x"),
    ("-\\frac{1}{\\sqrt{1-x^2}}", "\\arccos x"),
    ("\\frac{1}{1+x^2}", "\\arctan x")
]

# Desmos header configuration (dimensions and axis settings)
desmos_header = """
```desmos-graph
height=150; width=150;
left=-5; right=5;
top=5; bottom=-5;
---
"""

# Generate Desmos equations from the pairs
desmos_content = desmos_header
for i, (f, F) in enumerate(function_integral_pairs):
    desmos_content = desmos_header
    color_code1 = f"#AA0000"  # Color coding for each pair (just for fun)
    color_code2 = f"#00AA00"  # Color coding for each pair (just for fun)
    desmos_content += f"y={f} | {color_code1}\n"
    desmos_content += f"y={F} | {color_code2}\n"
    desmos_content += "```"
    print(desmos_content)