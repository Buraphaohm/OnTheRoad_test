def lucky(n):
    count = 0

    start_range = int('0' * n)  # สร้างตัวเลขที่ใช้เริ่มต้นเป็น 0 ตามจำนวน n
    end_range = int(10 ** n)

    for num in range(start_range, end_range): 
        str_num = str(num)
        if len(str_num) < n:  # เชคว่าตัวเลขนี้มีหลักน้อยกว่าที่กำหนดหรือไม่
            str_num = str_num.zfill(n)  # ถ้าใช่ให้เติม 0 ข้างหน้า
        half = n // 2  # ใช้ // เพื่อหารได้ผลลัพธ์เป็นจำนวนเต็ม
        sum_first_half = sum(int(digit) for digit in str_num[:half])
        sum_second_half = sum(int(digit) for digit in str_num[half:])

        if sum_first_half == sum_second_half:
            count += 1

    return count

n = int(input("Enter an even number less than 9: "))
if n % 2 == 0 and n <= 9:  # ตรวจสอบว่า n เป็นเลขคู่และมีค่าไม่เกิน 9
    result = lucky(n)
    print(f"The count of {n}-digit 'lucky' numbers is: {result}")
else:
    print(f"Invalid input for n: {n}")
