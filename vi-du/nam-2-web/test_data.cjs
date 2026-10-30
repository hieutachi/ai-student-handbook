'use strict';
const assert = require('node:assert/strict');
const D = require('./data.js');
let passed = 0;
let failed = 0;
function test(name, fn) {
  try { fn(); passed++; console.log('PASS ' + name); }
  catch (error) { failed++; console.error('FAIL ' + name + ': ' + error.message); }
}
test('ba khoản = 60000', () => assert.equal(D.totalExpenses(D.sampleExpenses()), 60000));
test('rỗng = 0', () => assert.equal(D.totalExpenses([]), 0));
test('một khoản = 7000', () => assert.equal(D.totalExpenses([{ amount: 7000 }]), 7000));
test('500 khoản lớn vẫn nguyên chính xác', () => assert.equal(D.totalExpenses(Array.from({ length: 500 }, () => ({ amount: 1e9 }))), 5e11));
for (const [input, expected] of [['35000', 35000], [' 7000 ', 7000], ['1', 1], ['0007', 7], ['1000000000', 1e9]]) {
  test('parse ' + JSON.stringify(input), () => assert.equal(D.parseAmount(input), expected));
}
for (const input of ['', ' ', '0', '-1', '15k', '15.000', '15,000', '3.5', '1e3', 'Infinity', '1000000001', 35000, null]) {
  test('từ chối ' + JSON.stringify(input), () => assert.throws(() => D.parseAmount(input)));
}
test('từ chối amount là chuỗi', () => assert.throws(() => D.totalExpenses([{ amount: '35000' }])));
test('từ chối sai tên trường value', () => assert.throws(() => D.totalExpenses([{ value: 35000 }])));
test('từ chối 501 khoản', () => assert.throws(() => D.totalExpenses(Array.from({ length: 501 }, () => ({ amount: 1 })))));
test('không thay đổi dữ liệu gốc', () => { const data = D.sampleExpenses(); const before = JSON.stringify(data); D.totalExpenses(data); assert.equal(JSON.stringify(data), before); });
test('schema lưu hợp lệ', () => assert.deepEqual(D.normalizeExpenses(D.sampleExpenses()), D.sampleExpenses()));
test('từ chối id trùng', () => assert.throws(() => D.normalizeExpenses([D.sampleExpenses()[0], D.sampleExpenses()[0]])));
test('từ chối title rỗng', () => assert.throws(() => D.normalizeExpenses([{ id: 1, title: ' ', amount: 1, category: 'khac' }])));
test('từ chối category lạ', () => assert.throws(() => D.normalizeExpenses([{ id: 1, title: 'Vở', amount: 1, category: 'toString' }])));
test('từ chối category mảng dù ép sang khóa hợp lệ', () => assert.throws(() => D.normalizeExpenses([{ id: 1, title: 'Vở', amount: 1, category: ['khac'] }])));
test('giữ tiêu đề có ký hiệu như dữ liệu', () => assert.equal(D.normalizeExpenses([{ id: 1, title: '<b>Vở</b>', amount: 1, category: 'hoc-tap' }])[0].title, '<b>Vở</b>'));
test('bài lỗi chuỗi minh họa', () => assert.equal('35000' + '7000', '350007000'));
test('bài lỗi value minh họa', () => assert.equal(Number.isNaN(D.sampleExpenses().reduce((sum, item) => sum + item.value, 0)), true));
console.log(`${passed} passed, ${failed} failed`);
process.exitCode = failed ? 1 : 0;
