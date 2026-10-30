// BAN CO LOI CO CHU DICH: giu lai de hoc, khong dung lam dap an.
#include <iostream>
#include <vector>

int main() {
    std::vector<long long> amounts = {35000, 7000, 18000};
    long long total = 0;
    int n = static_cast<int>(amounts.size());
    for (int i = 0; i < n - 1; ++i) {
        total += amounts[i];
    }
    std::cout << "Tong chi tieu: " << total << " VND\n";
    // Ket qua du kien khi chay: 42000; yeu cau dung la 60000.
    return 0;
}
