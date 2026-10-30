"""ViSinhVien: minh hoa CSDL RIENG, khong phai backend cua Web demo.
Chi dung database trong RAM va du lieu gia. Python 3, thu vien chuan.
"""
import sqlite3
import sys

# Console Windows co the dung bang ma cu (cp1252) va lam chuong trinh dung giua.
# Buoc stdout/stderr sang UTF-8 de in duoc ten khoan chi co dau.
for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

connection = sqlite3.connect(":memory:")
connection.execute("""
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL CHECK(length(trim(title)) BETWEEN 1 AND 80),
    amount INTEGER NOT NULL CHECK(typeof(amount) = 'integer' AND amount BETWEEN 1 AND 1000000000),
    category TEXT NOT NULL CHECK(category IN ('an-uong', 'di-lai', 'hoc-tap', 'khac'))
)
""")
rows = [(1, "Cơm trưa", 35000, "an-uong"), (2, "Xe buýt", 7000, "di-lai"), (3, "Vở ghi", 18000, "hoc-tap")]
connection.executemany("INSERT INTO expenses(id, title, amount, category) VALUES (?, ?, ?, ?)", rows)
total = connection.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses").fetchone()[0]
assert total == 60000
print("Tong du lieu mau:", total, "VND")
# Dấu nháy đơn thuộc dữ liệu. Placeholder giữ dữ liệu tách khỏi câu lệnh.
title = "Vở O'Reilly"
connection.execute("INSERT INTO expenses(id, title, amount, category) VALUES (?, ?, ?, ?)", (4, title, 12000, "hoc-tap"))
found = connection.execute("SELECT title, amount FROM expenses WHERE title = ?", (title,)).fetchall()
assert found == [(title, 12000)]
print("Tra cuu tham so:", found)
# So tien am va so thap phan deu phai bi constraint tu choi.
for bad in (-1, 0, 1.5, 1000000001):
    try:
        connection.execute("INSERT INTO expenses(id,title,amount,category) VALUES (?,?,?,?)", (5, "Du lieu khong hop le", bad, "khac"))
    except sqlite3.IntegrityError:
        print("PASS reject amount", bad)
    else:
        raise AssertionError("Da chap nhan amount khong hop le")
connection.execute("DELETE FROM expenses")  # Chỉ bảng dữ liệu giả trong RAM vừa tạo.
assert connection.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses").fetchone()[0] == 0
print("PASS empty total = 0")
connection.close()
print("PASS SQLite demo; khong tao file CSDL, khong goi dich vu ngoai")
