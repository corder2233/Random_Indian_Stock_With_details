import requests

def rendom_stock():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        stock_data = data["data"]
        stock_name = stock_data["Name"]
        symbol = stock_data["Symbol"]
        c_price = stock_data["CurrentPrice"]
        HighLow = stock_data["HighLow"]
        mar_cap = stock_data["MarketCap"]
        PE = stock_data["StockPE"]
        ROE = stock_data["ROE"]
        Face_Value = stock_data["FaceValue"]

        return stock_name, symbol, c_price, HighLow, mar_cap, PE, ROE, Face_Value
    else:
        raise Exception("fatch failed")
    
def main():
        try:
            stock_name, symbol, c_price, HighLow, mar_cap,PE, ROE, Face_Value = rendom_stock()
            print(f"Stock Name:{stock_name} \nStock Symbol:{symbol} \n Current Price:{c_price} \n Price High_Low:{HighLow} \n Market cap:{mar_cap} \n Stock PE: {PE} \n ROE:{ROE} \n Face Value: {Face_Value}")
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
        main()