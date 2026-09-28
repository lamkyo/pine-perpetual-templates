# Binance USDⓈ-M Perpetual TradingView Pine Script v5 Strategy Pack

A collection of 6 production-grade, accounting-aware Pine Script v5 strategies and indicators specifically engineered for Binance USDⓈ-M and crypto perpetual futures.

---

## ⚡ The Fundamental Flaw of Most Retail Pine Scripts

95% of public TradingView indicators and strategies fail when deployed on real crypto perpetuals because they commit 3 fatal errors:
1. **Ignoring Funding Fee Decay:** Holding perpetual positions over days or weeks accumulates 8-hour funding fees that silently destroy backtest PnL.
2. **Naive Stop Loss vs. Liquidation Engine:** Setting standard stops without knowing where Binance's isolated/cross margin liquidation price lies according to the official maintenance margin ratio (MMR) tiers.
3. **Lookahead Bias & Repaint:** Using `request.security()` with default lookahead settings that leak future bar closes into historical calculations.

This pack solves all three. Every script is strictly written in **Pine Script v5**, with explicit `lookahead=barmerge.lookahead_off`, deterministic math, and real Binance USDⓈ-M margin mechanics.

---

## 📦 What's Inside the Pack

### 1. `01_funding_rate_arbitrage.pine` (Strategy)
- **Concept:** Funding Rate Carry & Basis Arbitrage.
- **Mechanism:** Monitors the live Binance 8h funding rate on perpetuals. Enters Long when funding is deeply negative (shorts subsidize longs) and Short when funding is excessively positive.
- **Risk Control:** Includes ATR trailing stops and an emergency liquidation safety buffer.

### 2. `02_perpetual_trend_breakout_atr.pine` (Strategy)
- **Concept:** Volatility-adjusted breakout trend follower.
- **Mechanism:** Dual Donchian Channels with 200 EMA macro regime filter and dynamic ATR trailing stop.
- **Safety Gate:** Computes isolated margin liquidation price on every bar; automatically aborts breakout entries if the liquidation distance is tighter than the safety threshold.

### 3. `03_mean_reversion_funding_filter.pine` (Strategy)
- **Concept:** Range mean-reversion with funding penalty filter.
- **Mechanism:** Bollinger Bands + RSI extremes. Automatically vetoes trades if entering counter-trend would incur high funding drag against the position.

### 4. `04_perpetual_grid_bot.pine` (Strategy)
- **Concept:** Perpetual range grid trader with liquidation risk bounds.
- **Mechanism:** Divides a defined price corridor into geometric grid bands, systematically capturing volatility inside the range while strictly enforcing boundary hard stops.

### 5. `05_liquidation_hunt_reversal.pine` (Strategy)
- **Concept:** Volume Spread Analysis (VSA) stop-run / liquidation wick detector.
- **Mechanism:** Identifies abnormal volume surges accompanied by long wick rejection candles (classic liquidation cascade flushes). Enters sniper reversals with asymmetric risk-to-reward ratios.

### 6. `06_accounting_parity_validator.pine` (Indicator / On-Chart HUD)
- **Concept:** Professional risk & accounting dashboard.
- **Features:**
  - Real-time Liquidation Price based on the official Binance 10-tier MMR table (up to 300M notional).
  - Safety Distance to Liquidation in % and USDT.
  - Annualized Funding Carry (APR).
  - Roundtrip Friction Hurdle (Maker/Taker fees + slippage in bps and USDT).

---

## 🚀 Quick Setup Guide (TradingView)

1. Open [TradingView](https://www.tradingview.com/) and navigate to any crypto perpetual chart (e.g., `BINANCE:BTCUSDT.P`).
2. At the bottom of the screen, open the **Pine Editor** tab.
3. Open any `.pine` file from this folder in a text editor, copy all text, and paste it into the Pine Editor.
4. Click **Save**, then click **Add to Chart**.
5. Customize parameters (leverage, initial equity, funding thresholds) via the strategy/indicator Settings cog icon.

---

## 🧪 Parity & Compliance Verification

Run the automated test suite locally:
```bash
python3 -m pytest tests/test_pine_templates.py -v
```
Checks verified:
- TradingView Pine Script v5 directive compliance (`//@version=5`)
- Elimination of lookahead bias (`barmerge.lookahead_off`)
- Exact syntactic delimiter balancing
- Full parity with Binance 10-tier USDⓈ-M risk brackets
