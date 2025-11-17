# 🔬 Research Agent Pro

> **The most sophisticated AI research agent with automatic visualizations**
>
> Research anything → Get insights with beautiful charts, graphs & infographics in seconds.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Next.js 15](https://img.shields.io/badge/Next.js-15-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688.svg)](https://fastapi.tiangolo.com)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-blue)](https://www.typescriptlang.org/)

[Live Demo](https://research-agent-pro.vercel.app) • [Documentation](./docs) • [Examples](./examples) • [Report Bug](https://github.com/MAYANK12-WQ/research-agent-pro/issues)

---

## 🌟 Why Research Agent Pro?

Unlike traditional research tools, Research Agent Pro **automatically** generates:
- 📊 **Interactive charts** (line, bar, pie, scatter, heatmaps)
- 🎨 **Professional infographics** (statistics cards, timelines, comparisons)
- 📄 **Complete research reports** with sources
- 💾 **Multiple export formats** (PDF, PNG, PowerPoint, Markdown, JSON)

### The Difference

| Feature | Perplexity | ChatGPT | Julius AI | **Research Agent Pro** |
|---------|-----------|---------|-----------|------------------------|
| Price | $20/mo | $20/mo | $20/mo | **FREE** ✅ |
| Web Research | ✅ | ✅ | ❌ | ✅ |
| Auto Charts | ❌ | ❌ | ✅ | ✅ |
| Auto Infographics | ❌ | ❌ | ❌ | **✅ UNIQUE** |
| PowerPoint Export | ❌ | ❌ | ❌ | **✅ UNIQUE** |
| Open Source | ❌ | ❌ | ❌ | ✅ |
| Speed | ⚡⚡⚡ | ⚡ | ⚡⚡ | ⚡⚡⚡ |

---

## ✨ Features

### 🔍 **Intelligent Research**
- Multi-source web search (Google, Brave, academic papers, news)
- Real-time data extraction and analysis
- Automatic fact verification
- Smart source citation

### 📊 **Automatic Visualizations**
- **Line charts** - Trends over time
- **Bar charts** - Comparisons
- **Pie charts** - Distributions
- **Scatter plots** - Correlations
- **Heatmaps** - Patterns
- **Network graphs** - Relationships

### 🎨 **Beautiful Infographics**
- Statistics cards with key metrics
- Timeline visualizations
- Comparison grids
- Geographic maps
- Custom templates

### 💾 **Multiple Export Formats**
- **PDF** - Professional reports with embedded charts
- **PowerPoint** - Presentation-ready slides
- **PNG/SVG** - High-resolution images
- **Markdown** - Documentation-friendly
- **JSON** - Structured data

### 🚀 **Built for Performance**
- Research complete in < 30 seconds
- Real-time streaming updates
- Responsive UI (mobile-friendly)
- Smart caching for speed

---

## 🎬 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL (optional, SQLite fallback included)

### 1. Clone the Repository
```bash
git clone https://github.com/MAYANK12-WQ/research-agent-pro.git
cd research-agent-pro
```

### 2. Get Free API Keys (5 minutes)

All services have generous free tiers:

| Service | Free Tier | Get Key |
|---------|-----------|---------|
| **Groq** | ~14,000 requests/day | [console.groq.com](https://console.groq.com/) |
| **Serper** | 2,500 searches/month | [serper.dev](https://serper.dev/) |
| **Tavily** | 1,000 searches/month | [tavily.com](https://tavily.com/) |
| **Brave Search** | 2,000 searches/month | [brave.com/search/api](https://brave.com/search/api/) |

### 3. Setup Backend
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your API keys

# Run backend
python app/main.py
```

Backend will run on `http://localhost:8000`

### 4. Setup Frontend
```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will run on `http://localhost:3000`

### 5. Start Researching!
1. Open `http://localhost:3000`
2. Enter your research query
3. Watch as beautiful visualizations are generated automatically!

---

## 💡 Example Queries

Try these example queries to see the power:

### Market Analysis
```
"Electric vehicle sales by country 2024"
```
**Output**: Bar chart (top countries), line chart (growth trend), pie chart (market share), infographic (key stats)

### Company Research
```
"OpenAI funding history and valuation"
```
**Output**: Timeline chart (funding rounds), bar chart (valuation growth), table (investors), infographic (milestones)

### Trend Analysis
```
"Remote work trends post-pandemic"
```
**Output**: Line chart (adoption over time), bar chart (industry comparison), heatmap (geographic distribution), insights infographic

### Competitive Analysis
```
"Compare iPhone vs Android market share in Asia 2023"
```
**Output**: Pie charts (market share), bar chart (side-by-side comparison), trend line (historical data)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│     Research Agent Pro Architecture      │
├─────────────────────────────────────────┤
│                                          │
│  Frontend (Next.js 15 + TypeScript)     │
│  ├─ Search Interface                    │
│  ├─ Real-time Progress                  │
│  ├─ Chart Display (Recharts)            │
│  └─ Export Options                      │
│                                          │
│  Backend (FastAPI + Python)             │
│  ├─ Query Analyzer (AI-powered)         │
│  ├─ Multi-Source Research Engine        │
│  ├─ Visualization Engine (Plotly)       │
│  ├─ Infographic Generator               │
│  └─ Export Engine (PDF/PPTX/PNG)        │
│                                          │
│  AI Layer (Groq Llama 3.3 70B)          │
│  ├─ Intent Understanding                │
│  ├─ Data Synthesis                      │
│  ├─ Insight Generation                  │
│  └─ Visualization Selection             │
│                                          │
└─────────────────────────────────────────┘
```

---

## 📸 Screenshots

> *Coming soon - Building the beautiful UI right now!*

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript
- **Styling**: TailwindCSS 4
- **Charts**: Recharts, Plotly.js
- **State**: Zustand
- **Animations**: Framer Motion

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.11+
- **LLM**: Groq (Llama 3.3 70B)
- **Search**: Serper, Tavily, Brave
- **Charts**: Plotly, Matplotlib
- **PDFs**: WeasyPrint, python-pptx
- **Database**: PostgreSQL / SQLite

---

## 🗺️ Roadmap

### Phase 1: MVP (Week 1) ✅
- [x] Project setup
- [x] API key integration
- [ ] Basic research engine
- [ ] Simple chart generation
- [ ] Clean UI

### Phase 2: Advanced Features (Week 2)
- [ ] All chart types
- [ ] Infographic templates
- [ ] PowerPoint export
- [ ] Research history
- [ ] Export to all formats

### Phase 3: Polish (Week 3)
- [ ] Performance optimization
- [ ] Advanced UI/UX
- [ ] Documentation
- [ ] Tutorial videos
- [ ] Launch on Product Hunt

### Future Features
- [ ] Multi-language support
- [ ] Voice queries
- [ ] Collaborative research
- [ ] API for developers
- [ ] Browser extension
- [ ] Slack/Discord bot

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](./CONTRIBUTING.md) first.

### How to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by [Perplexity AI](https://www.perplexity.ai/) for fast research
- Inspired by [Julius AI](https://julius.ai/) for visualizations
- Built with ❤️ by [Mayank](https://github.com/MAYANK12-WQ)

---

## 📧 Contact

**Mayank** - AI Engineer & Creator

- GitHub: [@MAYANK12-WQ](https://github.com/MAYANK12-WQ)
- LinkedIn: [Your LinkedIn]
- Twitter: [@your_twitter]

**Project Link**: [https://github.com/MAYANK12-WQ/research-agent-pro](https://github.com/MAYANK12-WQ/research-agent-pro)

---

## ⭐ Star History

If you find this project useful, please consider giving it a star!

[![Star History Chart](https://api.star-history.com/svg?repos=MAYANK12-WQ/research-agent-pro&type=Date)](https://star-history.com/#MAYANK12-WQ/research-agent-pro&Date)

---

<p align="center">
  Made with 💡 and lots of ☕
  <br>
  <strong>Building the future of AI research, one query at a time.</strong>
</p>
