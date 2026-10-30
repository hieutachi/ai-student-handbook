"""Generate the handbook's 16 original editorial SVGs, using only the stdlib.

Run explicitly during Phase 4: python scripts/make_visuals.py
Importing this module does not create directories, SVGs, or a manifest.
assets/manifest.json is a list of gallery entries; paths are handbook-root-relative.
The structural checks below are not a substitute for rendered visual review.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence
import json
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
NS = "http://www.w3.org/2000/svg"
PAPER = "#f6f3ea"
INK = "#20342d"
MUTED = "#58685f"
GREEN = "#35634b"
PALE = "#dce8d0"
RUST = "#b95132"
YELLOW = "#f2dfa5"
RULE = "#d4dbcf"
SKIN = "#d5a17c"
HAIR = "#242823"
SERIF = "Georgia, 'Times New Roman', serif"
SANS = "system-ui, 'Segoe UI', sans-serif"
MONO = "ui-monospace, Consolas, monospace"
ET.register_namespace("", NS)


def element(parent: ET.Element, tag: str, **attrs: object) -> ET.Element:
    """Build escaped XML, never interpolate user-visible text into markup."""
    return ET.SubElement(
        parent, f"{{{NS}}}{tag}",
        {key.rstrip("_").replace("_", "-"): str(value)
         for key, value in attrs.items() if value is not None},
    )


def group(parent: ET.Element, x: float = 0, y: float = 0) -> ET.Element:
    return element(parent, "g", transform=f"translate({x} {y})")


def rect(parent, x, y, width, height, fill=PAPER, stroke=None, radius=0):
    return element(parent, "rect", x=x, y=y, width=width, height=height,
                   rx=radius, fill=fill, stroke=stroke, stroke_width=2 if stroke else None)


def line(parent, x1, y1, x2, y2, color=INK, width=2, dash=None):
    return element(parent, "line", x1=x1, y1=y1, x2=x2, y2=y2,
                   stroke=color, stroke_width=width, stroke_dasharray=dash,
                   stroke_linecap="round")


def path(parent, data, fill="none", stroke=INK, width=3, dash=None, marker=None):
    return element(parent, "path", d=data, fill=fill, stroke=stroke,
                   stroke_width=width, stroke_linecap="round", stroke_linejoin="round",
                   stroke_dasharray=dash, marker_end=f"url(#{marker})" if marker else None)


def circle(parent, x, y, radius, fill=PAPER, stroke=None, width=2):
    return element(parent, "circle", cx=x, cy=y, r=radius, fill=fill,
                   stroke=stroke, stroke_width=width if stroke else None)


def ellipse(parent, x, y, rx, ry, fill, stroke=None):
    return element(parent, "ellipse", cx=x, cy=y, rx=rx, ry=ry,
                   fill=fill, stroke=stroke, stroke_width=3 if stroke else None)


def text(parent, x, y, content, size=22, fill=INK, font=SANS,
         weight="400", anchor="start", leading=None):
    """Only explicit line breaks; never shrink text to fit a shape."""
    if size < 18:
        raise ValueError("Illustration text must be at least 18px")
    # Rust is an accent, not sufficiently dark small type on soft yellow.
    # Keep warning words in ink below large-text size; their marks stay rust.
    if fill == RUST and size < 24:
        fill = INK
    rows = content.split("\n") if isinstance(content, str) else list(content)
    node = element(parent, "text", x=x, y=y, fill=fill, font_family=font,
                   font_size=size, font_weight=weight, text_anchor=anchor)
    for index, row in enumerate(rows):
        element(node, "tspan", x=x, dy=0 if index == 0 else (leading or size * 1.4)).text = row
    return node


def meta(parent, x, y, content, fill=MUTED, anchor="start"):
    return text(parent, x, y, content, 18, fill, MONO, anchor=anchor)


def check(parent, x, y, color=GREEN, size=16):
    path(parent, f"M{x-size*.5} {y} l{size*.4} {size*.4} l{size*.75} {-size*.9}",
         stroke=color, width=3)


def cross(parent, x, y, color=RUST, size=9):
    line(parent, x-size, y-size, x+size, y+size, color, 3)
    line(parent, x-size, y+size, x+size, y-size, color, 3)


def sheet(parent, x, y, width, height, fill=PAPER, stroke=INK):
    """An evidence document, with a folded corner rather than a UI card."""
    g = group(parent, x, y)
    path(g, f"M0 0 H{width-24} L{width} 24 V{height} H0 Z", fill, stroke, 2)
    path(g, f"M{width-24} 0 V24 H{width}", stroke=stroke, width=2)
    return g


def receipt(parent, x, y, name, amount, index, width=160, height=170, omitted=False):
    g = group(parent, x, y)
    teeth = " ".join(f"L{width*(1-step/20):g} {height-(7 if step % 2 else 0)}"
                     for step in range(21))
    path(g, f"M0 0 H{width} V{height} {teeth} L0 0 Z",
         YELLOW if omitted else PAPER, RUST if omitted else INK, 2,
         "6 5" if omitted else None)
    meta(g, 16, 29, f"PHIẾU {index}")
    line(g, 16, 43, width-16, 43, RULE)
    text(g, 16, 76, name, 20)
    text(g, 16, 116, str(amount), 28, RUST if omitted else INK, MONO)
    meta(g, 16, 146, "BỊ BỎ" if omitted else "VND", RUST if omitted else MUTED)
    return g


CHARACTERS = {
    "Minh": {"shirt": GREEN, "notebook": YELLOW, "label": "Minh / C++"},
    "Lan": {"shirt": RUST, "notebook": PALE, "label": "Lan / Web"},
}


def portrait(parent, name, x=0, y=0):
    """Fixed adult facial proportions, hair silhouette and palette across scenes."""
    g = group(parent, x, y)
    if name == "Lan":
        path(g, "M-32 39 Q-35 5 0 5 Q35 6 34 42 L40 101 Q4 116 -41 101 Z",
             HAIR, HAIR)
    rect(g, -11, 77, 22, 31, SKIN, radius=8)
    ellipse(g, -29, 56, 6, 10, SKIN)
    ellipse(g, 29, 56, 6, 10, SKIN)
    path(g, "M-29 39 Q-29 16 0 16 Q29 16 29 39 L26 67 Q20 89 0 90 Q-20 87 -26 67 Z",
         SKIN, INK, 3)
    if name == "Minh":
        path(g, "M-30 49 L-33 26 L-22 16 L-25 9 L-8 13 L1 3 L10 12 L25 10 "
             "L30 27 L29 46 L19 29 Q-1 40 -23 32 Z", HAIR, HAIR)
    else:
        path(g, "M-30 51 Q-38 13 -4 10 Q31 8 32 48 L24 55 L20 28 "
             "Q3 38 -20 33 L-24 58 Z", HAIR, HAIR)
    path(g, "M-17 48 l9 -2 M8 46 l9 2", stroke=INK, width=2)
    circle(g, -11, 55, 2.2, INK)
    circle(g, 11, 55, 2.2, INK)
    path(g, "M1 55 l-3 10 h5 M-8 75 Q0 80 9 73", stroke=INK, width=2)
    return g


def body(parent, name, x, y, pose="listen", label=True):
    """Reusable full figure, with task-specific arms, notebook and pencil."""
    data = CHARACTERS[name]
    g = group(parent, x, y)
    ellipse(g, 0, 289, 57, 8, RULE)
    path(g, "M-34 201 L-35 274 L-11 274 L0 218 L12 274 L36 274 L31 201 Z", INK, INK)
    path(g, "M-35 267 L-11 267 L-8 282 L-45 282 Q-45 273 -35 267 Z", HAIR, HAIR)
    path(g, "M12 267 L35 267 Q47 273 46 282 H10 Z", HAIR, HAIR)
    path(g, "M-13 101 Q-35 99 -48 123 L-35 205 Q0 218 35 205 L48 123 "
         "Q33 101 13 101 Z", data["shirt"], INK)
    path(g, "M-14 103 Q0 118 14 103", stroke=PAPER, width=2)
    # Dark seams preserve shirt recognition without decorative branding.
    path(g, "M-28 151 L-26 195 M28 151 L26 195", stroke=INK, width=2)
    arms = {
        "compare": (("M-43 122 Q-70 145 -67 181", (-67, 181)),
                    ("M43 123 Q65 152 91 123", (91, 123))),
        "point": (("M-43 123 Q-63 146 -48 183", (-48, 183)),
                  ("M43 124 Q68 141 105 164", (105, 164))),
        "explain": (("M-43 124 Q-69 134 -99 104", (-99, 104)),
                    ("M43 124 Q61 151 48 186", (48, 186))),
        "write": (("M-43 124 Q-68 145 -38 167", (-38, 167)),
                  ("M43 124 Q58 154 3 162", (3, 162))),
        "audit": (("M-43 124 Q-71 149 -90 175", (-90, 175)),
                  ("M43 124 Q61 143 20 165", (20, 165))),
        "listen": (("M-43 123 Q-62 148 -43 190", (-43, 190)),
                   ("M43 123 Q62 148 45 188", (45, 188))),
    }
    if pose not in arms:
        raise ValueError(f"Unknown character pose: {pose}")
    for arm, endpoint in arms[pose]:
        path(g, arm, stroke=INK, width=22)
        path(g, arm, stroke=data["shirt"], width=16)
        circle(g, *endpoint, 9, SKIN, INK, 2)
    if pose in {"write", "audit", "listen"}:
        notebook = sheet(g, -30, 153, 62, 47, data["notebook"])
        line(notebook, 11, 16, 38, 16, GREEN, 2)
        line(notebook, 11, 27, 46, 27, GREEN, 2)
    if pose in {"write", "audit"}:
        line(g, 7, 160, 33, 139, INK, 4)
        line(g, 11, 157, 32, 140, YELLOW, 2)
    portrait(g, name)
    if label:
        text(g, 0, 327, data["label"], 18, INK, MONO, anchor="middle")
    return g


class Drawing:
    def __init__(self, slug: str, title: str, description: str, height: int = 720):
        self.slug = slug
        self.height = height
        self.root = ET.Element(f"{{{NS}}}svg", {
            "viewBox": f"0 0 1200 {height}", "width": "1200", "height": str(height),
            "role": "img", "aria-labelledby": f"{slug}-title {slug}-desc",
            "{http://www.w3.org/XML/1998/namespace}lang": "vi",
        })
        element(self.root, "title", id=f"{slug}-title").text = title
        element(self.root, "desc", id=f"{slug}-desc").text = description
        defs = element(self.root, "defs")
        for name, color in (("ink", INK), ("rust", RUST), ("green", GREEN)):
            marker = element(defs, "marker", id=f"{slug}-{name}",
                             viewBox="0 0 12 12", refX=10, refY=6,
                             markerWidth=10, markerHeight=10,
                             markerUnits="userSpaceOnUse", orient="auto")
            path(marker, "M1 1 L11 6 L1 11 Z", color, "none", 0)
        rect(self.root, 0, 0, 1200, height, PAPER)

    def arrow(self, data, color="ink", dash=None, width=2.5):
        return path(self.root, data, stroke={"ink": INK, "rust": RUST, "green": GREEN}[color],
                    width=width, dash=dash, marker=f"{self.slug}-{color}")

    def heading(self, section, title, subtitle, number=None):
        meta(self.root, 64, 48, section)
        text(self.root, 64, 115, title, 48, font=SERIF)
        text(self.root, 64, 161, subtitle, 21, MUTED)
        if number:
            text(self.root, 1136, 114, number, 72, GREEN, SERIF, anchor="end")
        line(self.root, 64, 190, 1136, 190, RULE)

    def footer(self, left, right="HỌC CNTT CÙNG AI"):
        line(self.root, 64, self.height-76, 1136, self.height-76, RULE)
        text(self.root, 64, self.height-40, left, 18, MUTED)
        if right:
            meta(self.root, 1136, self.height-40, right, anchor="end")

    def serialize(self):
        return ET.tostring(self.root, encoding="unicode", xml_declaration=True) + "\n"


def cover(d):
    s = d.root
    meta(s, 64, 52, "CẨM NANG THỰC HÀNH / SINH VIÊN CNTT")
    line(s, 64, 77, 1136, 77, INK)
    meta(s, 64, 143, "NHẬN DIỆN · ĐIỀU KHIỂN")
    meta(s, 64, 174, "TỰ HỌC · TRÁCH NHIỆM")
    text(s, 60, 285, ("Học CNTT", "cùng AI."), 76, font=SERIF, leading=86)
    text(s, 64, 436, ("Đừng chỉ nhận một đáp án.", "Hãy biết vì sao nó đúng."), 27, leading=41)
    line(s, 64, 535, 130, 535, RUST, 4)
    text(s, 64, 577, ("Một bài toán nhỏ.", "Bốn chặng tự chủ."), 27, font=SERIF, leading=38)
    # A shared desk and the actual three-item problem, not a generic AI mascot.
    ellipse(s, 867, 360, 260, 199, PALE)
    path(s, "M636 340 Q866 187 1107 341", stroke=GREEN, width=2, dash="5 9")
    body(s, "Minh", 744, 171, "point", label=False)
    body(s, "Lan", 1028, 171, "explain", label=False)
    text(s, 709, 154, "Minh / C++", 18, font=MONO)
    text(s, 976, 154, "Lan / Web", 18, font=MONO)
    path(s, "M854 303 L925 303 L937 352 H844 Z", PAPER, INK, 3)
    line(s, 842, 357, 941, 357, INK, 5)
    path(s, "M871 317 l-8 8 8 8 M910 317 l8 8 -8 8", stroke=GREEN, width=3)
    line(s, 641, 378, 1123, 378, INK, 7)
    line(s, 672, 378, 650, 460, INK, 4)
    line(s, 1095, 378, 1114, 460, INK, 4)
    d.arrow("M887 385 V427", "green")
    for x, name, amount, idx in ((624, "Cơm trưa", 35000, "01"),
                                 (798, "Xe buýt", 7000, "02"),
                                 (972, "Vở ghi", 18000, "03")):
        receipt(s, x, 447, name, amount, idx)
    path(s, "M637 632 V642 H1117 V632", stroke=GREEN, width=2)
    text(s, 877, 689, "= 60000", 38, INK, MONO, anchor="middle")
    d.footer("Hai nhân vật hư cấu · một tình huống xuyên suốt", "01—04 / MISSION HANDBOOK")


def opener_people(d, minh_pose, lan_pose):
    body(d.root, "Minh", 178, 270, minh_pose)
    body(d.root, "Lan", 1024, 270, lan_pose)


def chapter_01(d):
    s = d.root
    d.heading("CHƯƠNG 01 / AI MYSTERY", "Cùng hỏi. Khác đáp.",
              "Ba phiếu đáp hư cấu: khác do model, ngữ cảnh hay ứng dụng?", "01")
    text(s, 600, 231, "“Vì sao tổng bị thiếu?”", 28, font=SERIF, anchor="middle")
    opener_people(d, "compare", "explain")
    for x, letter, rows, note in (
        (344, "A", ("Lượt cuối", "có chạy?"), "GỢI Ý"),
        (526, "B", ("i <= n", "luôn đúng!"), "CỐ Ý SAI"),
        (708, "C", ("i < n", "Cần test."), "CHƯA CHẠY"),
    ):
        page = sheet(s, x, 276, 160, 222, YELLOW if letter == "B" else PAPER)
        text(page, 17, 50, letter, 40, GREEN, SERIF)
        line(page, 17, 68, 139, 68, RULE)
        text(page, 17, 105, rows, 22, leading=33)
        meta(page, 17, 197, note)
        line(s, x+80, 249, x+80, 270, GREEN, 2)
    text(s, 603, 553, "So điều kiện, không chỉ so câu trả lời.", 23,
         font=SERIF, anchor="middle")
    d.footer("THINK FIRST / Cần thêm bằng chứng nào?", "MINH + LAN / 01")


def chapter_02(d):
    s = d.root
    d.heading("CHƯƠNG 02 / ĐIỀU KHIỂN", "Khoản tiền bị bỏ quên", 
              "Tình huống lỗi chủ đích: chỉ Vở ghi 18000 không được cộng.", "02")
    opener_people(d, "point", "audit")
    meta(s, 356, 239, "n = 3 / CẬN SAI: i < n - 1")
    for x, name, amount, idx, omitted in (
        (344, "Cơm trưa", 35000, "01", False),
        (526, "Xe buýt", 7000, "02", False),
        (708, "Vở ghi", 18000, "03", True),
    ):
        receipt(s, x, 282, name, amount, idx, omitted=omitted)
        if not omitted:
            check(s, x+80, 473)
    # Magnification targets only the omitted last amount, never all three items.
    circle(s, 788, 398, 70, "none", RUST, 3)
    line(s, 838, 448, 870, 480, RUST, 8)
    text(s, 595, 537, "42000 ≠ 60000", 32, font=MONO, anchor="middle")
    text(s, 595, 575, "Theo dấu trước. Sửa cận sau.", 22, anchor="middle")
    d.footer("Bản lỗi minh họa, không phải demo Web đang đúng.", "MINH + LAN / 02")


def chapter_03(d):
    s = d.root
    d.heading("CHƯƠNG 03 / THINK FIRST", "Giữ phần nghĩ cho mình", 
              "AI gợi ý; người học dự đoán, tự sửa và giải thích.", "03")
    opener_people(d, "write", "explain")
    note = sheet(s, 354, 234, 476, 292, PALE)
    meta(note, 26, 37, "GỢI Ý AI / HỘI THOẠI HƯ CẤU")
    text(note, 26, 78, "“Lượt cuối có chạy không?”", 26, font=SERIF)
    line(note, 26, 102, 448, 102, GREEN, 2)
    text(note, 26, 140, "Minh dự đoán", 20, GREEN, weight="600")
    text(note, 26, 178, "i = 2 → bị bỏ → 42000", 24, font=MONO)
    text(note, 26, 225, "Lan giải thích", 20, GREEN, weight="600")
    text(note, 26, 262, "2 < 2 là sai: không cộng 18000.", 22)
    text(s, 594, 576, "Gấp lời giải. Tự nói lại luồng chạy.", 23,
         font=SERIF, anchor="middle")
    d.footer("Tự làm lại với dữ liệu khác, không chỉ chép đáp án.", "MINH + LAN / 03")


def chapter_04(d):
    s = d.root
    d.heading("CHƯƠNG 04 / TRÁCH NHIỆM", "Trước khi bấm chia sẻ", 
              "Minh rà dữ liệu và quyền; Lan đối chiếu nguồn và kiểm thử.", "04")
    opener_people(d, "write", "audit")
    dossier = sheet(s, 352, 226, 490, 316)
    meta(dossier, 26, 38, "PHIẾU RÀ SOÁT / TÌNH HUỐNG HƯ CẤU")
    rows = (("Dữ liệu", "Chỉ dùng dữ liệu giả"),
            ("Quyền", "Chỉ tệp đã cho phép"),
            ("Nguồn", "Ghi nguồn, giấy phép"),
            ("Test", "Đọc kết quả, không đoán"))
    for index, (label, detail) in enumerate(rows):
        y = 88 + index * 62
        check(dossier, 29, y-6)
        text(dossier, 53, y, label, 21, GREEN, weight="600")
        text(dossier, 166, y, detail, 20)
        line(dossier, 25, y+20, 463, y+20, RULE)
    # An envelope is held at the gate until the evidence has been reviewed.
    path(s, "M528 567 H666 V616 H528 Z M528 567 L597 600 L666 567", PAPER, INK, 2)
    d.arrow("M597 545 V561", "green")
    text(s, 687, 600, "Rồi mới chia sẻ", 20)
    d.footer("Nếu lộ key: thu hồi trước khi dọn dấu vết.", "MINH + LAN / 04")


def ecosystem(d):
    s = d.root
    d.heading("AI MAP / CÁCH TRUY CẬP", "Nhiều lối vào, khác điều kiện", 
              "Đường truy cập không phải bảng xếp hạng chất lượng hay thương hiệu.")
    # Three hosted routes converge; local inference stays on the device.
    for y in (265, 363, 461):
        d.arrow(f"M471 {y} H590 Q651 {y} 695 363 H754", "green")
    browser = group(s, 78, 238)
    rect(browser, 0, 0, 76, 48, PALE, INK, 4)
    line(browser, 0, 12, 76, 12, INK)
    path(browser, "M14 23 H59 V36 H35 L24 44 V36 H14 Z", PAPER, INK, 2)
    text(s, 182, 258, "Chat trên web", 25, font=SERIF)
    text(s, 182, 286, "Nhập câu hỏi qua giao diện", 18, MUTED)
    rect(s, 78, 337, 76, 48, PALE, INK, 4)
    path(s, "M101 350 l-10 10 10 10 M132 350 l10 10 -10 10 M121 347 l-8 25",
         stroke=GREEN, width=3)
    text(s, 182, 356, "Gọi API", 25, font=SERIF)
    text(s, 182, 384, "Mã gửi request tới dịch vụ", 18, MUTED)
    rect(s, 78, 435, 76, 48, PALE, INK, 4)
    line(s, 101, 435, 101, 483, INK)
    line(s, 101, 465, 154, 465, INK)
    path(s, "M109 447 l8 5 -8 5 M125 458 h16", stroke=GREEN, width=2)
    text(s, 182, 454, "Trợ lý trong IDE", 25, font=SERIF)
    text(s, 182, 482, "Ngữ cảnh tệp theo quyền", 18, MUTED)
    # An access gate communicates limits without suggesting ownership.
    path(s, "M773 315 V409 M792 315 V409 M764 325 H800 M764 399 H800",
         stroke=INK, width=3)
    meta(s, 777, 280, "DỊCH VỤ", anchor="middle")
    text(s, 778, 448, ("Quyền, dữ liệu", "và hạn mức"), 19, anchor="middle")
    d.arrow("M806 363 H934", "green")
    circle(s, 1025, 363, 70, PALE, GREEN, 2)
    for yy in (342, 363, 384):
        path(s, f"M989 {yy} Q1007 {yy-19} 1025 {yy} T1061 {yy}", stroke=GREEN, width=2)
    text(s, 1025, 470, "Model từ xa", 21, anchor="middle")
    line(s, 64, 519, 1136, 519, RULE, 2, "6 8")
    rect(s, 78, 552, 76, 46, PALE, INK, 4)
    line(s, 73, 605, 161, 605, INK, 3)
    text(s, 182, 568, "Chạy cục bộ", 25, font=SERIF)
    text(s, 182, 598, "Cần cấu hình phù hợp", 18, MUTED)
    d.arrow("M471 578 H754", "green")
    text(s, 784, 568, "Model trên máy", 25, font=SERIF)
    text(s, 784, 598, "Rà cách ứng dụng xử lý dữ liệu", 18, MUTED)
    d.footer("Cùng tên model chưa chắc cùng context hoặc quyền.")


def roles(d):
    s = d.root
    d.heading("BEHIND THE SCENE / BỐN VAI TRÒ", "Ai làm gì trong một lượt hỏi?", 
              "Sơ đồ vai trò truy cập đơn giản hóa; không phải quan hệ sở hữu.")
    centers = (190, 460, 730, 1000)
    meta(s, 600, 232, "REQUEST / NGƯỜI DÙNG GỬI CÂU HỎI ←", anchor="middle")
    meta(s, 600, 458, "RESPONSE / KẾT QUẢ TRẢ VỀ →", GREEN, anchor="middle")
    for start, end in zip(centers[1:], centers[:-1]):
        d.arrow(f"M{start-12} 263 H{end+12}", "rust")
    for start, end in zip(centers[:-1], centers[1:]):
        d.arrow(f"M{start+12} 414 H{end-12}", "green")
    for cx in centers:
        line(s, cx, 263, cx, 288, RUST)
        line(s, cx, 392, cx, 414, GREEN)
    # Model: connected units; provider: service rack; app: interface; user: person.
    for x in (163, 190, 217):
        for y in (316, 343, 370):
            circle(s, x, y, 5, GREEN)
    for offset in (0, 27):
        path(s, f"M163 {316+offset} L190 {343+offset} L217 {316+offset}", stroke=GREEN, width=2)
    for yy in (297, 329, 361):
        rect(s, 416, yy, 88, 24, PALE, INK, 3)
        circle(s, 430, yy+12, 3, GREEN)
        line(s, 447, yy+12, 489, yy+12, GREEN)
    rect(s, 679, 297, 102, 87, PALE, INK, 4)
    line(s, 679, 317, 781, 317, INK)
    path(s, "M695 334 H764 V358 H725 L715 369 V358 H695 Z", PAPER, INK, 2)
    circle(s, 1000, 321, 22, SKIN, INK, 3)
    path(s, "M960 386 Q959 350 1000 350 Q1041 350 1040 386 Z", GREEN, INK, 3)
    for cx, title, rows in (
        (190, "Model", ("Sinh đầu ra", "từ ngữ cảnh")),
        (460, "Provider", ("Vận hành dịch vụ", "và quyền truy cập")),
        (730, "Application", ("Tổ chức giao diện", "và ngữ cảnh gửi đi")),
        (1000, "User", ("Gửi yêu cầu", "nhận, rà kết quả")),
    ):
        text(s, cx, 508, title, 32, font=SERIF, anchor="middle")
        text(s, cx, 550, rows, 20, anchor="middle", leading=31)
    d.footer("Một tổ chức có thể đảm nhiệm nhiều vai trò; mũi tên chỉ luồng trao đổi.", "")


def token_context(d):
    s = d.root
    d.heading("BEHIND THE SCENE / TOKEN & CONTEXT", "Một câu hỏi, nhiều mảnh nhỏ", 
              "Các lát cắt dưới đây chỉ minh họa; không phải kết quả tokenizer thật.")
    pieces = ((76, 160, "Tính"), (248, 172, "tổng"), (432, 112, "["),
              (556, 314, "7000"), (882, 242, "]"))
    for x, width, label in pieces:
        path(s, f"M{x+8} 228 H{x+width} L{x+width-8} 307 H{x} Z",
             YELLOW, INK, 2)
        text(s, x+width/2, 278, label, 32, font=MONO, anchor="middle")
    text(s, 600, 347, "Không suy ra số token hay chi phí từ hình này.", 21,
         MUTED, anchor="middle")
    old = sheet(s, 64, 415, 180, 146, PAPER, MUTED)
    text(old, 18, 46, ("Nội dung", "ngoài cửa sổ"), 20, MUTED, leading=32)
    line(old, 18, 107, 147, 107, RULE)
    # A bounded container, not an infinite memory metaphor.
    rect(s, 300, 411, 836, 151, PALE)
    path(s, "M318 395 H300 V578 H318 M1118 395 H1136 V578 H1118", stroke=GREEN, width=4)
    meta(s, 719, 393, "CỬA SỔ NGỮ CẢNH HỮU HẠN", GREEN, anchor="middle")
    rect(s, 861, 412, 274, 149, YELLOW)
    line(s, 545, 430, 545, 544, GREEN, 2)
    line(s, 859, 430, 859, 544, GREEN, 2, "5 6")
    text(s, 330, 469, ("Chỉ dẫn", "đang có"), 25, font=SERIF, leading=36)
    text(s, 575, 469, ("Dữ liệu + hội thoại", "được đưa vào"), 24, font=SERIF, leading=36)
    text(s, 886, 469, ("Phần dành cho", "đầu ra"), 24, font=SERIF, leading=36)
    cross(s, 272, 485, size=8)
    text(s, 64, 610, "Không tự nhớ phần bị bỏ.", 20, MUTED)
    text(s, 536, 610, "Giới hạn và cách tính tùy model / dịch vụ.", 20, MUTED)
    d.footer("Cần dữ kiện nào? Hãy kiểm tra nó thực sự có trong context.")


def workspace(d):
    s = d.root
    d.heading("MISSION 01 / MÔI TRƯỜNG", "Bên trong một không gian làm việc", 
              "IDE chứa editor và terminal; shell nhận lệnh rồi chạy chương trình CLI.")
    rect(s, 64, 224, 772, 371, PAPER, INK, 5)
    rect(s, 65, 225, 770, 46, INK, radius=4)
    text(s, 86, 256, "IDE / KHÔNG GIAN DỰ ÁN", 20, PAPER, MONO)
    rect(s, 65, 272, 170, 322, PALE)
    meta(s, 82, 308, "TỆP")
    path(s, "M83 334 h21 l7 8 h101 v38 H83 Z", PAPER, GREEN, 2)
    text(s, 91, 366, "bai-lam/", 18, font=MONO)
    line(s, 93, 394, 93, 455, GREEN)
    line(s, 93, 413, 106, 413, GREEN)
    line(s, 93, 450, 106, 450, GREEN)
    text(s, 112, 419, "main.cpp", 18, font=MONO)
    text(s, 112, 456, "test.txt", 18, font=MONO)
    meta(s, 260, 307, "EDITOR / SOẠN MÃ")
    text(s, 261, 350, ("for (int i = 0; i < n; ++i) {", "    total += amounts[i];", "}"),
         21, font=MONO, leading=31)
    rect(s, 236, 436, 599, 158, INK)
    meta(s, 260, 470, "TERMINAL / VÙNG NHẬP, XUẤT", PALE)
    text(s, 260, 512, "$ python --version", 23, PAPER, MONO)
    text(s, 260, 553, "Shell gọi CLI Python → nhận đầu ra", 20, PAPER)
    scope = sheet(s, 890, 247, 246, 303, YELLOW)
    meta(scope, 20, 39, "AI / AGENT")
    text(scope, 20, 86, ("Đọc", "Đề xuất sửa", "Xin chạy lệnh"), 24,
         font=SERIF, leading=43)
    line(scope, 20, 197, 223, 197, INK, 2)
    text(scope, 20, 230, ("Chỉ trong phạm vi", "bạn cho phép."), 20, leading=32)
    d.arrow("M890 345 H846", "rust", "5 6")
    path(s, "M858 324 V369", stroke=RUST, width=4)
    text(s, 891, 588, "Quyền ≠ lời hứa", 21, RUST)
    d.footer("Lệnh, cây tệp chỉ minh họa. Prompt không tự cấp quyền cho Agent.", "")


def workflow(d):
    s = d.root
    d.heading("MISSION / VÒNG LÀM VIỆC", "Điều khiển, không phó mặc", 
              "Bản sửa phải qua test và review; câu trả lời tự tin không thay bằng chứng.")
    xs = (140, 370, 600, 830, 1060)
    d.arrow("M830 277 V244 Q830 229 815 229 H389 Q370 229 370 249 V277", "rust")
    text(s, 600, 219, "Test sai → phân tích lại", 20, RUST, anchor="middle")
    for a, b in zip(xs[:-1], xs[1:]):
        d.arrow(f"M{a+62} 344 H{b-62}", "green")
    for index, x in enumerate(xs):
        circle(s, x, 344, 59, YELLOW if index == 0 else PALE, GREEN, 2)
        meta(s, x+62, 274, f"0{index+1}", anchor="middle")
    text(s, 140, 363, "?", 57, GREEN, SERIF, anchor="middle")
    path(s, "M344 361 L358 338 L373 348 L395 320 M350 316 H389", stroke=GREEN, width=3)
    path(s, "M578 364 L586 343 L610 319 L624 333 L600 358 Z M588 342 L602 356",
         PAPER, GREEN, 3)
    path(s, "M807 316 H850 M817 317 V340 L799 366 Q829 383 859 366 L841 340 V317",
         PAPER, GREEN, 3)
    check(s, 829, 356, size=20)
    path(s, "M1035 314 H1085 V375 H1035 Z", PAPER, GREEN, 2)
    for yy in (329, 348, 367):
        check(s, 1046, yy, size=8)
        line(s, 1060, yy, 1075, yy, GREEN, 2)
    for x, title, rows in zip(xs, ("Ask", "Analyze", "Edit", "Test", "Review"),
                              (("Nêu mục tiêu", "và giới hạn"),
                               ("Đọc bằng chứng", "tìm nguyên nhân"),
                               ("Sửa tối thiểu", "trong phạm vi"),
                               ("Chạy lại", "đối chiếu kỳ vọng"),
                               ("Đọc diff", "tự giải thích"))):
        text(s, x, 449, title, 31, font=SERIF, anchor="middle")
        text(s, x, 488, rows, 20, anchor="middle", leading=31)
    text(s, 945, 329, "Đạt", 18, GREEN, anchor="middle")
    d.arrow("M1060 552 V581 Q1060 597 1040 597 H160 Q140 597 140 577 V552", "ink")
    text(s, 600, 584, "Đổi yêu cầu hoặc phát hiện thiếu → hỏi lại", 20, anchor="middle")
    d.footer("Mỗi lượt: lưu bằng chứng, không chỉ lưu câu trả lời.")


def debugging(d):
    s = d.root
    d.heading("MISSION DEBUG / TRACE TỪNG LƯỢT", "Lượt cuối chưa từng chạy", 
              "Dữ liệu: [35000, 7000, 18000] · n = 3 · total khởi đầu bằng 0.")
    text(s, 64, 235, "Cận sai: i < n - 1  →  i < 2", 27, font=MONO)
    meta(s, 856, 235, "LỖI CHỦ ĐÍCH", RUST)
    # Ruled trace table: the failed guard is a row, not an executed iteration.
    rect(s, 64, 269, 746, 57, INK)
    for x, label in ((89, "i"), (176, "i < 2"), (364, "amounts[i]"), (632, "total")):
        text(s, x, 305, label, 21, PAPER, MONO)
    rect(s, 64, 479, 746, 90, YELLOW)
    for y, i, guard, value, total, failed in (
        (373, "0", "đúng", "35000", "35000", False),
        (450, "1", "đúng", "7000", "42000", False),
        (527, "2", "sai", "18000", "42000", True),
    ):
        color = RUST if failed else INK
        for x, label in ((89, i), (176, guard), (364, value), (632, total)):
            text(s, x, y, label, 25, color, MONO)
        if failed:
            text(s, 364, y+29, "bị bỏ, không cộng", 18, RUST)
        line(s, 64, y+29 if not failed else y+43, 810, y+29 if not failed else y+43, RULE)
    meta(s, 865, 296, "KẾT QUẢ LỖI", RUST)
    text(s, 861, 361, "42000", 48, RUST, MONO)
    line(s, 865, 393, 1110, 393, RULE)
    meta(s, 865, 438, "KỲ VỌNG")
    text(s, 861, 502, "60000", 48, GREEN, MONO)
    text(s, 64, 623, "35000 + 7000 + 18000 = 60000", 29, font=MONO)
    text(s, 64, 670, "Sửa cận thành i < n; kiểm tra dữ liệu đầu vào là bước riêng.", 22)
    d.footer("Mảng rỗng không đủ chứng minh vòng lặp đúng.")


def active_learning(d):
    s = d.root
    d.heading("THINK FIRST / VÒNG HỌC CHỦ ĐỘNG", "Giữ bằng chứng của việc hiểu", 
              "AI chỉ gợi ý. Dự đoán, tự sửa và giải thích vẫn là việc của bạn.")
    positions = ((210, 280), (600, 280), (990, 280),
                 (990, 501), (600, 501), (210, 501))
    for a, b in ((210, 600), (600, 990)):
        d.arrow(f"M{a+61} 280 H{b-61}", "green")
    d.arrow("M1052 280 H1097 Q1120 280 1120 304 V477 Q1120 501 1097 501 H1052", "green")
    d.arrow("M929 501 H661", "green")
    d.arrow("M539 501 H271", "green")
    d.arrow("M149 501 H108 Q80 501 80 475 V306 Q80 280 108 280 H149", "rust", "5 7")
    labels = (("Dự đoán", "Viết kết quả trước"), ("Nhận gợi ý", "Hỏi đúng một điểm nghẽn"),
              ("Tự sửa", "Tự viết phần thay đổi"), ("Chạy test", "So với kỳ vọng"),
              ("Giải thích", "Nói lại khi đóng AI"), ("Biến thể", "Đổi dữ liệu, tự làm lại"))
    for index, ((x, y), (title, subtitle)) in enumerate(zip(positions, labels), 1):
        circle(s, x, y, 52, YELLOW if index == 2 else PALE, GREEN, 2)
        text(s, x, y+16, f"0{index}", 38, font=SERIF, anchor="middle")
        text(s, x, y+89, title, 28, font=SERIF, anchor="middle")
        text(s, x, y+122, subtitle, 19, MUTED, anchor="middle")
    text(s, 600, 428, "Gợi ý không phải lời giải để chép.", 24,
         font=SERIF, anchor="middle")
    d.footer("Không nhớ lại được? Ghi điểm nghẽn và thử một biến thể nhỏ.", "")


def ai_trap(d):
    s = d.root
    d.heading("AI TRAP / PHẢN VÍ DỤ", "Một ca đúng chưa đủ", 
              "Đối chiếu lời tự tin bằng dữ liệu nhỏ nhất có thể bác bỏ nó.")
    text(s, 63, 323, "“", 126, RUST, SERIF)
    text(s, 128, 280, ("Mảng rỗng ra 0,", "nên vòng lặp đúng."), 32,
         font=SERIF, leading=48)
    meta(s, 128, 397, "LỜI AI GIẢ LẬP / KẾT LUẬN SAI", RUST)
    line(s, 128, 438, 536, 438, RULE)
    text(s, 128, 486, "[] → 0", 34, font=MONO)
    text(s, 128, 536, ("Chỉ một ca đi qua.", "Chưa kiểm tra phần tử cuối."), 22, leading=34)
    line(s, 596, 224, 596, 607, RULE)
    meta(s, 660, 247, "THỬ MỘT PHẦN TỬ")
    path(s, "M701 278 H681 V345 H701 M1033 278 H1053 V345 H1033", stroke=GREEN, width=3)
    rect(s, 740, 278, 252, 67, YELLOW)
    text(s, 866, 324, "7000", 34, font=MONO, anchor="middle")
    text(s, 660, 394, "n = 1 → i < n - 1", 24, font=MONO)
    text(s, 660, 434, "i = 0: 0 < 0 là sai", 23, font=MONO)
    line(s, 660, 459, 1120, 459, RULE)
    meta(s, 660, 499, "TRACE BẢN SAI", RUST)
    text(s, 660, 550, "0", 42, RUST, MONO)
    cross(s, 744, 533, size=11)
    meta(s, 897, 499, "KỲ VỌNG")
    text(s, 897, 550, "7000", 42, GREEN, MONO)
    text(s, 660, 603, "Phản ví dụ bác bỏ kết luận.", 23, font=SERIF)
    d.footer("Vòng lặp lỗi đang xét: i bắt đầu từ 0, điều kiện i < n - 1.", "")


def security(d):
    s = d.root
    d.heading("SECURITY ALERT / KEY BỊ LỘ", "Thu hồi trước. Dọn sau.", 
              "Xóa chuỗi khỏi tệp không vô hiệu hóa thông tin đã bị lộ.")
    circle(s, 130, 295, 62, INK)
    text(s, 130, 312, "02", 45, PAPER, SERIF, anchor="middle")
    text(s, 228, 283, ("Thu hồi key", "tại nhà cung cấp"), 32,
         font=SERIF, leading=43)
    text(s, 228, 383, ("Làm ngay sau bước 01.", "Không chờ dọn Git xong."), 22, leading=34)
    key = sheet(s, 90, 466, 456, 129, YELLOW)
    meta(key, 24, 36, "NHÃN GIẢ / KHÔNG PHẢI KEY THẬT")
    text(key, 24, 80, "KEY_DEMO_INVALID", 27, font=MONO)
    line(key, 20, 70, 371, 70, RUST, 3)
    text(key, 24, 110, "ĐÃ THU HỒI", 18, RUST, MONO)
    line(s, 724, 280, 724, 625, GREEN, 3)
    steps = (
        (267, "01", "Dừng chia sẻ thêm", "Không gửi lại tệp, không chụp nguyên key."),
        (350, "03", "Kiểm tra mức sử dụng", "Lượt gọi, chi phí, mốc thời gian lạ."),
        (433, "04", "Rà bản liên quan", "Commit, cấu hình, ảnh, chat trong phạm vi."),
        (516, "05", "Báo đúng đầu mối", "Mô tả sự cố; không đính kèm key."),
        (599, "06", "Giảm bản lưu, chặn tái diễn", "Không tự viết lại lịch sử kho mã."),
    )
    for y, number, title, detail in steps:
        circle(s, 724, y, 22, YELLOW if number == "06" else PALE, GREEN, 2)
        text(s, 724, y+7, number, 18, font=MONO, anchor="middle")
        text(s, 763, y-3, title, 22, weight="600")
        text(s, 763, y+27, detail, 18, MUTED)
    text(s, 90, 662, "Thứ tự: 01 dừng chia sẻ → 02 thu hồi → 03–06 khắc phục.", 22)
    d.footer("Ví dụ giả lập; không đưa key thật vào ảnh, prompt hoặc kho mã.", "")


def final_boss(d):
    s = d.root
    d.heading("FINAL BOSS / BA MỨC THỰC HÀNH", "Nâng năng lực, không nâng gói phí", 
              "Gold mở rộng quy trình từ Bronze hoặc Silver, không phải mua công cụ đắt hơn.")
    # Three evidence workbenches; the rise encodes scope of responsibility.
    stages = (
        (64, 383, 320, "BRONZE", "C++", ("Sửa hai lỗi chủ đích", "Trace + test + bảo vệ"), PALE),
        (424, 330, 320, "SILVER", "Web", ("Theo luồng nhiều tệp", "Sửa lỗi + test + nguồn"), PALE),
        (784, 253, 352, "GOLD", "Kiểm soát Agent", ("Phạm vi + quyền + diff", "Test + review + khai báo"), YELLOW),
    )
    for x, y, width, label, title, details, fill in stages:
        # Bound pages are purposeful artifacts, not ornamental achievement badges.
        page = sheet(s, x+16, y, width-32, 177, fill)
        line(page, 12, 12, 12, 161, GREEN, 3)
        meta(page, 28, 36, label)
        text(page, 28, 80, title, 29, font=SERIF)
        text(page, 28, 118, details, 20, leading=32)
        line(s, x, y+188, x+width, y+188, GREEN, 4)
        line(s, x+16, y+188, x+16, 603, GREEN, 2)
        line(s, x+width-16, y+188, x+width-16, 603, GREEN, 2)
    d.arrow("M224 365 V239 H754 Q766 239 766 252 V293 H791", "green", "5 6")
    d.arrow("M584 311 V288 H735 Q752 288 752 304 V326 H791", "green")
    text(s, 805, 502, ("Không có AI?", "Mô phỏng quy trình thủ công.", "Ghi rõ đó là mô phỏng."), 20, leading=30)
    rect(s, 64, 624, 1072, 60, INK)
    text(s, 90, 663, "KHÔNG CẦN TRẢ PHÍ", 23, PAPER, MONO)
    text(s, 462, 663, "Đánh giá bằng bài làm và khả năng giải thích.", 22, PAPER)
    d.footer("Làm trên bản sao; giữ nguyên các demo tham khảo.")


def skill_map(d):
    s = d.root
    d.heading("SKILL UNLOCKED / BẢN ĐỒ BẰNG CHỨNG", "Bốn năng lực. Bốn dấu vết.", 
              "Tự đánh giá bằng việc làm được và giải thích được, không bằng thanh tiến độ.")
    # Four document branches, not a radar chart that fabricates numeric ability.
    path(s, "M516 365 C450 365 449 294 384 294 M684 365 C753 365 752 294 816 294 "
         "M516 447 C448 447 449 529 384 529 M684 447 C752 447 753 529 816 529",
         stroke=GREEN, width=3)
    circle(s, 600, 406, 90, PALE, GREEN, 3)
    text(s, 600, 384, ("Tự làm", "Tự giải thích"), 25, font=SERIF,
         anchor="middle", leading=39)
    meta(s, 600, 458, "BẰNG CHỨNG", GREEN, anchor="middle")
    for x, y, number, label, evidence in (
        (64, 220, "01", "Nhận diện công cụ", ("Bản đồ vai trò", "Lý do chọn cách truy cập")),
        (816, 220, "02", "Điều khiển quá trình", ("Trace, diff và test", "Lý do cho từng thay đổi")),
        (64, 455, "03", "Giữ năng lực tự làm", ("Dự đoán trước gợi ý", "Bài biến thể không AI")),
        (816, 455, "04", "Chịu trách nhiệm", ("Phiếu rà dữ liệu, nguồn", "Quyền và khai báo AI")),
    ):
        page = sheet(s, x, y, 320, 157)
        meta(page, 20, 31, f"{number} / NĂNG LỰC")
        text(page, 20, 70, label, 24, font=SERIF)
        text(page, 20, 107, evidence, 20, leading=30)
        line(page, 0, 157, 70, 157, RUST, 4)
    d.footer("Tự đánh dấu đã học không phải chứng nhận năng lực.", "")


@dataclass(frozen=True)
class Visual:
    slug: str
    title: str
    alt: str
    purpose: str
    draw: Callable[[Drawing], None]
    height: int = 720

    def manifest_entry(self):
        return {"title": self.title, "path": f"assets/{self.slug}.svg",
                "alt": self.alt, "purpose": self.purpose}


VISUALS: Sequence[Visual] = (
    Visual("cover", "Học CNTT cùng AI — một bài toán, bốn chặng",
           "Minh tóc đen ngắn áo xanh và Lan tóc đen ngang vai áo cam cùng đọc ba phiếu: "
           "Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000; tổng đúng là 60000.",
           "Mở tình huống chung của cẩm nang và giới thiệu hai nhân vật hư cấu xuyên suốt.", cover, 780),
    Visual("chapter-01", "Cùng hỏi. Khác đáp.",
           "Minh so ba phiếu đáp hư cấu A, B, C; Lan cùng đặt câu hỏi về model, context và ứng dụng.",
           "Khơi gợi việc so điều kiện tạo đáp án thay vì xếp hạng giao diện AI.", chapter_01),
    Visual("chapter-02", "Khoản tiền bị bỏ quên",
           "Hai khoản 35000 và 7000 được cộng; chỉ phiếu Vở ghi 18000 được khoanh là bị bỏ. "
           "Minh chỉ dữ liệu, Lan rà ghi chép; bản lỗi cho 42000 thay vì 60000.",
           "Dẫn vào truy dấu lỗi bỏ phần tử cuối, không làm hỏng demo Web vốn đúng.", chapter_02),
    Visual("chapter-03", "Giữ phần nghĩ cho mình",
           "Minh tự viết dự đoán i=2 bị bỏ; Lan giải thích 2<2 là sai. AI chỉ gợi ý xem lượt cuối.",
           "Tách hỗ trợ của AI khỏi trách nhiệm dự đoán và giải thích của người học.", chapter_03),
    Visual("chapter-04", "Trước khi bấm chia sẻ",
           "Minh và Lan rà phiếu dữ liệu, quyền, nguồn, test trước khi gửi bài. "
           "Chú thích nhắc thu hồi key bị lộ trước khi dọn dấu vết.",
           "Biến trách nhiệm thành những việc cụ thể trước khi chia sẻ.", chapter_04),
    Visual("ecosystem", "Nhiều lối vào, khác điều kiện",
           "Chat web, API và trợ lý IDE đi qua cổng dịch vụ tới model từ xa; "
           "một nhánh riêng chạy model trên máy. Không có thứ hạng thương hiệu.",
           "Phân biệt cách truy cập, quyền, dữ liệu và điều kiện vận hành.", ecosystem),
    Visual("roles", "Ai làm gì trong một lượt hỏi?",
           "Bốn vai trò xếp Model, Provider, Application, User. Request đi ngược từ User tới Model; "
           "response xuôi từ Model tới User. Mũi tên không biểu thị quan hệ sở hữu.",
           "Giải thích vai trò và luồng trao đổi; một tổ chức có thể đảm nhiệm nhiều vai trò.", roles),
    Visual("token-context", "Một câu hỏi, nhiều mảnh nhỏ",
           "Năm lát cắt giả định minh họa token, không phải tokenizer thật. Cửa sổ hữu hạn có "
           "chỉ dẫn, dữ liệu, hội thoại và phần dành cho đầu ra; nội dung ngoài cửa sổ không tự được nhớ.",
           "Làm rõ tính minh họa của token và giới hạn ngữ cảnh, không suy diễn số token hay chi phí.", token_context),
    Visual("workspace", "Bên trong một không gian làm việc",
           "Khung IDE chứa cây tệp, editor và terminal. Trong terminal, shell nhận python --version "
           "và gọi CLI Python. AI hoặc Agent ở ngoài ranh giới quyền đọc, sửa, chạy lệnh.",
           "Phân biệt IDE, editor, terminal, shell, CLI và quyền giới hạn của Agent.", workspace),
    Visual("workflow", "Điều khiển, không phó mặc",
           "Ask sang Analyze, Edit, Test, Review. Test sai quay lại Analyze; đổi yêu cầu "
           "hoặc phát hiện thiếu sau review quay lại Ask.",
           "Thể hiện quy trình có vòng kiểm chứng thay vì chuỗi giao việc một chiều.", workflow),
    Visual("debugging", "Lượt cuối chưa từng chạy",
           "Trace n=3, total=0, cận i<n-1: i=0 cộng 35000; i=1 cộng 7000 thành 42000; "
           "i=2 không thỏa 2<2, bỏ 18000. Kỳ vọng 60000; sửa cận i<n, validation là bước riêng.",
           "Chỉ rõ lượt kiểm tra điều kiện thất bại và sai lệch tổng bằng dữ liệu cụ thể.", debugging, 780),
    Visual("active-learning", "Giữ bằng chứng của việc hiểu",
           "Vòng sáu bước hai hàng: dự đoán, nhận gợi ý, tự sửa, chạy test, giải thích, biến thể; "
           "biến thể quay về dự đoán. AI chỉ hỗ trợ ở bước gợi ý.",
           "Gợi một vòng học chủ động có bằng chứng tự làm, không khẳng định tác động trí nhớ.", active_learning),
    Visual("ai-trap", "Một ca đúng chưa đủ",
           "Lời AI giả lập sai: mảng rỗng ra 0 nên vòng lặp đúng. Phản ví dụ [7000] với "
           "i=0, n=1, cận i<n-1 làm 0<0 sai: thực tế 0, kỳ vọng 7000.",
           "Dùng một phản ví dụ nhỏ để bác bỏ kết luận tự tin nhưng thiếu kiểm chứng.", ai_trap),
    Visual("security", "Thu hồi trước. Dọn sau.",
           "Sáu bước theo đúng thứ tự trong chương: 01 dừng chia sẻ thêm; 02 thu hồi key ở nhà cung "
           "cấp, ô lớn bên trái; 03 kiểm tra mức sử dụng; 04 rà bản liên quan; 05 báo đúng đầu mối; "
           "06 giảm bản lưu và chặn tái diễn, không tự viết lại lịch sử kho mã. "
           "Nhãn KEY_DEMO_INVALID không phải key thật.",
           "Ưu tiên vô hiệu hóa thông tin xác thực trước dọn dấu vết và phòng ngừa tái diễn.", security, 780),
    Visual("final-boss", "Nâng năng lực, không nâng gói phí",
           "Bronze thực hành C++, Silver thực hành Web, Gold nâng quy trình kiểm soát Agent "
           "từ một trong hai nhánh: quyền, diff, test, review, khai báo. Không cần trả phí; "
           "không có AI có thể mô phỏng thủ công và ghi rõ.",
           "Phân mức theo năng lực và bằng chứng, không theo giá công cụ.", final_boss, 780),
    Visual("skill-map", "Bốn năng lực. Bốn dấu vết.",
           "Bốn nhánh bằng chứng quanh tự làm, tự giải thích: bản đồ công cụ; trace, diff, test; "
           "dự đoán và bài không AI; phiếu rà dữ liệu, nguồn, quyền và khai báo.",
           "Liên kết bốn năng lực với sản phẩm quan sát được, không chứng nhận tự động.", skill_map),
)


EXPECTED_SLUGS = (
    "cover", "chapter-01", "chapter-02", "chapter-03", "chapter-04",
    "ecosystem", "roles", "token-context", "workspace", "workflow", "debugging",
    "active-learning", "ai-trap", "security", "final-boss", "skill-map",
)


def validate_svg(source: str, visual: Visual) -> None:
    """Structural safety checks only; no claim of font metrics or rendered QA."""
    root = ET.fromstring(source)
    if root.tag != f"{{{NS}}}svg" or root.get("viewBox") != f"0 0 1200 {visual.height}":
        raise ValueError(f"Invalid SVG canvas: {visual.slug}")
    if visual.height not in (720, 780):
        raise ValueError(f"Unexpected canvas height: {visual.slug}")
    for tag in ("title", "desc"):
        node = root.find(f"{{{NS}}}{tag}")
        if node is None or not (node.text or "").strip():
            raise ValueError(f"Missing accessible {tag}: {visual.slug}")
    allowed = {"svg", "title", "desc", "defs", "marker", "g", "rect", "line",
               "path", "circle", "ellipse", "text", "tspan"}
    ids = [node.get("id") for node in root.iter() if node.get("id")]
    if len(ids) != len(set(ids)):
        raise ValueError(f"Duplicate SVG ids: {visual.slug}")
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] not in allowed:
            raise ValueError(f"Unsupported embedded content: {visual.slug}")
        for key, value in node.attrib.items():
            local_key = key.rsplit("}", 1)[-1]
            if local_key in {"href", "src", "style"} or local_key.lower().startswith("on"):
                raise ValueError(f"External or executable attribute: {visual.slug}")
            if "url(" in value and not (value.startswith("url(#") and value.endswith(")")
                                         and value[5:-1] in ids):
                raise ValueError(f"Nonlocal or unresolved reference: {visual.slug}")
        if node.tag == f"{{{NS}}}text":
            if float(node.get("font-size", "0")) < 18:
                raise ValueError(f"Text below 18px: {visual.slug}")
            if node.get("font-family") not in (SERIF, SANS, MONO):
                raise ValueError(f"Unexpected font stack: {visual.slug}")
            x, y = float(node.get("x", "0")), float(node.get("y", "0"))
            # Character labels are local coordinates in a translated group.
            # Deliberately do not pretend these are measured glyph bounds.
            if x > 1200 or y > visual.height:
                raise ValueError(f"Text origin outside canvas: {visual.slug}")


def build_visuals():
    """Create and validate the full batch in memory before any filesystem writes."""
    if tuple(item.slug for item in VISUALS) != EXPECTED_SLUGS:
        raise ValueError("The editorial collection must contain exactly the required 16 SVGs")
    result = []
    for visual in VISUALS:
        drawing = Drawing(visual.slug, visual.title, visual.alt, visual.height)
        visual.draw(drawing)
        source = drawing.serialize()
        validate_svg(source, visual)
        entry = visual.manifest_entry()
        if not all(isinstance(value, str) and value.strip() for value in entry.values()):
            raise ValueError(f"Incomplete gallery entry: {visual.slug}")
        result.append((visual, source, entry))
    return result


def main() -> None:
    batch = build_visuals()
    ASSETS.mkdir(parents=True, exist_ok=True)
    for visual, source, _ in batch:
        (ASSETS / f"{visual.slug}.svg").write_text(source, encoding="utf-8")
    manifest = [entry for _, _, entry in batch]
    (ASSETS / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(batch)} SVGs and assets/manifest.json; rendered review still required.")


if __name__ == "__main__":
    main()
