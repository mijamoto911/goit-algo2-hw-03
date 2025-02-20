# 📦 GOIT-ALGO2-HW-03

Цей проєкт містить два основні завдання:

1. **Моделювання логістичної мережі та розрахунок максимального потоку** (алгоритм Едмондса-Карпа)
2. **Порівняння ефективності OOBTree та dict** для діапазонних запитів.

1️⃣ Завдання 1: Логістична мережа та максимальний потік
Програма створює граф логістичної мережі, додає термінали, склади, магазини і знаходить максимальний потік між джерелом та стоком.

📍 Як запустити:

python scripts/edmonds_karp.py

📈 Візуалізація:
Щоб побудувати граф логістики, виконайте:

python scripts/graph*flow_logistic.py
🏆 Вихідні дані:
Розрахований максимальний потік через логістичну мережу.
Таблиця потоків між терміналами та магазинами (логістична*мережа_потоки.csv).
2️⃣ Завдання 2: Порівняння OOBTree vs Dict
Це завдання аналізує продуктивність OOBTree (BTrees) та dict для виконання діапазонних запитів.

📍 Як запустити:

python scripts/oob_tree.py

⏳ Вихідні дані:
Час виконання 100 діапазонних запитів для OOBTree та Dict (збережені в performance_results.txt).
📊 Очікуваний вивід:

Total range_query time for OOBTree: 0.0005 seconds
Total range_query time for Dict: 0.0057 seconds
✅ Очікується, що OOBTree працює швидше, оскільки використовує впорядковану структуру даних.

🔥 Висновки
Логістична мережа: алгоритм Едмондса-Карпа дозволяє знайти оптимальний маршрут для постачання товарів.
OOBTree vs Dict: OOBTree швидший у діапазонних запитах, але потребує більше пам’яті.

Автор: Eduard Schumacher
Email: mijamoto911@gmail.com

🔗 Додатково:
📄 Документація NetworkX: NetworkX Docs
📄 Алгоритм Едмондса-Карпа: Wikipedia
