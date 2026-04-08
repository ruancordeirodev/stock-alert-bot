import time

from app.services.fetcher import get_price
from app.core.alert import check_alert
from app.core.state import init_db, has_triggered, set_triggered


ASSETS = {
    "PETR4.SA": {"target": 44, "mode": "below"},
    "VALE3.SA": {"target": 70, "mode": "above"},
    "ITUB4.SA": {"target": 30, "mode": "below"}
}


def run():
    init_db()

    print("🚀 Alert Bot iniciado")

    while True:
        for symbol, config in ASSETS.items():

            price = get_price(symbol)

            print(f"{symbol} -> {price}")

            if price is None:
                continue

            alert = check_alert(
                symbol,
                price,
                config["target"],
                config["mode"]
            )

            if alert and not has_triggered(symbol):
                print(f"🚨 ALERTA: {symbol} -> {price}")
                set_triggered(symbol, 1)

            if not alert and has_triggered(symbol):
                set_triggered(symbol, 0)

        time.sleep(5)


if __name__ == "__main__":
    run()