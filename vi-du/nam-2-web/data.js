/* Dữ liệu giả, dùng số nguyên VND. Dùng được trong browser và Node.js. */
(function () {
  'use strict';
  const MAX_AMOUNT = 1000000000;
  const MAX_ITEMS = 500;
  const categories = Object.freeze({ 'an-uong': 'Ăn uống', 'di-lai': 'Đi lại', 'hoc-tap': 'Học tập', 'khac': 'Khác' });
  function validAmount(amount) {
    return Number.isSafeInteger(amount) && amount > 0 && amount <= MAX_AMOUNT;
  }
  function parseAmount(input) {
    if (typeof input !== 'string' || !/^[0-9]+$/.test(input.trim())) {
      throw new Error('Nhập số nguyên VND, không có dấu chấm, phẩy hay chữ.');
    }
    const amount = Number(input.trim());
    if (!validAmount(amount)) throw new Error('Số tiền phải từ 1 đến 1.000.000.000 VND.');
    return amount;
  }
  function totalExpenses(expenses) {
    if (!Array.isArray(expenses) || expenses.length > MAX_ITEMS) throw new Error('Danh sách tối đa 500 khoản.');
    let total = 0;
    for (const expense of expenses) {
      if (!expense || !validAmount(expense.amount)) throw new Error('amount phải là số nguyên VND hợp lệ.');
      total += expense.amount;
    }
    return total;
  }
  function normalizeExpenses(input) {
    if (!Array.isArray(input) || input.length > MAX_ITEMS) throw new Error('Dữ liệu lưu không đúng định dạng.');
    const ids = new Set();
    return input.map(item => {
      if (!item || !Number.isSafeInteger(item.id) || item.id < 1 || ids.has(item.id) ||
          typeof item.title !== 'string' || !item.title.trim() || item.title.trim().length > 80 ||
          typeof item.category !== 'string' || !Object.hasOwn(categories, item.category) || !validAmount(item.amount)) {
        throw new Error('Một khoản lưu sẵn không hợp lệ.');
      }
      ids.add(item.id);
      return { id: item.id, title: item.title.trim(), amount: item.amount, category: item.category };
    });
  }
  function sampleExpenses() {
    return [
      { id: 1, title: 'Cơm trưa', amount: 35000, category: 'an-uong' },
      { id: 2, title: 'Xe buýt', amount: 7000, category: 'di-lai' },
      { id: 3, title: 'Vở ghi', amount: 18000, category: 'hoc-tap' }
    ];
  }
  const api = Object.freeze({ parseAmount, totalExpenses, normalizeExpenses, sampleExpenses, categories, MAX_AMOUNT, MAX_ITEMS });
  globalThis.ViData = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})();
