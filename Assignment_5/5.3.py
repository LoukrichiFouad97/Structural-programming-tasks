import math

def distance_from_origin(x, y):
    return math.sqrt(x**2 + y**2)

def main():
    # Get the number of points
    num_points = int(input("Enter the number of points: "))

    # Initialize a two-dimensional array to store coordinates
    points = []
    
    # Input coordinates for each point
    for i in range(num_points):
        x = float(input(f"Enter x-coordinate for point {i + 1}: "))
        y = float(input(f"Enter y-coordinate for point {i + 1}: "))
        points.append([x, y])

    # Compute distance for each point
    distances = [distance_from_origin(x, y) for x, y in points]

    # Find the index of the farthest point
    farthest_index = distances.index(max(distances))

    # Display the coordinates in tabular format
    print("\nCoordinates Table:")
    print("Point   X-Coordinate   Y-Coordinate")
    for i in range(num_points):
        print(f"{i + 1:<7}{points[i][0]:<15}{points[i][1]:<15}")

    # Display the farthest point
    print(f"\nThe farthest point is Point {farthest_index + 1} with a distance of {max(distances):.2f} from the origin.")

if __name__ == "__main__":
    main()
