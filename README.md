# 🧠 Hello World AI Agent

![Demo](demo.gif)

This project demonstrates a minimal AI Agent that monitors a folder and automatically sorts files into subfolders based on type.

## 🧪 Agents

### ✅ Polling Agent
- Uses a `while True + sleep` loop to poll for changes every 2 seconds.

### ✅ Event-driven Agent
- Uses the `watchdog` library to react to new files instantly via OS file system events.

### ✅ LLM Agent (OpenAI + Gemini)
- Uses OpenAI or Gemini (Google) models to reason about file types from names and sort them accordingly.

---

## ⚙️ Setup

```bash
# Create virtual environment (optional)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📂 Folder Structure

```bash
hello-world-agent/
├── polling_agent.py
├── event_agent.py
├── llm_agent.py
├── benchmark_runner.py
├── requirements.txt
├── .env
├── demo.gif
└── README.md
```

## 🧪 Running the Agents

### Polling Agent

```bash
python polling_agent.py test_files/
```

### Event Agent

```bash
python event_agent.py test_files/
```

### LLM Agent (Gemini or OpenAI)

```bash
# Set keys in .env first
python llm_agent.py test_files/
```

### Benchmark

```bash
python benchmark_runner.py
```
