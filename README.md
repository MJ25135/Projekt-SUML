

# Predykcja Ocen Końcowych z Matematyki

Ten projekt przewiduje końcowe oceny uczniów z matematyki (`G3`) na podstawie danych socjodemograficznych i edukacyjnych. Aplikacja umożliwia wprowadzanie szczegółowych informacji o uczniu oraz uzyskanie przewidywanej oceny.

---

## Struktura Projektu

- **`data/student-mat.csv`**:  
  Zawiera zbiór danych używany do trenowania i ewaluacji modelu. Dane obejmują informacje o demografii uczniów, środowisku rodzinnym, nawykach naukowych i ocenach.  

- **`app.py`**:  
  Frontend aplikacji oparty na Streamlit. Udostępnia przyjazny interfejs użytkownika do wprowadzania danych i wyświetlania przewidywanej oceny końcowej.

- **`data_preparation.py`**:  
  Zawiera kroki przetwarzania i przygotowania danych

- **`model.py`**:  
  Implementacja modelu uczenia maszynowego przy użyciu Random Forest Regressor. Zawiera kroki przetwarzania danych, trenowanie modelu, ewaluację oraz logikę predykcji.

---

## Kluczowe Funkcje

- Predykcja końcowych ocen z matematyki na podstawie wprowadzonych danych.
- Wyświetlanie metryk jakości modelu (MAE, MSE, R² Score).
- Prosty i intuicyjny interfejs internetowy do wprowadzania danych i wyświetlania wyników.

---
