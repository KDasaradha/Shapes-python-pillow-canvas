# 🚀 How to Run ShapeCanvas - Quick Reference

**⚡ Super Quick Start - 2 Minutes**

## 📦 **Step 1: Install** *(30 seconds)*

```bash
cd "c:/Users/K_Dasaradh/Desktop/tardigrade/kdsr_repos/Shapes-python-pillow-canvas"
pip install -e .
```

## ⚡ **Step 2: Run** *(30 seconds)*

### **Option A: Use Your Original File**
```bash
shape-canvas lines_canvas_coordinates_json_data_input_json.json -o output.png --show
```

### **Option B: Try Our Example**
```bash
shape-canvas examples/basic_shapes.json -o test.png --show
```

### **Option C: Python Script**
```python
from shape_canvas import Canvas
Canvas.from_file("examples/basic_shapes.json").render().save("output.png").show()
```

## 🎉 **Done!**

Your image should appear and be saved as `output.png`.

---

**🔥 Need more help?** → **[Complete Tutorial (QUICKSTART.md)](QUICKSTART.md)**

**📚 Full Documentation** → **[README.md](README.md)**