SELECT w1.id FROM Weather w1, Weather w2
WHERE w1.temperature > w2.temperature
AND TO_DAYS(w1.RecordDate) - TO_DAYS(w2.RecordDate) = 1