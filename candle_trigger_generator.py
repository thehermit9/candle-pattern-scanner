import pandas as pd

# --- Configurable pattern rules ---
PATTERNS = {
    "bullish_engulfing": lambda o, c, po, pc: (po > pc and c > o and c > po and o < pc),
    "bearish_engulfing": lambda o, c, po, pc: (po < pc and c < o and c < po and o > pc),
    "doji": lambda o, c, _, __: abs(c - o) / ((c + o) / 2) < 0.001,
    "hammer": lambda o, c, l, h: (c > o) and ((o - l) > 2 * (c - o)),
}

def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=["time"])
    df = df.sort_values("time").reset_index(drop=True)
    return df

def detect_patterns(df):
    signals = []
    for i in range(1, len(df)):
        row, prev = df.iloc[i], df.iloc[i - 1]
        for name, rule in PATTERNS.items():
            if rule(row['open'], row['close'], prev['open'], prev['close']):
                signals.append((row["time"], name))
                break
    return pd.DataFrame(signals, columns=["time", "pattern"])

def main():
    df = load_data("btc_sample.csv")
    signal_df = detect_patterns(df)
    signal_df.to_csv("signals.csv", index=False)
    print("✅ Signals saved to signals.csv")

if __name__ == "__main__":
    main()
