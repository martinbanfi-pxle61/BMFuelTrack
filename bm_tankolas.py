import math
import random


def bm_calc_consumption(liters, distance_km):
    if distance_km <= 0:
        raise ValueError("A megtett távolság legyen pozitív.")
    return liters / distance_km * 100


class BMTankolasManager:
    def __init__(self):
        self.records = []

    def bm_add_record(self, liters, price_per_liter, distance_km):
        consumption = bm_calc_consumption(liters, distance_km)
        total_cost = liters * price_per_liter
        rec_id = random.randint(1000, 9999)
        record = {
            "id": rec_id,
            "liters": liters,
            "price_per_liter": price_per_liter,
            "distance_km": distance_km,
            "consumption": consumption,
            "total_cost": total_cost,
        }
        self.records.append(record)
        return record

    def bm_delete_record(self, index):
        if 0 <= index < len(self.records):
            del self.records[index]
            return True
        return False

    def get_consumptions(self):
        consumptions = []
        for r in self.records:
            consumptions.append(r["consumption"])
        return consumptions

    def get_summary(self):
        consumptions = self.get_consumptions()
        if not consumptions:
            return None
        count = len(consumptions)
        total = 0.0
        minimum = consumptions[0]
        maximum = consumptions[0]
        for value in consumptions:
            total += value
            if value < minimum:
                minimum = value
            if value > maximum:
                maximum = value
        avg = total / count
        sorted_values = sorted(consumptions)
        if count % 2 == 1:
            median_value = sorted_values[count // 2]
        else:
            m1 = sorted_values[count // 2 - 1]
            m2 = sorted_values[count // 2]
            median_value = (m1 + m2) / 2
        if count > 1:
            var_sum = 0.0
            for value in consumptions:
                diff = value - avg
                var_sum += diff * diff
            variance = var_sum / count
            stdev = math.sqrt(variance)
        else:
            stdev = 0.0
        return {
            "avg": avg,
            "median": median_value,
            "stdev": stdev,
            "min": minimum,
            "max": maximum,
            "count": count,
        }

    def format_summary(self):
        summary = self.get_summary()
        if summary is None:
            return "Még nincs adat."
        avg_rounded = math.ceil(summary["avg"] * 10) / 10
        min_floor = math.floor(summary["min"])
        max_floor = math.floor(summary["max"])
        lines = [
            f"Tankolások száma: {summary['count']}",
            f"Átlag fogyasztás: {avg_rounded:.1f} l/100km",
            f"Medián: {summary['median']:.1f} l/100km",
            f"Minimum: {min_floor} l/100km",
            f"Maximum: {max_floor} l/100km",
            f"Szórás: {summary['stdev']:.2f}",
        ]
        return "\n".join(lines)
