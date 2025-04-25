class Area:
    def __init__(self):
        pass

    def triangle_area(self, height, base):
        return 0.5 * height * base

    def area_circle(self, radius):
        return 3.14 * radius ** 2

    def parallelepiped(self, length, width, height):
        return 2 * (length * width + length * height + width * height)

area_obj = Area()

# 삼각형 넓이 계산
triangle_area = area_obj.triangle_area(10, 5)
print(f"삼각형 넓이: {triangle_area}")

# 원의 넓이 계산
circle_area = area_obj.area_circle(5)
print(f"원의 넓이: {circle_area}")

# 직육면체 표면적 계산
parallelepiped_area = area_obj.parallelepiped(3, 3, 3)
print(f"직육면체 넓이: {parallelepiped_area}")
