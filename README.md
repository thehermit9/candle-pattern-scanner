 Candle Pattern Signal Tool (Python)
This lightweight Python tool scans any OHLCV data (CSV format) and flags key candlestick patterns:

Doji

Bullish Engulfing

Bearish Engulfing

Hammer

📤 Outputs
signals.csv – Timestamps of detected candle patterns

chart.png – Candle chart with pattern markers

No bloated libraries. No unnecessary dependencies. Just clean, modifiable Python.

🚀 How to Use
Install requirements
pip install -r requirements.txt

Run the scanner and plotter
python candle_trigger_generator.py
python plot_signals.py

Review your outputs

View signals.csv for pattern matches

View chart.png for a visual chart of pattern locations

🔧 Customize It
Modify pattern sensitivity in config.json

Use any OHLCV-format CSV with these columns:
time, open, high, low, close, volume

📦 Download Full Tool
👉 Get the full bundle on Gumroad (Free): https://luke33.gumroad.com/l/candletool
Includes sample data, signal generator, plotting script, config file, and output examples.

License
MIT License — use, modify, and redistribute freely.

This version is free — leave a tip if you find it helpful.
