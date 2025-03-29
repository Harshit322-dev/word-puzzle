from cairosvg import svg2png

# Convert logo
svg2png(url='logo.svg', write_to='logo.png', output_width=200, output_height=200)

# Convert profile
svg2png(url='profile.svg', write_to='profile.png', output_width=200, output_height=200)

print("SVG फ़ाइलें सफलतापूर्वक PNG में कन्वर्ट हो गई हैं!") 