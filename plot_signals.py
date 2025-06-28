import pandas as pd
import matplotlib.pyplot as plt

def plot_signals(ohlcv_file, signals_file, output_file="chart.png"):
    df = pd.read_csv(ohlcv_file, parse_dates=["time"])
    signals = pd.read_csv(signals_file, parse_dates=["time"])

    df = df.sort_values("time")
    merged = pd.merge(df, signals, on="time", how="left")

    plt.figure(figsize=(12, 6))
    plt.plot(df["time"], df["close"], label="Close Price", alpha=0.7)

    for pattern in merged["pattern"].dropna().unique():
        matches = merged[merged["pattern"] == pattern]
        plt.scatter(matches["time"], matches["close"], label=pattern, s=60)

    plt.title("Price with Candle Pattern Signals")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"✅ Chart saved to {output_file}")

if __name__ == "__main__":
    plot_signals("btc_sample.csv", "signals.csv")
