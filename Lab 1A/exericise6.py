import requests
from time import sleep
from bs4 import BeautifulSoup

def scrape_block(blocknumber, page):
    # the URL of the web page that we want to get transaction data
    api_url = "https://etherscan.io/txs?block=" + str(blocknumber) + "&p="+str(page)
    # HTTP headers used to send a HTTP request
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0'}
    # Pauses for 0.5 seconds before sending the next request
    sleep(0.5)
    transaction_fee_sum = 0
    transaction_count = 0
    # send the request to get data in the webpage
    response = requests.get(api_url, headers=headers)
    # get the transaction table from the response data we get
    for row in BeautifulSoup(response.content, 'html.parser').select('table.table-hover tbody tr'):
        # each row in the table is a transaction
        attributes = map(lambda x: x.text, row.findAll('td'))
        # extract transaction attributes
        _begin, hash, method, block, timestamp1, age, from1, _arr, to1, value1, txnfee, burnfee = attributes

        transaction_fee_sum += float(txnfee)
        transaction_count += 1

        if transaction_count == 50:
            return transaction_fee_sum, transaction_count

        ######################## modify code below for each exercise #######################
        # print("transaction of ID:", hash, "block:", block, "from address", from1, "toaddress", to1, "transaction fee",txnfee)

    return transaction_fee_sum, transaction_count

if __name__ == "__main__":  # entrance to the main function
    transaction_fee_sum_block_1, transaction_count1 = scrape_block(15479087, 1)
    transaction_fee_sum_block_2, transaction_count2 = scrape_block(15479088, 1)

    print("Number of transactions:",transaction_count1+transaction_count2)

    average_fee = (transaction_fee_sum_block_1+transaction_fee_sum_block_2)/(transaction_count1+transaction_count2)
    print("Average fees of the first 50 transactions in block 15479087 and the first 50 transactions in block 15479088:")
    print(average_fee)