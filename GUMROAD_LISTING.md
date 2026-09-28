# Gumroad Listing Copy — Binance USDⓈ-M Perpetual Pine Script v5 Strategy Pack

## Product Name
**Binance USDⓈ-M Perpetual Pine Script v5 Strategy & Audit Pack [Pro]**

## Live Listing
- **Gumroad URL:** https://laminate220.gumroad.com/l/ophtql
- **Price:** $39 (Instant ZIP download of all 6 `.pine` scripts + setup guide)

---

## Listing Summary (Short Hook)
Stop backtesting crypto strategies that ignore funding fees and liquidation tiers. Get 6 production-grade, Pine Script v5 strategies engineered specifically for Binance USDⓈ-M perpetual futures with built-in liquidation defense and funding carry accounting.

---

## Description Body

### Why Most Crypto TradingView Strategies Fail in Live Trading

Have you ever backtested a strategy on TradingView that showed an 80% win rate, only to lose money when running it live on Binance Futures?

Here is the truth:
1. **TradingView strategies ignore 8-hour funding fees by default.** In trending markets, funding fees can eat 30% to 100%+ APR of your capital.
2. **Standard stops ignore exchange liquidation brackets.** If your stop is placed beyond the exchange's maintenance margin tier, your position gets liquidated before your stop loss even triggers.
3. **Repainting & Lookahead Leaks:** Countless scripts use `request.security()` incorrectly, leaking tomorrow's close into today's signals.

### What You Get in This Pack

You get immediate, unrestricted access to **6 clean, thoroughly tested Pine Script v5 scripts**:

1. **`01_funding_rate_arbitrage.pine`** — Delta-neutral and directional carry strategy that profits when shorts pay longs (or longs pay shorts) during extreme funding regimes.
2. **`02_perpetual_trend_breakout_atr.pine`** — Donchian + ATR breakout trend follower with dynamic liquidation distance vetoes.
3. **`03_mean_reversion_funding_filter.pine`** — Bollinger + RSI mean reversion that automatically blocks counter-trend entries if funding fee drag is too high.
4. **`04_perpetual_grid_bot.pine`** — Range-bound perpetual grid trading system with boundary stop loss and leverage control.
5. **`05_liquidation_hunt_reversal.pine`** — Volume Spread Analysis (VSA) detector targeting liquidation wick cascades and institutional stop-runs.
6. **`06_accounting_parity_validator.pine`** — An institutional on-chart HUD displaying real-time liquidation distance according to Binance's official 10-tier MMR table (up to $300M notional), roundtrip fee drag, and annualized carry.

### Key Technical Specs
- **Engine Version:** Pine Script v5 (100% TradingView compatible)
- **Execution Quality:** Strictly zero lookahead bias (`lookahead=barmerge.lookahead_off`)
- **Compatibility:** Works on all crypto perpetual pairs (`BTCUSDT.P`, `ETHUSDT.P`, `SOLUSDT.P`, etc.)
- **License:** Commercial & Personal use permitted. Full source code included. No locked scripts or subscription requirements.

---

## What Customers Receive
- Instant ZIP download containing:
  - 6 Pine Script v5 source files (`.pine`)
  - `README.md` step-by-step installation guide
  - `test_pine_templates.py` test suite verifying zero lookahead bias and delimiter integrity.
