// ViSinhVien: du lieu gia cho bai hoc, so tien tinh bang VND nguyen.
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

long long totalExpenses(const std::vector<long long>& amounts) {
    if (amounts.size() > 500) {
        throw std::invalid_argument("Toi da 500 khoan chi");
    }
    long long total = 0;
    int n = static_cast<int>(amounts.size());
    for (int i = 0; i < n; ++i) {
        if (amounts[i] <= 0 || amounts[i] > 1000000000LL) {
            throw std::invalid_argument("Moi khoan: 1 den 1000000000 VND");
        }
        total += amounts[i];
    }
    return total;
}

int runTests() {
    int passed = 0;
    int failed = 0;
    auto check = [&](const std::string& label, bool ok) {
        std::cout << (ok ? "PASS " : "FAIL ") << label << '\n';
        if (ok) ++passed; else ++failed;
    };
    check("ba khoan", totalExpenses({35000, 7000, 18000}) == 60000);
    check("danh sach rong", totalExpenses({}) == 0);
    check("mot khoan", totalExpenses({7000}) == 7000);
    check("khoan chi 1 VND", totalExpenses({1}) == 1);
    check("500 khoan lon", totalExpenses(std::vector<long long>(500, 1000000000LL)) == 500000000000LL);
    for (long long bad : {0LL, -1000LL, 1000000001LL}) {
        bool rejected = false;
        try { totalExpenses({bad}); }
        catch (const std::invalid_argument&) { rejected = true; }
        check("tu choi " + std::to_string(bad), rejected);
    }
    bool rejected = false;
    try { totalExpenses(std::vector<long long>(501, 1)); }
    catch (const std::invalid_argument&) { rejected = true; }
    check("tu choi 501 khoan", rejected);
    std::cout << passed << " passed, " << failed << " failed\n";
    return failed == 0 ? 0 : 1;
}

int main(int argc, char* argv[]) {
    if (argc == 2 && std::string(argv[1]) == "--test") return runTests();
    const std::vector<long long> amounts = {35000, 7000, 18000};
    std::cout << "Com trua: 35000 VND\nXe buyt: 7000 VND\nVo ghi: 18000 VND\n";
    std::cout << "Tong chi tieu: " << totalExpenses(amounts) << " VND\n";
    return 0;
}
