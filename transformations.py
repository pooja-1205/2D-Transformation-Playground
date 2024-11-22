import numpy as np
import matplotlib.pyplot as plt

# Define 2D shape (Square)
shape = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [0, 0]  # Close the shape
])

# Transformation functions
def translate(shape, tx, ty):
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    shape_h = np.hstack((shape, np.ones((shape.shape[0], 1))))
    return (T @ shape_h.T).T[:, :2]

def rotate(shape, angle):
    angle_rad = np.radians(angle)
    R = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                  [np.sin(angle_rad), np.cos(angle_rad), 0],
                  [0, 0, 1]])
    shape_h = np.hstack((shape, np.ones((shape.shape[0], 1))))
    return (R @ shape_h.T).T[:, :2]

def scale(shape, sx, sy):
    S = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])
    shape_h = np.hstack((shape, np.ones((shape.shape[0], 1))))
    return (S @ shape_h.T).T[:, :2]

def shear(shape, shx, shy):
    H = np.array([[1, shx, 0],
                  [shy, 1, 0],
                  [0, 0, 1]])
    shape_h = np.hstack((shape, np.ones((shape.shape[0], 1))))
    return (H @ shape_h.T).T[:, :2]

def affine_transform(shape, matrix):
    """Apply a custom affine transformation matrix"""
    shape_h = np.hstack((shape, np.ones((shape.shape[0], 1))))
    return (matrix @ shape_h.T).T[:, :2]

# Interactive simulation
def interactive_simulator():
    global shape
    while True:
        print("\nChoose a Transformation:")
        print("1. Translate")
        print("2. Rotate")
        print("3. Scale")
        print("4. Shear")
        print("5. Custom Affine")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            tx = float(input("Enter Tx (Translation in X): "))
            ty = float(input("Enter Ty (Translation in Y): "))
            shape = translate(shape, tx, ty)
        
        elif choice == '2':
            angle = float(input("Enter rotation angle (degrees): "))
            shape = rotate(shape, angle)
        
        elif choice == '3':
            sx = float(input("Enter scaling factor in X (Sx): "))
            sy = float(input("Enter scaling factor in Y (Sy): "))
            shape = scale(shape, sx, sy)
        
        elif choice == '4':
            shx = float(input("Enter shear factor in X: "))
            shy = float(input("Enter shear factor in Y: "))
            shape = shear(shape, shx, shy)
        
        elif choice == '5':
            print("\nEnter the 3x3 affine transformation matrix elements:")
            matrix = np.zeros((3, 3))
            for i in range(3):
                for j in range(3):
                    matrix[i,j] = float(input(f"Enter element [{i},{j}]: "))
            shape = affine_transform(shape, matrix)
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, try again!")
            continue
        
        # Plot the transformed shape
        plt.figure(figsize=(8, 8))
        plt.plot(shape[:, 0], shape[:, 1], 'b-', linewidth=2, label="Transformed Shape")
        plt.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], 'r--', label="Original Shape")
        plt.legend()
        plt.title("2D Transformation")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.axis('equal')  # Keep aspect ratio equal
        plt.show()

# Run the simulator
if __name__ == "__main__":
    interactive_simulator()