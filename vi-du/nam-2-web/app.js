/* Không server, không gọi API, không gửi dữ liệu ra mạng. */
(function () {
  'use strict';
  const D = globalThis.ViData;
  const STORAGE_KEY = 'visinhvien-demo-v1';
  const form = document.getElementById('expense-form');
  const list = document.getElementById('expenses');
  const message = document.getElementById('message');
  const storageNotice = document.getElementById('storage-notice');
  const format = new Intl.NumberFormat('vi-VN');
  let expenses = D.sampleExpenses();
  let persistent = true;
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved !== null) expenses = D.normalizeExpenses(JSON.parse(saved));
  } catch (error) {
    persistent = false;
    storageNotice.textContent = 'Không đọc được dữ liệu lưu. Đang dùng dữ liệu mẫu trong bộ nhớ; tải lại sẽ mất thay đổi. Không ghi đè dữ liệu cũ.';
  }
  function save() {
    if (!persistent) return;
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(expenses));
      storageNotice.textContent = 'Dữ liệu giả lưu trong trình duyệt này. Không đồng bộ và không có tài khoản đăng nhập.';
    } catch (error) {
      persistent = false;
      storageNotice.textContent = 'Trình duyệt không cho lưu hoặc đã hết dung lượng. Dùng bộ nhớ tạm; tải lại có thể mất thay đổi.';
    }
  }
  function render() {
    list.replaceChildren();
    for (const item of expenses) {
      const row = document.createElement('tr');
      for (const value of [item.title, D.categories[item.category], format.format(item.amount) + ' đ']) {
        const cell = document.createElement('td');
        cell.textContent = value;
        row.append(cell);
      }
      const action = document.createElement('td');
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'delete';
      button.textContent = 'Xóa';
      button.setAttribute('aria-label', 'Xóa khoản ' + item.title);
      button.addEventListener('click', () => {
        expenses = expenses.filter(expense => expense.id !== item.id);
        save(); render();
        message.textContent = 'Đã xóa khoản chi giả. Có thể dùng nút Khôi phục mẫu để làm lại bài.';
      });
      action.append(button); row.append(action); list.append(row);
    }
    document.getElementById('total').textContent = format.format(D.totalExpenses(expenses)) + ' đ';
    document.getElementById('count').textContent = expenses.length + ' khoản chi';
    document.getElementById('empty').hidden = expenses.length !== 0;
  }
  form.addEventListener('submit', event => {
    event.preventDefault();
    try {
      if (expenses.length >= D.MAX_ITEMS) throw new Error('Bản học tập giới hạn 500 khoản chi.');
      const title = form.elements.title.value.trim();
      if (!title || title.length > 80) throw new Error('Tên khoản chi cần từ 1 đến 80 ký tự.');
      const amount = D.parseAmount(form.elements.amount.value);
      const category = form.elements.category.value;
      // Chọn id nhỏ nhất chưa được dùng, tránh vượt miền số nguyên an toàn.
      const usedIds = new Set(expenses.map(item => item.id));
      let id = 1;
      while (usedIds.has(id)) id += 1;
      expenses = D.normalizeExpenses([...expenses, { id, title, amount, category }]);
      save(); render(); form.reset(); form.elements.title.focus();
      message.textContent = 'Đã thêm khoản chi giả. Hãy tự nhẩm tổng để đối chiếu.';
    } catch (error) {
      message.textContent = error.message;
    }
  });
  document.getElementById('reset').addEventListener('click', () => {
    if (!window.confirm('Thay mọi khoản trong bản demo bằng 3 khoản mẫu? Không dùng nút này với dữ liệu cần giữ.')) return;
    expenses = D.sampleExpenses();
    save(); render(); message.textContent = 'Đã khôi phục ba khoản mẫu, tổng 60.000 đ.';
  });
  render();
})();
