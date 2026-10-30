'use strict';
// FINAL BOSS: hai loi chu dich, tach khoi demo Web dung.
// API chi cho bai test Node. Khong gan tep nay vao trang Web tham khao.
function parseAmount(input) {
  if (typeof input !== 'string') throw new Error('Phai la chuoi');
  const amount = parseInt(input.trim(), 10);
  if (!Number.isSafeInteger(amount) || amount <= 0 || amount > 1e9)
    throw new Error('Tien ngoai mien hop le');
  return amount;
}
function totalExpenses(expenses) {
  if (!Array.isArray(expenses) || expenses.length > 500) throw new Error('Danh sach sai');
  for (const item of expenses) {
    if (!item || !Number.isSafeInteger(item.amount) || item.amount <= 0 || item.amount > 1e9)
      throw new Error('amount sai');
  }
  return expenses.reduce((total, item) => total + item.value, 0);
}
module.exports = { parseAmount, totalExpenses };
