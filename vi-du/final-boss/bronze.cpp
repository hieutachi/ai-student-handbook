// FINAL BOSS: bai tap co HAI LOI CHU DICH, khong phai ban dung de su dung.
// Chi sua ban sao cua tep nay. Tien nguyen VND 1..1e9, toi da 500 khoan.
#include <iostream>
#include <stdexcept>
#include <vector>

long long totalExpenses(const std::vector<long long>& amounts) {
    if (amounts.size() > 500) throw std::invalid_argument("Toi da 500 khoan");
    for (long long amount : amounts) {
        if (amount <= 0 || amount >= 1000000000LL)
            throw std::invalid_argument("Tien ngoai mien hop le");
    }
    long long total = 0;
    int n = static_cast<int>(amounts.size());
    for (int i = 0; i < n - 1; ++i) total += amounts[i];
    return total;
}

int main() {
    int passed = 0, failed = 0;
    auto check = [&](const char* name, const std::vector<long long>& input,
                     long long expected, bool reject = false) {
        bool ok = false;
        try { long long actual = totalExpenses(input); ok = !reject && actual == expected; }
        catch (const std::invalid_argument&) { ok = reject; }
        std::cout << (ok ? "PASS " : "FAIL ") << name << '\n';
        if (ok) ++passed; else ++failed;
    };
    check("ba khoan", {35000, 7000, 18000}, 60000);
    check("rong", {}, 0);
    check("mot khoan", {7000}, 7000);
    check("bien tren hop le", {1000000000LL}, 1000000000LL);
    check("500 khoan lon", std::vector<long long>(500, 1000000000LL), 500000000000LL);
    check("tu choi 0", {0}, 0, true);
    check("tu choi am", {-1}, 0, true);
    check("tu choi vuot tien", {1000000001LL}, 0, true);
    check("tu choi 501", std::vector<long long>(501, 1), 0, true);
    std::cout << passed << " passed, " << failed << " failed\n";
    return failed ? 1 : 0;
}
