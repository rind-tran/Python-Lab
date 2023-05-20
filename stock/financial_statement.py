from vnstock import *
import pandas


MA_CK = "MWG"
OUTPUT_DIR = r"C:\Users\Adm\Desktop\CK\Danh Muc dau tu\ban le"
OUTPUT_FILE = f"{OUTPUT_DIR}\{MA_CK}.xlsx"
FREQUENCY = "Quarterly" # Quarterly | Yearly

# Export Balance Sheet
df = financial_report (symbol=MA_CK, report_type="BalanceSheet", frequency=FREQUENCY)
try:
    with pandas.ExcelWriter(OUTPUT_FILE, mode='a') as writer:
        df.to_excel(writer, index=False, sheet_name="BalanceSheet")
except:
    df.to_excel(OUTPUT_FILE, index=False, sheet_name="BalanceSheet")

# Export Income Statement
df = financial_report (symbol=MA_CK, report_type="IncomeStatement", frequency=FREQUENCY)
with pandas.ExcelWriter(OUTPUT_FILE, mode='a') as writer:
    df.to_excel(writer, index=False, sheet_name="IncomeStatement")

# Export Cash Flow
df = financial_report (symbol=MA_CK, report_type="CashFlow", frequency=FREQUENCY)
with pandas.ExcelWriter(OUTPUT_FILE, mode='a') as writer:
    df.to_excel(writer, index=False, sheet_name="CashFlow")
