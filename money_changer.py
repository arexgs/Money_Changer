from forex_python.converter import CurrencyRates
from decimal import Decimal, ROUND_HALF_UP

def get_exchange_rate_idr_to_usd():
    try:
        c = CurrencyRates()
        rate = c.get_rate('IDR', 'USD')
        return Decimal(str(rate))
    except Exception as e:
        print(f"\nGagal mengambil nilai tukar real-time: {e}. Menggunakan nilai cadangan.")
        return Decimal('0.00006024')
    
def greedy_denomination(amount_usd):
    denominations = [
        Decimal('100.00'), Decimal('50.00'), Decimal('20.00'), Decimal('10.00'), Decimal('5.00'), Decimal('2.00'),
        Decimal('1.00'), Decimal('0.50'), Decimal('0.25'), Decimal('0.10'), Decimal('0.05'), Decimal('0.01')
    ]

    # Menyimpan hasil penukaran menggunakan dictionary
    result = {}
    remaining_amount = amount_usd

    print("\n--- Rincian Penukaran ---")
    for denom in denominations:
        count = int(remaining_amount/denom)

        if count > 0:
            result[denom] = count
            used_amount = denom * count
            remaining_amount -= used_amount
            remaining_amount = remaining_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            print(f"Menggunakan {count} lembar/keping ${denom:.2f}")
    
    return result

def convert_idr_to_usd(amount_idr):
    exchange_rate = get_exchange_rate_idr_to_usd()
    amount_usd_raw = amount_idr * exchange_rate
    amount_usd = amount_usd_raw.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    print(f"\n===================================================")
    print(f"Konversi IDR ke USD")
    print(f"Mata Uang Awal (IDR): Rp {amount_idr:,.2f}")
    print(f"Nilai Tukar (IDR ke USD): 1 IDR = {exchange_rate:.8f} USD")
    print(f"Hasil Konversi (USD): $ {amount_usd:,.2f}")
    print(f"===================================================")

    if amount_usd > 0:
        denominations_breakdown = greedy_denomination(amount_usd)

        print(f"\n--- Ringkasan Penukaran ---")
        total_units = 0
        for denom, count in denominations_breakdown.items():
            if denom >= 1:
                denom_type = "lembar uang kertas"
            else:
                denom_type = "keping koin"
            print(f"${denom:.2f} x {count} ({denom_type})")
            total_units += count
            
        print(f"Total lembar/keping yang diberikan: {total_units}")
    
    return amount_usd, denominations_breakdown

if __name__ == "__main__":
    try:
        rupiah_input = Decimal(input("\nMasukkan jumlah Rupiah (IDR) yang akan ditukar: Rp. "))
        convert_idr_to_usd(rupiah_input)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

