import math

def calculate_display_metrics():
    width_px = int(input("Enter horizontal resolution (pixels): "))
    height_px = int(input("Enter vertical resolution (pixels): "))
    diagonal_in = float(input("Enter physical diagonal size (inches): "))

    total_pixels = width_px * height_px
    
    gcd = math.gcd(width_px, height_px)
    aspect_w = width_px // gcd
    aspect_h = height_px // gcd

    diagonal_px = math.sqrt(width_px**2 + height_px**2)
    dpi = diagonal_px / diagonal_in

    if dpi < 100:
        category = "Low Density (Standard Monitor)"
    elif dpi <= 200:
        category = "Medium Density (HD Display)"
    else:
        category = "High Density (Retina / Mobile)"

    print("\n--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count:  {total_pixels:,} pixels")
    print(f"Aspect Ratio:       {aspect_w}:{aspect_h}")
    print(f"Calculated DPI:     {dpi:.2f} DPI")
    print(f"Density Category:   {category}")

if __name__ == "__main__":
    calculate_display_metrics()