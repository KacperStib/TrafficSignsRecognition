# Jak podłączyć Bazy Danych?

## Co będziemy potrzebować:
- [SQL Server Management Studio 20.1 (SSMS):](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16#download-ssms)


- [Microsoft® SQL Server® 2019 Express:](https://www.microsoft.com/en-us/download/details.aspx?id=101064)


- [LabView Database Connectivity Toolkit:](https://www.ni.com/en/support/downloads/software-products/download.labview-database-connectivity-toolkit.html#411229)


## Krok pierwszy:
Pierwsze co instalujem to SQL Server Express (nie SSMS), 
Na samym początku wybieramy opcję żę chcemy opcję instalcji custom.
Wybieramy, gdzie chcemy zainstalować serwer.
Zacznie się nam pobierać i instalować serwer.
Gdy już się skończy pobierać, wyskoczy nam okno SQL Server Center - wybieramy pierwszą opcję *New SQL Server Stand-alone installation*.
Akceptujemy regulamin.
W upadte wybieramy według upodobań.
Jak pojawi nam się *Feature Selection*:
 - odznaczamy Machine Learning,
 - **Upewniamy się**, że mamy w kategorii *Shared Features* (znajduje się niżej)
 zaznaczone wszystko oprócz *Local DB*.

 Idziemy dalej.
W *Instance Configuration* nic nie zmieniamy.
W *Server Configuration* przeklikujemy dalej.
W *Database Engine Configuration* też.
I instalacja leci.
Jak się zakończy - idziemy kroku drugiego.

## Krok Drugi
Uruchamiamy instalację SSMS.
Wybieramy gdzie chcemy zainstalować i lecimy dalej.
Jak się zainsataluje - odpalamy SSMS.

## Krok Trzeci
Jak odpali się nam SSMS:
 - Wyskoczy nam okno Connect To Server,
 - zapisujemy to, co jest w Server Name (przyda się później),
 - w Encryption wybieramy Optional,
lecimy dalej - klikamy.

Po lewej stronie mamy drzewko - klikamy prawym w Databases i tworzymy nową bazę danych, ja ustawiam sobie nazwę "Signs" - nic nie zmieniamy i klikamy OK.
Po lewej pojawi się taki **walec** jako baza "Signs" - klikamy na plusik, by rozwinąć, następnie prawym na tabelę - new i Table.
Dodajemy kolumny - w moim przypadku dodałem kolumnę ID (int), Path (varchar(50)), Category (varchar(50)), odznaczamy Allow Null.
Klikamy prawym na ID i wybieramy Primary Key.
W właściwościach ID zaznaczamy Identity Specification (Is Identity) na True.
Klikamy ctrl+s i dajemy nazwę tabelii - ja dałem "LabviewSigns".
Następnie po lewej możemy sobie kliknąć na "folder" Tables i zobaczyć, czy wygenerowała nam się tabela (będzie z początkiem dbo.*nazwa*).
Minimaluzjemy SMSS i przechodzimy do kolejnego kroku.

## Krok Czwarty
Tutaj ważne jest, by wiedzieć jaki mamy system - 32 czy 64 bitowy.
W menu start (zakładam że macie Windowsa), wpisujemy ODBC.
Wyskoczą wam dwie aplikacje - wybieracie tę z waszą wersją systemu, u mnie to jest 64 bity.
Gdy się to nam uruchomi, domyślnie jesteśmy w DSN użytkownika - klikamy sobie dodaj.
Wyskoczy nam wybór sterownika - wybieramy **SQL Server** (jest pośrodku),
Nazwę dajemy sobie jaką chcemy - ja dam RecLab (zaraz będzie ta nazwa nam potrzebna), opis skip i w Serwerze dajemy to, co zapisaliśmy sobie na początku kroku trzeciego - to co mieliśmy w Server name.
Dajemy dalej (nie zakończ), następnie nic nie zmienamy i dalej, następnie zaznaczamy domyślną bazę danych na naszą (*Sings*) i dalej, i dalej, zakończ i Testuj źródło danych - jeżeli wszystko wykonaliśmy dobrze - dostanimy komunikat, że **TESTY UKOŃCZONE POMYŚLNIE!** i dajemy ok.
Możemy teraz przejść do LabView

## Krok Piąty
Otwieramy nasz projekt i wchodzimy w databaseInsert.vi.
Po lewej jest string - tutaj wpisujemy nazwę z kroku czwartego (RecLab).
jeżeli wszystko poszło dobrze - możemy wrócić do SMSS i na pasku znaleźć New Query - 
``
select * from LabviewSigns
``
Dostaniemy zapisane w niej rekordy.



### Walec