# TransitDelayAI

**TransitDelayAI** is a smart, AI-powered tool that analyzes public transit data to detect and explore delays using **GTFS** feeds and **local GenAI (Mistral via Ollama)**.

This solo-built project blends **Python**, **data analysis**, and **prompt engineering** to create a modular, real-world solution for exploring **late-night public transport service patterns**.

---

## Key Features

- Analyze GTFS data (`trips.txt`, `calendar.txt`, `stop_times.txt`)
- Identify routes running after 8 PM on Sundays
- Use **natural language** to query your data via **local LLMs (Ollama + Mistral)**
- Modular structure with reusable logic (`utils/`)
- No paid API needed — 100% local + open-source
- Designed for clarity, extensibility, and real-world applications

---

## Tech Stack & Tools

| Area              | Tools/Tech Used                           |
|-------------------|--------------------------------------------|
| Language          | Python                                     |
| Data Processing   | pandas, GTFS static files                  |
| GenAI/LLM         | [Ollama](https://ollama.com) + Mistral LLM |
| Prompt Engineering| Custom system prompts, safe code execution |
| Folder Structure  | Modular: `utils/`, `data/`, `interface/`   |
| Version Control   | Git + GitHub                               |

---

### How AI Is Used

This project connects to a local Mistral model using Ollama to convert **natural language questions** into working Python code.

**Example prompts you can ask:**
- "Which routes operate after 8 PM on Sundays?"
- "Which trip has the longest duration?"
- "Which route has the most stops on weekdays?"

## Sample Output

```bash
Routes operating after 8 PM on Sundays:
['142', '155', '198', '201']

