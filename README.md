<!-- [![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/YYgLXq0X)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11228617&assignment_repo_type=AssignmentRepo) -->
<h1 align="center">

<br>

<p align="center">
<img src="https://github.com/grochot-agh/final-project-group-name-not-found/blob/main/projekt/static/finger.png"  alt="Logo">
</p>

<br>

<br>

</h1>

<h4 align="center">CrimeMatch</h4>

<p align="center">
  <a >
    <img src="https://github.com/grochot-agh/final-project-group-name-not-found/blob/main/projekt/static/zdjecie1.png"
         alt="Screenshot">
  </a>
</p>

## Project Overview 🎉
Projekt miał na celu stworzenie responsywnej aplikacji webowej, umożliwiającej użytkownikom
wyszukiwanie i wprowadzanie informacji o przestępstwach za pomocą formularza. Wprowadzone
dane zostają zapisane w bazie danych SQL. Użytkownicy mają dostęp tylko do odpowiednich funkcji po zalogowaniu.  Dane są porównywane z innymi zgłoszeniami w bazie w celu znalezienia podobnych przypadków. Wyświetlane zostają odpowiednio posortowane dane przestępców i data przestępstwa. .<br>
Główne funkcje projektu obejmują:<br>
<strong>Formularz zgłoszeń:</strong> Zalogowany użytkownik może wprowadzać informacje dotyczące przestępstwa za pomocą intuicyjnego formularza. Formularz wymaga podstawowych informacji o popełnionym przestępstwie. Umożliwia wprowadzenie danych takich jak imię, nazwisko, wiek, miejsce zamieszkania, data przestępstwa, rodzaj przestępstwa, miejsce, pora oraz broń użyta przez przestępcę.<br>
<strong>Wyszukiwanie Przestępców:</strong> Użytownik może wprowadzić informacje dotyczące sprawy nad którą pracuje, aby wyszukać przestępców o najlepszym dopasowaniu. Użytkownik może wyszukiwać przestępstwa na podstawie określonych kryteriów, takich jak rodzaj przestępstwa, miejsce, pora oraz broń. Wyniki wyszukiwania są sortowane według odpowiednio dobranych wag dla każdego kryterium, a następnie wyświetlane.<br>
<strong>Usuwanie wyników:</strong> Jeśli zostaną wprowadzone błędne dane zalogowany użytkownik może je w każdej chwili usunąć. W widoku usuwania przestępców wyświetlana jest lista przestępców z ich identyfikatorami, imionami i nazwiskami. Po wybraniu przestępcy do usunięcia, zostaje on usunięty z bazy danych, a następnie aktualizowane są identyfikatory przestępców.<br>


## Tech/framework used 🔧

| Technologie                                             |                                    |
| Aplikacja CrimeMatch łączy Python, Flask, MySQL oraz HTML/CSS w celu stworzenia funkcjonalnego systemu zarządzania przestępstwami opartego na stronie internetowej.|<br>
| [Python](X)                           | Aplikacja została stworzona przy użyciu języka programowania Python.  |<br>
| [Flask](X)                           |  Flask jest frameworkiem webowym dla języka Python, który zapewnia narzędzia i biblioteki do budowy aplikacji internetowych. Jest używany do obsługi trasowania, obsługi żądań oraz renderowania szablonów w tej aplikacji.   |<br>
| [MySQL](X)                           | Aplikacja korzysta z MySQL jako systemu zarządzania bazą danych do przechowywania danych dotyczących przestępstw i użytkowników. Nawiązuje połączenie z serwerem MySQL przy użyciu biblioteki mysql.connector.  |<br>
| [HTML/CSS](X)                           | Front-end aplikacji został zbudowany przy użyciu HTML do strukturyzacji stron internetowych oraz CSS do stylizacji i układu.  |


## Screenshots 📺

<p align="center">
    <img src="https://github.com/grochot-agh/final-project-group-name-not-found/blob/main/projekt/static/logowanie.png" alt="Screenshot">
</p>

<p align="center">
    <img src="https://github.com/grochot-agh/final-project-group-name-not-found/blob/main/projekt/static/dodaj_przest%C4%99pstwo.png" alt="Screenshot">
</p>

<p align="center">
    <img src="https://github.com/grochot-agh/final-project-group-name-not-found/blob/main/projekt/static/szukaj.png" alt="Screenshot">
</p>
<p align="center">
    <img src="https://github.com/grochot-agh/final-project-group-name-not-found/blob/main/projekt/static/usun.png" alt="Screenshot">
</p>


## Instalacja 💾
Aby uruchomić aplikację, należy najpierw zainstalować niezbędne zależności i upewnić się, że jesteś połączony z VPN AGH. Można to zrobić, wykonując następujące kroki:

Krok 1: Upewnij się, że masz zainstalowany Python w wersji 3.x. <br>
Krok 2: Połącz się z VPN AGH, aby uzyskać dostęp do bazy danych.<br>
Krok 3: Sklonuj repozytorium aplikacji z GitHuba lub pobierz i rozpakuj archiwum ZIP.<br>
Krok 4: Przejdź do katalogu głównego aplikacji.<br>
Krok 5: Zainstaluj niezbędne zależności, korzystając z menadżera pakietów pip.<br>
Krok 6: Uruchom aplikację.<br>
Po wykonaniu tych kroków aplikacja powinna być dostępna pod adresem http://localhost:5000 w przeglądarce internetowej. Upewnij się, że jesteś nadal połączony z VPN AGH, aby aplikacja mogła prawidłowo korzystać z bazy danych.



## Available scripts

| Command                   | Description                   |     |
| ------------------------- | ----------------------------- | --- |
| `npm run start`           | Open local server             |     |
| `npm run build`           | Create optimized build        |     |
| `npm run test`            | Run tests                     |     |
