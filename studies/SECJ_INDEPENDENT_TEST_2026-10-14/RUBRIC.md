# Bewertungsskala für unabhängige Bewerterinnen und Bewerter (SEC-J)

**Version:** 1.0 · 2026-10-14 · **gehört zu:** [PROTOCOL.md](PROTOCOL.md)

Sie bewerten jede Maßnahme auf **vier Achsen**, jeweils auf einer Skala von **0,00 bis 1,00 in Schritten von 0,05**. Grundlage ist ausschließlich die Fallmappe (`case_packets/`) und Ihr Fachwissen. Bitte keine weiteren Provolution-Dokumente lesen. Dort stehen die Bewertungen der Autoren.

Zu jeder Maßnahme notieren Sie außerdem Ihre **Sicherheit** (1 = geraten … 5 = sehr sicher) und die **benötigte Zeit** in Minuten.

---

## S · Suffizienz: Reicht die Wirkung?

*Leitfrage:* Erreicht die Maßnahme den Beitrag, den sie für das in der Fallmappe genannte Problem leisten müsste?

| Wert | Anker |
|---:|---|
| 0,00 | keine nennenswerte Wirkung auf das Problem |
| 0,25 | kleiner Bruchteil des nötigen Beitrags |
| 0,50 | etwa die Hälfte des nötigen Beitrags |
| 0,75 | großer Teil des nötigen Beitrags, Lücke klein |
| 1,00 | der nötige Beitrag wird vollständig oder darüber hinaus erreicht |

## E · Effizienz: Steht der Aufwand im Verhältnis?

*Leitfrage:* Wie gut ist das Verhältnis von Ressourcen (Geld, Personal, Material, Zeit) zur Wirkung, **verglichen mit realistischen Alternativen** für dasselbe Ziel?

| Wert | Anker |
|---:|---|
| 0,00 | deutlich aufwendiger als jede vernünftige Alternative |
| 0,25 | aufwendiger als die meisten Alternativen |
| 0,50 | durchschnittlich |
| 0,75 | günstiger als die meisten Alternativen |
| 1,00 | unter den günstigsten bekannten Wegen zu diesem Ziel |

## C · Konsistenz: Widerspruchsfrei?

*Leitfrage:* Verträgt sich die Maßnahme mit anderen Klimamaßnahmen, mit physikalischen und ökonomischen Randbedingungen und mit sich selbst (keine inneren Zielkonflikte)?

| Wert | Anker |
|---:|---|
| 0,00 | direkter, unauflösbarer Widerspruch (z. B. hebt eine andere zentrale Maßnahme auf) |
| 0,25 | schwere Zielkonflikte, nur mit großem Aufwand lösbar |
| 0,50 | relevante Zielkonflikte, lösbar |
| 0,75 | kleinere Reibungen, überwiegend vereinbar |
| 1,00 | keine erkennbaren Konflikte, klare Synergien |

## J · Gerechtigkeit: Wer gewinnt, wer verliert?

*Leitfrage:* Wie wirkt die Maßnahme auf die Verteilung von Lasten und Nutzen, besonders für benachteiligte Gruppen? Bitte vier Teilaspekte mitdenken:

- **J1 Interessenkonflikt:** Profitieren vor allem diejenigen, die die Maßnahme durchsetzen?
- **J2 Partizipation:** Können Betroffene mitentscheiden?
- **J3 Verteilungswirkung:** Wer trägt Kosten, wer erhält Nutzen?
- **J4 Vulnerabilität:** Werden besonders verletzliche Gruppen geschützt oder belastet?

| Wert | Anker |
|---:|---|
| 0,00 | diskriminiert oder belastet Benachteiligte schwer |
| 0,25 | verschärft Ungleichheit deutlich |
| 0,50 | neutral oder gemischt (**Werte unter 0,50 lösen im Framework ein Veto aus**) |
| 0,75 | verbessert die Lage Benachteiligter erkennbar |
| 1,00 | verbessert die Lage Benachteiligter deutlich, Betroffene sind beteiligt |

---

## Hinweise

- Bewerten Sie **jede Achse unabhängig** von den anderen. Eine teure Maßnahme kann trotzdem gerecht sein.
- Fehlen Ihnen Informationen, bewerten Sie nach bestem Wissen und senken Sie die **Sicherheit**. Bitte keine Achse leer lassen.
- Den Gesamtwert müssen Sie nicht berechnen; das geschieht in der Auswertung.
- Die Trainingsfälle T01 und T02 dienen nur dem Einüben der Skala und werden nicht ausgewertet.

> **Hinweis zur Herkunft der Skala:** Band 5 definiert S, E und J als Formeln (z. B. S = Wirkung / Mindestwirkung) und C binär (0/1). Die vorhandenen Scores im Repo sind aber abgestufte Experten-Urteile (z. B. C = 0,82). Diese Skala macht das Urteil explizit und für Dritte nachvollziehbar. Ob unabhängige Personen damit dieselben Werte erreichen, ist genau die Frage dieses Tests.
