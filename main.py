from datetime import datetime
import yfinance as yahoofinance
import argparse
import webbrowser as wb

parser = argparse.ArgumentParser()
parser.add_argument("--stockticker", dest="stockticker", metavar="stockticker", help="Stock Ticker info made easy. Only works with U.S. Stock Markets.", required=True)

def main():
    GetInformation = yahoofinance.Ticker(args.stockticker)
    getCurrencyStr = GetInformation.info['currency']
    print("Stock Ticker: $" + GetInformation.info['symbol'])
    print("Company Name:", GetInformation.info['longName'], "\n")
    print("Exchange Timezone:", GetInformation.info['exchangeTimezoneName'])
    print("Open Price:", GetInformation.info['open'], getCurrencyStr)
    print("Current Stock Price:", GetInformation.info['currentPrice'], getCurrencyStr)
    print("Previous Close:", GetInformation.info['previousClose'], getCurrencyStr, "\n")
    print("Shares Outstanding:", GetInformation.info['sharesOutstanding'])
    print("Shares Float:", GetInformation.info['floatShares'])
    print("Shares Short:", GetInformation.info['sharesShort'])
    print("Short Ratio:", GetInformation.info['shortRatio'], "\n")
    print("Dividend Yield:", GetInformation.info['dividendYield'])
    print("Dividend Rate:", GetInformation.info['dividendRate'])
    print("Dividend Payout Ratio:", GetInformation.info['payoutRatio'])
    getDividendYield = GetInformation.info['dividendYield']
    if getDividendYield == None:
        print("Dividends may not be paid on this stock", "\n")
    else:
        getdividenddate = datetime.fromtimestamp(GetInformation.info['lastDividendDate'])
        dateDividendString = f"{getdividenddate:%A %d %B %Y, %I:%M:%S %p}"
        print("Last Dividend Date: " + dateDividendString, "\n")
    print("Target High Price:", GetInformation.info['targetHighPrice'], getCurrencyStr)
    print("Target Median Price:", GetInformation.info['targetMedianPrice'], getCurrencyStr)
    print("Target Low Price:", GetInformation.info['targetLowPrice'], getCurrencyStr)
    stockAnalysisString = GetInformation.info['recommendationKey']
    print("Stock Analysis:", stockAnalysisString.capitalize(), "\n")
    print("Industry:", GetInformation.info['industry'])
    print("Sector:", GetInformation.info['sector'])
    print("Employees:", GetInformation.info['fullTimeEmployees'], "\n")
    print("Address 1:", GetInformation.info['address1'])
    print("Address 2:", GetInformation.info['zip'] + " " + GetInformation.info['city'])
    print("State:", GetInformation.info['state'])
    print("Country:", GetInformation.info['country'])
    print("Website:", GetInformation.info['website'], "\n")
    print("Phone Contact: " + GetInformation.info['phone'], "\n")
    print("Company Description:")
    print(GetInformation.info['longBusinessSummary'], "\n")
    print("Research Information", "\n")
    print("Stock Filings EDGAR: https://www.sec.gov/edgar/search/")
    print("Yahoo Finance Full Chart: https://finance.yahoo.com/chart/" + GetInformation.info['symbol'])
    print("Lookup for OTC Stocks: https://www.otcmarkets.com/")
    print("Stock Analysis: https://stockanalysis.com/")
    print("Search on the web for more info. Use search terms like stock screener, stock analysis, stock trading and many more..", "\n")
    askOpenWebsite(GetInformation.info['website'])

def askOpenWebsite(webaddress):
    print("Current Website:", webaddress)
    openwebsite = input("Do you want to open the website for this stock? (yes or no) ")
    if openwebsite == ("yes"):
        wb.open(webaddress)
        print("Done.", "\n")
    elif openwebsite == ("no"):
        print("OK. All Right.", "\n")
    print("When you start trading stocks, you can use a zero commission broker")
    print("Be aware of your choose with a stock broker")
    print("Have a great day")

if __name__ == "__main__":
    args = parser.parse_args()
    main()
