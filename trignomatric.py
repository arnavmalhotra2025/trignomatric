import math

def main():
    print("Trigonometric Calculator")
    print("------------------------")
    
    angle_deg = float(input("Enter angle in degrees: "))
    
    angle_rad = math.radians(angle_deg)

    sin_val = math.sin(angle_rad)
    cos_val = math.cos(angle_rad)
    try:
        tan_val = math.tan(angle_rad)
    except:
        tan_val = "Undefined"

    print(f"\nResults for angle {angle_deg}°:")
    print(f"Sin({angle_deg}) = {sin_val:.6f}")
    print(f"Cos({angle_deg}) = {cos_val:.6f}")

    if abs(cos_val) < 1e-10:
        print(f"Tan({angle_deg}) = Undefined (division by zero)")
    else:
        print(f"Tan({angle_deg}) = {tan_val:.6f}")

if __name__ == "__main__":
    main()