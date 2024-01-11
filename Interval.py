def Intersection_count(N, intervals):
    # สร้างlistไว้เก็บ
    endpoints = []
    
    # แต่ละinterval เพิ่มจุดเริ่มและท้าย
    for interval in intervals:
        endpoints.append((interval[0], 1)) # จุดเริ่ม
        endpoints.append((interval[1], -1)) # จุดท้าย
    
    # เรียงลำดับ
    endpoints.sort()
    
    # นับจำนวนที่intersectและinterval
    intersections = 0
    open_intervals = 0
    
    # loop
    for endpoint, value in endpoints:
        open_intervals += value
        
        # ถ้าซ้ำให้นับ
        if open_intervals > 1:
            intersections += 1
    
    return intersections

N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

result = Intersection_count(N, intervals)

print(result)