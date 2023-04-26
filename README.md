## Barcode chart collector

With this tool, you can create a list of trading pairs that trade close to their minimum tradeable prices, producing so-called "barcode charts".

The app achieves this by generating a list of pairs that are traded under the price of the given pair's tick size multiplied by a configurable multiplier. This enables you to quickly collect trading pairs that fit your criteria and generate barcode charts for your analysis.

Supported exchanges:

-   KuCoin (spot markets)
-   OKEx (spot markets)

### How to run

1. Install the packages: `pipenv install`
2. Input your exchange API keys into the `secrets.json` file
3. Run the script: `python main.py`

### Configuration

The markets and the tick size multiplier can be configured in `main.py`.
