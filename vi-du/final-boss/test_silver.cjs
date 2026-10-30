'use strict';
const assert = require('node:assert/strict');
const D = require('./silver.cjs');
let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); passed++; console.log('PASS '+name); }
  catch (error) { failed++; console.error('FAIL '+name+': '+error.message); }
}
const sample = [{amount:35000},{amount:7000},{amount:18000}];
test('ba khoan',()=>assert.equal(D.totalExpenses(sample),60000));
test('rong',()=>assert.equal(D.totalExpenses([]),0));
test('mot khoan',()=>assert.equal(D.totalExpenses([{amount:7000}]),7000));
test('500 khoan lon',()=>assert.equal(D.totalExpenses(Array.from({length:500},()=>({amount:1e9}))),5e11));
test('parse hop le',()=>assert.equal(D.parseAmount(' 35000 '),35000));
test('tu choi hau to abc',()=>assert.throws(()=>D.parseAmount('35000abc')));
test('tu choi so le',()=>assert.throws(()=>D.parseAmount('1.5')));
test('tu choi ky hieu mu',()=>assert.throws(()=>D.parseAmount('1e3')));
test('tu choi rong',()=>assert.throws(()=>D.parseAmount('')));
test('tu choi 0',()=>assert.throws(()=>D.parseAmount('0')));
test('tu choi amount chuoi',()=>assert.throws(()=>D.totalExpenses([{amount:'35000'}])));
test('tu choi 501 khoan',()=>assert.throws(()=>D.totalExpenses(Array.from({length:501},()=>({amount:1})))));
console.log(`${passed} passed, ${failed} failed`);
process.exitCode = failed ? 1 : 0;
