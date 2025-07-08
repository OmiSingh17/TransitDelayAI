# 🚇 TransitDelayAI

> 🧠 “Which routes operate after 8 PM on Sundays?” — Just ask, and AI will code the answer.

**TransitDelayAI** is a smart, AI-powered project that analyzes public transit data using GTFS files and natural language queries — no cloud API needed.

This project blends **Python**, **data analysis**, and **GenAI (via Ollama + Mistral)** to explore late-night transit behavior, with a modular design built for clarity, reuse, and real-world application.

---

## 🔑 Key Features

- ✅ Analyze GTFS data (`trips.txt`, `calendar.txt`, `stop_times.txt`)
- 🔎 Detect routes operating after 8 PM on Sundays
- 🗣 Use **natural language** to query data via **local LLMs**
- 🧱 Modular design with reusable logic in `utils/`
- 🖥 AI runs **fully offline** with **Ollama + Mistral**
- 🚀 Ready for future prediction, visualizations & alerts

---

## 🤖 How AI Is Used

This project uses a **locally running Mistral LLM** via [Ollama](https://ollama.com) to convert natural language questions into working Python code.

### 📦 Example AI Prompts:
- “Which routes operate after 8 PM on Sundays?” ✅
- “Which trip has the longest duration?”
- “Which route has the most stops?”
- “List trips that don’t run on weekdays”

All code responses are parsed, verified, and safely executed using `subprocess` + `re`.

---

## 🖼 Sample Output

```bash
✅ Routes operating after 8 PM on Sundays:
['142', '155', '198', '201']

## 🛠 Tech Stack & Tools

| Area               | Tools/Tech Used                        |
|--------------------|----------------------------------------|
| Language           | Python                                 |
| Data Processing    | pandas, GTFS static files              |
| GenAI/LLM          | [Ollama](https://ollama.com) + Mistral LLM |
| Prompt Engineering | Custom system prompts, safe code execution |
| Folder Structure   | Modular: `utils/`, `data/`, `interface/` |
| Version Control    | Git + GitHub                           |

TransitDelayAI/
├── data/                  # GTFS input files (calendar, trips, stop_times)
├── utils/                 # Reusable logic modules
│   └── sunday_routes.py
├── Ollama_interface/      # GenAI prompt and response engine
│   └── ollama_interface.py
├── output/                # Optional for charts/logs
├── main.py                # Clean entry point for running logic
└── README.md
