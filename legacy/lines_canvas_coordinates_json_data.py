import json
import math
from math import pi, cos, sin
from PIL import Image, ImageDraw, ImageOps

def create_blank_canvas(data):
    # Extract canvas size and background color from the data
    canvas_size = tuple(data['canvas_size'])
    background_color = tuple(data['background_color'])

    # Create a blank image with the specified canvas size and background color
    canvas = Image.new('RGB', canvas_size, background_color)
    
    return canvas

# Function to create a canvas with grid lines
def create_canvas_with_lines(canvas, data):
    canvas_size = tuple(data['canvas_size'])
    line_interval = data['line_interval']
    line_color = data['line_color']

    draw = ImageDraw.Draw(canvas)

    num_units_x = canvas_size[0] // line_interval
    num_units_y = canvas_size[1] // line_interval

    for x in range(0, canvas_size[0], line_interval):
        draw.line([(x, 0), (x, canvas_size[1])], fill=line_color)

    for y in range(0, canvas_size[1], line_interval):
        draw.line([(0, y), (canvas_size[0], y)], fill=line_color)

    for x in range(num_units_x + 1):
        for y in range(num_units_y + 1):
            coords = (x * line_interval, y * line_interval)
            draw.text(coords, f"({x * line_interval},{y * line_interval})", fill="black")

    return canvas

def generate_gradient_color(color1, color2, width, height, direction="horizontal"):
    if direction == "horizontal":
        gradient = Image.new("RGB", (width, height))
        for x in range(width):
            r = int((color1[0] * (width - x) + color2[0] * x) / width)
            g = int((color1[1] * (width - x) + color2[1] * x) / width)
            b = int((color1[2] * (width - x) + color2[2] * x) / width)
            for y in range(height):
                gradient.putpixel((x, y), (r, g, b))
        return gradient
    elif direction == "vertical":
        gradient = Image.new("RGB", (width, height))
        for y in range(height):
            r = int((color1[0] * (height - y) + color2[0] * y) / height)
            g = int((color1[1] * (height - y) + color2[1] * y) / height)
            b = int((color1[2] * (height - y) + color2[2] * y) / height)
            for x in range(width):
                gradient.putpixel((x, y), (r, g, b))
        return gradient


def draw_shapes_on_canvas(canvas, data):
    for shape_data in data['shapes']:
        shape_type = shape_data['type']
        if shape_type == "straight_line":
            canvas = draw_straight_line(canvas, shape_data)
        elif shape_type == "dashed_line":
            canvas = draw_dashed_line(canvas, shape_data)
        elif shape_type == "zigzag_line":
            canvas = draw_zigzag_line(canvas, shape_data)
        elif shape_type == "wavy_line":
            canvas = draw_wavy_line(canvas, shape_data)
        elif shape_type == "line_with_arrowhead":
            canvas = draw_line_with_arrowhead(canvas, shape_data)
        elif shape_type == "line_with_double_arrowhead":
            canvas = draw_line_with_double_arrowhead(canvas, shape_data)
        elif shape_type == "elbow_connector":
            canvas = draw_elbow_connector(canvas, shape_data)
        elif shape_type == "elbow_connector_with_arrowhead":
            canvas = draw_elbow_connector_with_arrowhead(canvas, shape_data)
        elif shape_type == "elbow_connector_with_double_arrowhead":
            canvas = draw_elbow_connector_with_double_arrowhead(canvas, shape_data)
        elif shape_type == "speech_bubble_rectangle":
            canvas = draw_speech_bubble_rectangle(canvas, shape_data)
        elif shape_type == "polygon_with_coordinates":
            canvas = draw_polygon_with_coordinates(canvas, shape_data)
        elif shape_type == "regular_polygon":
            canvas = draw_regular_polygon(canvas, shape_data)
        elif shape_type == "square":
            canvas = draw_square(canvas, shape_data)
        elif shape_type == "rectangle":
            canvas = draw_rectangle(canvas, shape_data)
        elif shape_type == "circle":
            canvas = draw_circle(canvas, shape_data)
        elif shape_type == "ellipse":
            canvas = draw_ellipse(canvas, shape_data)
        elif shape_type == "heart":
            canvas = draw_heart_with_rotation_angle(canvas, shape_data)
        elif shape_type == "diamond":
            canvas = draw_diamond(canvas, shape_data)
        elif shape_type == "cloud":
            canvas = draw_cloud(canvas, shape_data)
        elif shape_type == "star":
            canvas = draw_star(canvas, shape_data)
        else:
            return "Shape not Found"
    return canvas


# Function to draw a straight line
def draw_straight_line(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    border_width = data['border_width']

    draw = ImageDraw.Draw(canvas)
    draw.line([start, end], fill=fill_color, width=border_width)

    return canvas

# Function to draw a dashed line
def draw_dashed_line(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    border_width = data['border_width']
    dash_length = data.get('dash_length', 10)

    draw = ImageDraw.Draw(canvas)
    is_drawing_dash = True
    current_position = start

    while current_position[0] < end[0]:
        next_x = min(current_position[0] + dash_length, end[0])
        next_position = (next_x, current_position[1])

        if is_drawing_dash:
            draw.line([current_position, next_position], fill=fill_color, width=border_width)

        current_position = next_position
        is_drawing_dash = not is_drawing_dash

    return canvas

# Function to draw a zigzag line
def draw_zigzag_line(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    border_width = data['border_width']
    amplitude = data.get('amplitude', 20)
    frequency = data.get('frequency', 40)

    draw = ImageDraw.Draw(canvas)
    current_position = start

    while current_position[0] < end[0]:
        next_x = min(current_position[0] + frequency, end[0])
        next_y = current_position[1] + amplitude
        draw.line([current_position, (next_x, next_y)], fill=fill_color, width=border_width)
        current_position = (next_x, next_y)
        amplitude = -amplitude

    return canvas

# Function to draw a wavy line
def draw_wavy_line(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    border_width = data['border_width']
    amplitude = data.get('amplitude', 20)
    frequency = data.get('frequency', 40)
    num_points = data.get('num_points', 100)

    draw = ImageDraw.Draw(canvas)
    points = []
    x, y = start

    for _ in range(num_points):
        points.append((x, y))
        x += frequency
        y += amplitude * (1 if len(points) % 2 == 0 else -1)

        if x > end[0]:
            break

    for i in range(1, len(points)):
        draw.line([points[i - 1], points[i]], fill=fill_color, width=border_width)

    return canvas

# Function to draw a line with an arrowhead at the end
def draw_line_with_arrowhead(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']

    draw = ImageDraw.Draw(canvas)
    draw.line([start, end], fill=fill_color, width=border_width)
    arrow = (end[0] - 10, end[1])
    draw.polygon([end, (arrow[0], arrow[1] - 5), (arrow[0], arrow[1] + 5)], fill=fill_color, outline=outline_color, width=border_width)

    return canvas

# Function to draw a line with double arrowheads at both ends
def draw_line_with_double_arrowhead(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']

    draw = ImageDraw.Draw(canvas)
    draw.line([start, end], fill=fill_color, width=border_width)
    arrow1 = (start[0] + 10, start[1])
    arrow2 = (end[0] - 10, end[1])
    draw.polygon([start, (arrow1[0], arrow1[1] - 5), (arrow1[0], arrow1[1] + 5)], fill=fill_color, outline=outline_color, width=border_width)
    draw.polygon([end, (arrow2[0], arrow2[1] - 5), (arrow2[0], arrow2[1] + 5)], fill=fill_color, outline=outline_color, width=border_width)

    return canvas

# Function to draw an elbow connector
def draw_elbow_connector(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    border_width = data['border_width']
    elbow_length = data.get('elbow_length', 50)

    draw = ImageDraw.Draw(canvas)
    x1, y1 = start
    x2, y2 = end
    draw.line([start, (x1 + elbow_length, y1)], fill=fill_color, width=border_width)
    draw.line([(x1 + elbow_length, y1), (x1 + elbow_length, y1 + elbow_length * 2)], fill=fill_color, width=border_width)
    draw.line([(x1 + elbow_length, y1 + elbow_length * 2), (x2, y2 + elbow_length * 2)], fill=fill_color, width=border_width)

    return canvas

# Function to draw an elbow connector with an arrowhead
def draw_elbow_connector_with_arrowhead(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    elbow_length = data.get('elbow_length', 50)

    draw = ImageDraw.Draw(canvas)
    x1, y1 = start
    x2, y2 = end
    draw.line([start, (x1 + elbow_length, y1)], fill=fill_color, width=border_width)
    draw.line([(x1 + elbow_length, y1), (x1 + elbow_length, y1 + elbow_length * 2)], fill=fill_color, width=border_width)
    draw.line([(x1 + elbow_length, y1 + elbow_length * 2), (x2, y2 + elbow_length * 2)], fill=fill_color, width=border_width)
    arrow = (x2 - 10, y2 + elbow_length * 2)
    draw.polygon([(x2, y2 + elbow_length * 2), (arrow[0], arrow[1] - 5), (arrow[0], arrow[1] + 5)], fill=fill_color, outline=outline_color, width=border_width)

    return canvas

# Function to draw an elbow connector with double arrowheads
def draw_elbow_connector_with_double_arrowhead(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    elbow_length = data.get('elbow_length', 50)

    draw = ImageDraw.Draw(canvas)
    x1, y1 = start
    x2, y2 = end
    draw.line([start, (x1 + elbow_length, y1)], fill=fill_color, width=border_width)
    draw.line([(x1 + elbow_length, y1), (x1 + elbow_length, y1 + elbow_length * 2)], fill=fill_color, width=border_width)
    draw.line([(x1 + elbow_length, y1 + elbow_length * 2), (x2, y2 + elbow_length * 2)], fill=fill_color, width=border_width)
    arrow1 = (x1 + 10, y1)
    arrow2 = (x2 - 10, y2 + elbow_length * 2)
    draw.polygon([start, (arrow1[0], arrow1[1] - 5), (arrow1[0], arrow1[1] + 5)], fill=fill_color, outline=outline_color, width=border_width)
    draw.polygon([(x2, y2 + elbow_length * 2), (arrow2[0], arrow2[1] - 5), (arrow2[0], arrow2[1] + 5)], fill=fill_color, outline=outline_color, width=border_width)

    return canvas

# Function to draw speech bubble rectangle
def draw_speech_bubble_rectangle(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']

    draw = ImageDraw.Draw(canvas)
    x1, y1 = start
    x2, y2 = end
    rect_width = x2 - x1
    rect_height = y2 - y1

    points = [
        (x1, y1), (x2, y1), (x2, y2), (x1 + (x2 - x1) // 4, y2),
        (((x1 + rect_width // 8) + (x1 + rect_width // 4)) // 2, y2 + 20),
        (x1 + (x2 - x1) // 8, y2), (x1, y2), (x1, y1)
    ]
    draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)

    return canvas

# Function to draw Polygon based on number of points or coordinates
def draw_polygon_with_coordinates(canvas, data):
    coordinates = [tuple(coord) for coord in data['coordinates']]
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']

    draw = ImageDraw.Draw(canvas)
    draw.polygon(coordinates, fill=fill_color, outline=outline_color, width=border_width)
    
    return canvas

# Function to draw regular polygon based on number of sides
def draw_regular_polygon(canvas, data):
    center = tuple(data['center'])
    n_sides = data['n_sides']
    rotation = data.get('rotation', 0)  # Default rotation is 0 degrees
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']  # Default line width is 1 pixel
    # Define the bounding circle
    bounding_circle = (center, data['radius'])
    
    draw = ImageDraw.Draw(canvas)

    # Draw the regular polygon
    draw.regular_polygon(bounding_circle, n_sides, rotation, fill=fill_color, outline=outline_color)

    # Draw the outline (border) of the polygon with the specified width
    for i in range(n_sides):
        start = (
            center[0] + data['radius'] * math.cos(2 * math.pi * i / n_sides + math.radians(rotation)),
            center[1] + data['radius'] * math.sin(2 * math.pi * i / n_sides + math.radians(rotation))
        )
        end = (
            center[0] + data['radius'] * math.cos(2 * math.pi * (i + 1) / n_sides + math.radians(rotation)),
            center[1] + data['radius'] * math.sin(2 * math.pi * (i + 1) / n_sides + math.radians(rotation))
        )
        draw.line([start, end], fill=outline_color, width=border_width)
        
    return canvas

# Function to draw a square
def draw_square(canvas, data):
    start = tuple(data['start'])
    size = data['size']
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    draw = ImageDraw.Draw(canvas)
    end = (start[0] + size, start[1] + size)
    draw.rectangle([start, end], fill=fill_color, outline=outline_color, width=border_width)
    return canvas

# Function to draw a rectangle
def draw_rectangle(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([start, end], fill=fill_color, outline=outline_color, width=border_width)
    return canvas

# Function to draw a circle
def draw_circle(canvas, data):
    center = tuple(data['center'])
    radius = data['radius']
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    draw = ImageDraw.Draw(canvas)
    draw.ellipse([(center[0] - radius, center[1] - radius), (center[0] + radius, center[1] + radius)], fill=fill_color, outline=outline_color, width=border_width)
    return canvas

# Function to draw an ellipse
def draw_ellipse(canvas, data):
    start = tuple(data['start'])
    end = tuple(data['end'])
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    draw = ImageDraw.Draw(canvas)
    draw.ellipse([start, end], fill=fill_color, outline=outline_color, width=border_width)
    return canvas

# Function to draw heart
def draw_heart_with_rotation_angle(canvas, data):
    center = tuple(data['center'])
    size = data['size']
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    rotation_angle = data['rotation_angle']  # Angle in degrees
    draw = ImageDraw.Draw(canvas)

    def rotate_point(point, angle_degrees, center):
        angle_rad = math.radians(angle_degrees)
        x, y = point
        cx, cy = center
        new_x = (x - cx) * math.cos(angle_rad) - (y - cy) * math.sin(angle_rad) + cx
        new_y = (x - cx) * math.sin(angle_rad) + (y - cy) * math.cos(angle_rad) + cy
        return (new_x, new_y)

    def heart_equation(t):
        x = size * (16 * math.sin(t)**3)
        y = size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        return rotate_point((x + center[0], y + center[1]), rotation_angle, center)

    num_points = data.get('num_points', 100)
    points = [heart_equation(2 * math.pi * t / num_points) for t in range(num_points)]

    # for i in range(1, len(points)):
    #     draw.line([points[i - 1], points[i]], fill=fill_color, width=border_width)
        
    # Draw a filled polygon to represent the heart shape
    draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        
    return canvas

# Function to draw daimond
def draw_diamond(canvas, data):
    center = tuple(data['center'])
    size = data['size']
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    draw = ImageDraw.Draw(canvas)
    points = [
        (center[0], center[1] - size),
        (center[0] + size, center[1]),
        (center[0], center[1] + size),
        (center[0] - size, center[1])
    ]
    points.append(points[0])  # Close the diamond
    draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
    return canvas

# Function to draw cloud
def draw_cloud(canvas, data):
    center = tuple(data['center'])
    size = data['size']
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    num_circles = data['num_circles']

    draw = ImageDraw.Draw(canvas)
    x, y = center
    temp_x, temp_y = center

    for i in range(2):
        for j in range(num_circles):
            ellipse_bbox = (x - size, y - size, x + size, y + size)
            draw.ellipse(ellipse_bbox, fill=fill_color, outline=outline_color, width=border_width)
            size += int(size * 0.05)  
            x += int(size * 1.4) 
        x = temp_x - int(size * 0.5)
        y = temp_y + int(size * 1.5) 
    return canvas


# Function to draw star based on number of points
def draw_star(canvas, data):
    center = tuple(data['center'])
    size = data['size']
    fill_color = tuple(data['fill_color'])
    outline_color = tuple(data['outline_color'])
    border_width = data['border_width']
    num_points = data['num_points']

    draw = ImageDraw.Draw(canvas)
    x, y = center

    points = []
    for i in range(num_points * 2):
        angle = 2 * pi * i / (num_points * 2)
        if i % 2 == 0:
            radius = size
        else:
            radius = size * 0.4  # Adjust this value for the inner vertices
        points.extend([x + radius * cos(angle), y + radius * sin(angle)])

    draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)

    return canvas


# Load data from the JSON file
with open('Decorative_Elements/lines_canvas_coordinates_json_data_input_json.json', 'r') as json_file:
    data = json.load(json_file)

# Create a blank canvas using the data
canvas = create_blank_canvas(data)

# Create canvas with grid lines
canvas = create_canvas_with_lines(canvas, data)

# Draw the shapes on the canvas
canvas = draw_shapes_on_canvas(canvas, data)

# Save or manipulate the canvas as needed
# For example, you can save the canvas:
canvas.save('canvas_image.png')
canvas.show()